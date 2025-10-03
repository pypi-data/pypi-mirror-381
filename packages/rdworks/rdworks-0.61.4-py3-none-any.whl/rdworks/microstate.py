import math
import itertools
import logging
import importlib.resources
import itertools
import numpy as np
import pandas as pd
import networkx as nx
import copy

from collections import deque, defaultdict
from typing import Self, Iterator
from dataclasses import dataclass
from types import SimpleNamespace
from pathlib import Path

from rdkit import Chem

from rdworks import Conf, Mol
from rdworks.xtb.wrapper import GFN2xTB
from rdworks.tautomerism import ComprehensiveTautomers, RdkTautomers


logger = logging.getLogger(__name__)


kT = 0.001987 * 298.0 # (kcal/mol K), standard condition
C = math.log(10) * kT


# adapted from https://github.com/dptech-corp/Uni-pKa/enumerator
smarts_path = importlib.resources.files('rdworks.predefined.ionized')
AcidBasePatterns = pd.read_csv(smarts_path / 'smarts_pattern.csv')
AcidBasePatternsSimple = pd.read_csv(smarts_path / 'simple_smarts_pattern.csv')
UnreasonablePatterns = list(map(Chem.MolFromSmarts, [
    "[#6X5]",
    "[#7X5]",
    "[#8X4]",
    "[*r]=[*r]=[*r]",
    "[#1]-[*+1]~[*-1]",
    "[#1]-[*+1]=,:[*]-,:[*-1]",
    "[#1]-[*+1]-,:[*]=,:[*-1]",
    "[*+2]",
    "[*-2]",
    "[#1]-[#8+1].[#8-1,#7-1,#6-1]",
    "[#1]-[#7+1,#8+1].[#7-1,#6-1]",
    "[#1]-[#8+1].[#8-1,#6-1]",
    "[#1]-[#7+1].[#8-1]-[C](-[C,#1])(-[C,#1])",
    # "[#6;!$([#6]-,:[*]=,:[*]);!$([#6]-,:[#7,#8,#16])]=[C](-[O,N,S]-[#1])",
    # "[#6]-,=[C](-[O,N,S])(-[O,N,S]-[#1])",
    "[OX1]=[C]-[OH2+1]",
    "[NX1,NX2H1,NX3H2]=[C]-[O]-[H]",
    "[#6-1]=[*]-[*]",
    "[cX2-1]",
    "[N+1](=O)-[O]-[H]"
]))


def Boltzmann_weighted_average(energies: list[float], beta: float=1.0) -> float:
    energies = np.array(energies)
    relative_energies = energies - np.min(energies)
    boltzmann_factors = np.exp(-relative_energies * beta)
    Z = np.sum(boltzmann_factors)
    weights = boltzmann_factors / Z 
    return float(np.dot(weights, energies))


@dataclass
class IonizableSite:
    """(de)protonation site information"""
    atom_idx: int
    atom: str
    hs: int # number of H attached to the atom
    q: int # formal charge of the atom
    pr: bool # can be protonated?
    de: bool # can be deprotonated?
    name: str
    acid_base: str
    

class State:
    def __init__(self, 
                 smiles: str,
                 origin: str | None = None, 
                 transformation: str | None = None,
                 min_formal_charge: int = -2,
                 max_formal_charge: int = +2,
                 min_atomic_charge: int = -1,
                 max_atomic_charge: int = +1,
                 protomer_rule: str = 'default',
                 tautomer_rule: str | None = None) -> None:
        """Molecular state.

        Args:
            smiles (str): SMILES
            origin (str | None, optional): original SMILES before tautomerization or ionization. Defaults to None.
            transformation (str | None, optional): Tautomer, +H, -H, or None. Defaults to None.
            min_formal_charge (int, optional): min formal charge. Defaults to -2.
            max_formal_charge (int, optional): max formal charge. Defaults to +2.
            min_atomic_charge (int, optional): min atomic charge. Defaults to -1.
            max_atomic_charge (int, optional): max atomic charge. Defaults to +1.
            protomer_rule (str, optional): 
                Ioniziation patterns ('default' or 'simple').
                Defaults to 'default'.
            tautomer_rule (str, optional): 
                Tautomerization patterns ('rdkit' or 'comprehensive'). 
                Defaults to None.
        """
        self.smiles = smiles
        self.origin = origin # parent or origin
        self.transformation = transformation  # how this state is generated from origin
        self.min_formal_charge = min_formal_charge
        self.max_formal_charge = max_formal_charge
        self.min_atomic_charge = min_atomic_charge
        self.max_atomic_charge = max_atomic_charge
        self.protomer_rule = protomer_rule
        self.tautomer_rule = tautomer_rule

        self.rdmol = None
        self.rdmolH = None
        self.sites = []
        self.charge = None
        self.update()


    def __str__(self) -> str:
        """String representation.

        Returns:
            str: short description of the state.
        """
        return f"State(smiles={self.smiles}, sites={self.sites}, transformation={self.transformation}, origin={self.origin})"


    def __eq__(self, other: Self) -> bool:
        """Operator `==`."""
        if isinstance(other, State):
            return self.smiles == other.smiles
        return False
    
    
    def copy(self) -> Self:
        return copy.deepcopy(self)


    def update(self) -> None:
        self.rdmol = Chem.MolFromSmiles(self.smiles)
        self.rdmolH = Chem.AddHs(self.rdmol)
        self.find_ionizable_sites()
        self.charge = Chem.GetFormalCharge(self.rdmol)


    def info(self) -> None:
        print(f"SMILES: {self.smiles}")
        print(f"Formal charge: {self.charge}")
        print(f"Origin: {self.origin}")
        print(f"Transformation: {self.transformation}")
        print(f"Ionizable sites:")
        for site in self.sites:
            print(f"  - atom_idx= {site.atom_idx:2}, atom= {site.atom:>2},", end=" ")
            print(f"q= {site.q:+2}, hs= {site.hs:1},", end=" ")
            print(f"pr= {site.pr:1}, de= {site.de:1},", end=" ")
            print(f"acid_base= {site.acid_base}, name= {site.name}")
        print()


    def hydrogen_count(self, idx: int) -> int:
        atom = self.rdmolH.GetAtomWithIdx(idx)
        hydrogen_count = 0
        if atom.GetAtomicNum() == 1:
            for bond in atom.GetNeighbors()[0].GetBonds():
                neighbor = bond.GetOtherAtom(atom)
                if neighbor.GetAtomicNum() == 1:
                    hydrogen_count += 1
        else:
            for bond in atom.GetBonds():
                neighbor = bond.GetOtherAtom(atom)
                if neighbor.GetAtomicNum() == 1:
                    hydrogen_count += 1
        return hydrogen_count
    

    def site_info(self) -> list[tuple]:
        return [(site.atom, site.atom_idx, site.q, site.pr, site.de) for site in self.sites]       


    def can_be_protonated_at(self, atom_idx:int) -> bool:
        """Check if an atom can potentially be protonated"""
        atom = self.rdmol.GetAtomWithIdx(atom_idx)
        # Check formal charge (negative charge can be protonated)
        if atom.GetFormalCharge() < 0:
            return True
        
        # Check for atoms with lone pairs (N, O, S, P, etc.)
        # that aren't already fully protonated
        atomic_num = atom.GetAtomicNum()
        total_valence = atom.GetTotalValence()
        
        # Common protonatable atoms
        if atomic_num == 7:  # N, O, S
            if total_valence < 4:  # Can form NH4+
                return True
        elif atomic_num in [8, 16]:  # O, S
            if total_valence < 3:  # Can form OH3+ or SH3+
                return True
        
        return False


    def can_be_deprotonated_at(self, atom_idx:int) -> bool:
        """Check if an atom can potentially be deprotonated"""
        atom = self.rdmol.GetAtomWithIdx(atom_idx)
        # Check if atom has a positive formal charge (can lose H+)
        if atom.GetFormalCharge() > 0:
            return True
        
        # Check if atom has hydrogens that can be removed
        if atom.GetTotalNumHs() == 0:
            return False
        
        # Common deprotonatable atoms with acidic hydrogens
        if atom.GetAtomicNum() in [7, 8, 15, 16]:  # N, O, P, S
            return True
        
        return False
    

    def find_ionizable_sites(self) -> None:
        if self.protomer_rule == 'simple':
            template = AcidBasePatternsSimple
        elif self.protomer_rule == 'default':
            template = AcidBasePatterns
        else:
            template = AcidBasePatterns
        for idx, name, smarts, index, acid_base in template.itertuples():
            pattern = Chem.MolFromSmarts(smarts)
            match = self.rdmolH.GetSubstructMatches(pattern)
            if len(match) == 0:
                continue
            else:
                index = int(index)
                for m in match:
                    atom_idx = m[index]
                    at = self.rdmol.GetAtomWithIdx(atom_idx)
                    atom = at.GetSymbol()
                    hs = self.hydrogen_count(atom_idx)
                    q = at.GetFormalCharge()
                    pr = self.can_be_protonated_at(atom_idx)
                    de = self.can_be_deprotonated_at(atom_idx)
                    site = IonizableSite(atom_idx=atom_idx, 
                                        atom=atom,
                                        hs=hs,
                                        q=q,
                                        name=name,
                                        acid_base=acid_base,
                                        pr=pr,
                                        de=de)
                    exist = False
                    for _ in self.sites:
                        if _.atom_idx == site.atom_idx:
                            exist = True
                            _.acid_base += f':{site.acid_base}'
                            _.name += f':{site.name}'
                    if not exist:
                        self.sites.append(site)
        self.sites = sorted(self.sites, key=lambda x: x.atom_idx)


    def ionize(self, idx: int, mode: str) -> None:
        rwmol = Chem.RWMol(self.rdmol)
        atom = rwmol.GetAtomWithIdx(idx)
        if mode == "a2b":
            if atom.GetAtomicNum() == 1:
                atom_X = atom.GetNeighbors()[0] # only one
                charge = atom_X.GetFormalCharge() -1
                atom_X.SetFormalCharge(charge) # <-- change formal charge
                rwmol.RemoveAtom(idx) # remove the H atom
                rwmol.RemoveBond(idx, atom_X.GetIdx()) # remove the bond    
                ionized = rwmol.GetMol()         
            else:
                charge = atom.GetFormalCharge() -1
                numH = atom.GetTotalNumHs() -1
                atom.SetFormalCharge(charge) # <-- change formal charge
                atom.SetNumExplicitHs(numH) # <-- remove one H
                atom.UpdatePropertyCache() # <-- update the property cache
                ionized = Chem.AddHs(rwmol)
        
        elif mode == "b2a":
            charge = atom.GetFormalCharge() + 1
            atom.SetFormalCharge(charge) # <-- change formal charge
            numH = atom.GetNumExplicitHs() + 1
            atom.SetNumExplicitHs(numH) # <-- add one H
            ionized = Chem.AddHs(rwmol)
            # Add hydrogens, specifying onlyOnAtoms to target the desired atom
            # explicitOnly=True ensures only explicit Hs are added, not implicit ones
            # ionized = Chem.AddHs(mw, explicitOnly=True, onlyOnAtoms=[idx])

        Chem.SanitizeMol(ionized)

        rdmol = Chem.MolFromSmiles(Chem.MolToSmiles(ionized, canonical=False))
        rdmolH = Chem.AddHs(rdmol)
        smiles = Chem.CanonSmiles(Chem.MolToSmiles(Chem.RemoveHs(rdmolH)))

        self.smiles = smiles
        self.sites = []
        self.update()


    def make_protonated(self, 
                        atom_idx: int | None = None, 
                        site_idx: int | None = None) -> list[Self]:
        """Make protonated state(s) from the current state.

        All ionizable sites are considered for protonation unless `atom_idx` or `site_idx` is given.

        Args:
            atom_idx (int | None, optional): atom index. Defaults to None.
            site_idx (int | None, optional): site index. Defaults to None.

        Returns:
            list[Self]: list of protonated States.
        """
        states = []

        if self.charge == self.max_formal_charge:
            return states
        
        if isinstance(atom_idx, int):
            for site in self.sites:
                if site.pr and (site.atom_idx == atom_idx):
                    new_state = self.copy()
                    new_state.ionize(site.atom_idx, "b2a")
                    new_state.transformation = '+H'
                    new_state.origin = self.smiles
                    states.append(new_state)        
        elif isinstance(site_idx, int):
            site = self.sites[site_idx]
            if not site.pr:
                return states
            new_state = self.copy()
            new_state.ionize(site.atom_idx, "b2a")
            new_state.transformation = '+H'
            new_state.origin = self.smiles
            states.append(new_state)
        else:
            for site in self.sites:
                if not site.pr:
                    continue
                new_state = self.copy()
                new_state.ionize(site.atom_idx, "b2a")
                new_state.transformation = '+H'
                new_state.origin = self.smiles
                states.append(new_state)

        return states
    

    def make_deprotonated(self, 
                          atom_idx: int | None = None, 
                          site_idx: int | None = None) -> list[Self]:
        """Make deprotonated state(s) from the current state.

        Args:
            atom_idx (int | None, optional): atom index. Defaults to None.
            site_idx (int | None, optional): site index. Defaults to None.

        Returns:
            list[Self]: list of deprotonated States.
        """
        states = []

        if self.charge == self.min_formal_charge:
            return states
        
        if isinstance(atom_idx, int):
            for site in self.sites:
                if site.de and (site.atom_idx == atom_idx):
                    new_state = self.copy()
                    new_state.ionize(atom_idx, "a2b")
                    new_state.transformation = '-H'
                    new_state.origin = self.smiles
                    states.append(new_state)
        elif isinstance(site_idx, int):
            site = self.sites[site_idx]
            if not site.de:
                return states
            new_state = self.copy()
            new_state.ionize(site.atom_idx, "a2b")
            new_state.transformation = '-H'
            new_state.origin = self.smiles
            states.append(new_state)
        else:
            for site in self.sites:
                if not site.de:
                    continue
                new_state = self.copy()
                new_state.ionize(site.atom_idx, "a2b")
                new_state.transformation = '-H'
                new_state.origin = self.smiles
                states.append(new_state)
        return states


    def make_tautomers(self) -> list[Self]:
        if self.tautomer_rule is None:
            return []
        elif self.tautomer_rule == "rdkit":
            t = RdkTautomers(self.smiles).enumerate()
        elif self.tautomer_rule == "comprehensive":
            t = ComprehensiveTautomers(self.smiles).enumerate()
        else:
            return []
        
        states = []
        for smiles in t.enumerated:
            try:
                assert smiles != self.smiles
                rdmol = Chem.MolFromSmiles(smiles)
                assert rdmol is not None
                charge = Chem.GetFormalCharge(rdmol)
                assert charge == self.charge
                states.append(State(smiles=smiles,
                                    origin=self.smiles,
                                    transformation='Tautomer'))
            except:
                continue
        return states
    


class StateEnsemble:
    def __init__(self, states: list[State] = [], transformation: str | None = None) -> None:
        self.states = states
        self.maxiter = 10
        if transformation:
            for state in self.states:
                state.transformation = transformation

    def __iter__(self) -> Iterator:
        return iter(self.states)

    def __next__(self) -> State:
        return next(self.states)
    
    def __getitem__(self, index: int | slice) -> State | Self:
        """Operator `[]`"""
        assert self.size() != 0, "StateEnsemble is empty"
        if isinstance(index, slice):
            return StateEnsemble(self.states[index])
        else:
            return self.states[index]

    def __setitem__(self, index: int, state: State) -> Self:
        """Set item."""
        self.states[index] = state
        return self


    def __add__(self, other: State | Self) -> Self:
        """Operator `+`."""
        assert isinstance(other, State | StateEnsemble), "'+' operator expects State or StateEnsemble object"
        new_object = self.copy()
        if isinstance(other, State):
            new_object.states.append(other)
        elif isinstance(other, StateEnsemble):
            new_object.states.extend(other.states)
        return new_object
    

    def __iadd__(self, other: State | Self) -> Self:
        """Operator `+=`."""
        assert isinstance(other, State | StateEnsemble), "'+=' operator expects State or StateEnsemble object"
        if isinstance(other, State):
            self.states.append(other)
        elif isinstance(other, StateEnsemble):
            self.states.extend(other.states)
        return self
    

    def size(self) -> int:
        return len(self.states)
    

    def drop(self) -> Self:
        """Drop duplicate and unreasonable states."""
        U = []
        mask = []
        for state in self.states:
            if state.rdmol is None:
                mask.append(False)
                continue
            if state.smiles in U:
                mask.append(False)
                continue
            reasonable = True
            for pattern in UnreasonablePatterns:
                if len(state.rdmol.GetSubstructMatches(pattern)) > 0:
                    reasonable = False
                    break
            if not reasonable:
                mask.append(False)
                continue
            mask.append(True)
            U.append(state.smiles)  
        self.states = list(itertools.compress(self.states, mask))
        return self
    

    def show(self) -> None:
        for state in self.states:
            state.info()
        

class StateNetwork:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.visited_states = []
        self.initial_state = None
    

    def generate_neighbors(self, state: State) -> StateEnsemble:
        """Generate all possible neighboring microstates."""
        neighbors = StateEnsemble()
        if state == self.initial_state and isinstance(state.tautomer_rule, str):
            neighbors += StateEnsemble(state.make_tautomers())
        neighbors += StateEnsemble(state.make_protonated())
        neighbors += StateEnsemble(state.make_deprotonated())
        neighbors = neighbors.drop()
        
        return neighbors


    def mcs_index_map(self, other: State) -> dict[int, int]:
        """Generate a MCS-based atom indices map.

        Uses the self.initial_state as reference in mapping `other` State.

        Args:
            other (State): to be mapped state.

        Returns:
            dict: {ref atom index: other atom index, ...}
        """
        mcs = Chem.rdFMCS.FindMCS([self.initial_state.rdmol, other.rdmol], 
                            atomCompare=Chem.rdFMCS.AtomCompare.CompareAny, 
                            bondCompare=Chem.rdFMCS.BondCompare.CompareAny, 
                            completeRingsOnly=True)
        mcs_rdmol = Chem.MolFromSmarts(mcs.smartsString)
        match_1 = self.initial_state.rdmol.GetSubstructMatch(mcs_rdmol)
        match_2 = other.rdmol.GetSubstructMatch(mcs_rdmol)
        return {match_2[i]: match_1[i] for i in range(len(match_1))}


    def build(self, 
              smiles: str,
              origin: str | None = None, 
              transformation: str | None = None,
              min_formal_charge: int = -2,
              max_formal_charge: int = +2,
              min_atomic_charge: int = -1,
              max_atomic_charge: int = +1,
              protomer_rule: str = 'default',
              tautomer_rule: str | None = None,
              verbose: bool = False) -> None:
        """Build the microstate network using BFS from initial state.""" 
        self.initial_state = State(smiles=smiles,
                              protomer_rule=protomer_rule,
                              tautomer_rule=tautomer_rule,
                              min_formal_charge=min_formal_charge,
                              max_formal_charge=max_formal_charge,
                              min_atomic_charge=min_atomic_charge,
                              max_atomic_charge=max_atomic_charge)
        self.initial_state
        # Initialize BFS
        queue = deque([self.initial_state])
        self.visited_states.append(self.initial_state)
        self.graph.add_node(self.initial_state.smiles, 
                            initial=True, 
                            sites=self.initial_state.site_info())
        iter = 0

        while queue:
            iter += 1
            current_state = queue.popleft()
            neighbors = self.generate_neighbors(current_state)
            for neighbor_state in neighbors:
                if neighbor_state.transformation == 'Tautomer' and current_state.charge != neighbor_state.charge:
                    continue
                self.graph.add_edge(current_state.smiles, 
                                    neighbor_state.smiles, 
                                    transformation=neighbor_state.transformation)
                if neighbor_state not in self.visited_states:
                    self.visited_states.append(neighbor_state)
                    imap = self.mcs_index_map(neighbor_state)
                    sites = [(a, imap[i], q, pr, de) for (a, i, q, pr, de) in neighbor_state.site_info()]
                    self.graph.add_node(neighbor_state.smiles, 
                                        initial=False, 
                                        sites=sites)
                    queue.append(neighbor_state)
            if verbose:
                print(f"Iteration {iter:2}: {len(self.visited_states):2} microstates found")
        
        if verbose:
            print(f"\nNetwork construction complete!")
            print(f"Total microstates: {len(self.graph.nodes())}")
            print(f"Total transformations: {len(self.graph.edges())}")


    def micro_pKa(self, PE: list[float], beta: float=1.0) -> dict[int,list[float]]:
        pKa = defaultdict(list)
        for site in self.initial_state.sites:
            group = defaultdict(list)
            for k, st in enumerate(self.visited_states):
                for (a, i, q, pr, de) in st.site_info():
                    # ex. [('N', 5, 0, True, True), ...]
                    if i == site.atom_idx:
                        group[q].append(PE[k])
            weighted_mean = {q: Boltzmann_weighted_average(_, beta=beta) for q, _ in sorted(group.items())}
            charges = list(sorted(weighted_mean)) # ex. [-1, 0, +1]
            for (q1, q2) in list(itertools.pairwise(charges)): # ex. [(-1, 0), (0, +1)]
                G_deprotonated = weighted_mean[q1]
                G_protonated = weighted_mean[q2]
                delta_G_deprotonation = G_deprotonated - G_protonated
                pKa[site.atom_idx].append(delta_G_deprotonation)
        
        ordered_pKa = {}
        for k, v in pKa.items():
            ordered_pKa[k] = sorted(v)

        return ordered_pKa
            

    def macro_pKa(self, PE: list[float], beta: float=1.0) -> list[float]:
        pKa = []
        for site in self.initial_state.sites:
            group = defaultdict(list)
            for k, st in enumerate(self.visited_states):
                for (a, i, q, pr, de) in st.site_info():
                    # ex. [('N', 5, 0, True, True), ...]
                    group[q].append(PE[k])
        weighted_mean = {q: Boltzmann_weighted_average(_, beta=beta) for q, _ in sorted(group.items())}
        charges = list(sorted(weighted_mean)) # ex. [-1, 0, +1]
        for (q1, q2) in list(itertools.pairwise(charges)): # ex. [(-1, 0), (0, +1)]
            G_deprotonated = weighted_mean[q1]
            G_protonated = weighted_mean[q2]
            delta_G_deprotonation = G_deprotonated - G_protonated
            pKa.append(delta_G_deprotonation)
        
        return sorted(pKa)

    
    def population(self, PE: list[float], pH: float, C: float, kT: float = 1.0) -> list[float]:
        reference_PE = None
        dG = []
        for k, st in enumerate(self.visited_states):
            if st == self.initial_state:
                reference_PE = PE[k]
        for k, st in enumerate(self.visited_states):
            delta_G = PE[k] - reference_PE
            delta_m = st.charge - self.initial_state.charge
            dG.append(delta_G + delta_m * C * pH)
        dG = np.array(dG)
        Boltzmann_factors = np.exp(-dG/kT)
        Z = np.sum(Boltzmann_factors)
        
        return Boltzmann_factors/Z


class DeprecatedIonizedStates:
    """Knowledge-based enumeration of (de)protonated states"""

    smarts_path = importlib.resources.files('rdworks.predefined.ionized')
    ionization_patterns = pd.read_csv(smarts_path / 'simple_smarts_pattern.csv')
    
    # Unreasonable chemical structures
    unreasonable_patterns = [
        Chem.MolFromSmarts(s) for s in [
            "[#6X5]",
            "[#7X5]",
            "[#8X4]",
            "[*r]=[*r]=[*r]",
            "[#1]-[*+1]~[*-1]",
            "[#1]-[*+1]=,:[*]-,:[*-1]",
            "[#1]-[*+1]-,:[*]=,:[*-1]",
            "[*+2]",
            "[*-2]",
            "[#1]-[#8+1].[#8-1,#7-1,#6-1]",
            "[#1]-[#7+1,#8+1].[#7-1,#6-1]",
            "[#1]-[#8+1].[#8-1,#6-1]",
            "[#1]-[#7+1].[#8-1]-[C](-[C,#1])(-[C,#1])",
            # "[#6;!$([#6]-,:[*]=,:[*]);!$([#6]-,:[#7,#8,#16])]=[C](-[O,N,S]-[#1])",
            # "[#6]-,=[C](-[O,N,S])(-[O,N,S]-[#1])",
            "[OX1]=[C]-[OH2+1]",
            "[NX1,NX2H1,NX3H2]=[C]-[O]-[H]",
            "[#6-1]=[*]-[*]",
            "[cX2-1]",
            "[N+1](=O)-[O]-[H]",
        ]]


    def __init__(self, smiles: str, charge_min: int = -2, charge_max: int = 2):
        self.smiles = Chem.CanonSmiles(smiles)
        self.charge_max = charge_max
        self.charge_min = charge_min

        self.rdmol = Chem.MolFromSmiles(self.smiles)
        self.rdmol_H = Chem.AddHs(self.rdmol)
        self.charge = Chem.GetFormalCharge(self.rdmol_H)
        
        # initial states
        self.states = {self.smiles : (self.rdmol_H, self.charge)}
        
        # initial ionization sites
        self.sites = {self.smiles: self.set_ionization_sites(self.smiles)}

        # pKa pairs: 
        # HA(acid) + H2O == A-(base) + H3O+ or HA+(acid) + H2O == A(base) + H3O+
        self.pairs = []

        # iteratively build an ensemble of ionized states
        self.ensemble()


    
    @staticmethod
    def set_ionization_sites(smiles: str) -> tuple:
        subject = Chem.MolFromSmiles(smiles)
        subject = Chem.AddHs(subject)
        charge = Chem.GetFormalCharge(subject)        
        indices = [] # atom indices of protonation/deprotonation site(s)
        for i, name, smarts, smarts_index, acid_or_base in IonizedStates.ionization_patterns.itertuples():
            pattern = Chem.MolFromSmarts(smarts)
            matches = subject.GetSubstructMatches(pattern)
            # returns a list of tuples, where each tuple contains the indices 
            # of the atoms in the molecule that match the substructure query
            # ex. ((1,), (2,), (3,))
            if len(matches) > 0:
                smarts_index = int(smarts_index)
                indices += [(match[smarts_index], acid_or_base) for match in matches]
        
        return (list(set(indices)), subject, charge)
    

    @staticmethod
    def clean_smiles(rdmol: Chem.Mol) -> str:
        Chem.SanitizeMol(rdmol)
        rdmol = Chem.MolFromSmiles(Chem.MolToSmiles(rdmol))
        rdmol_H = Chem.AddHs(rdmol)
        rdmol = Chem.RemoveHs(rdmol_H)
        return Chem.CanonSmiles(Chem.MolToSmiles(rdmol))


    @staticmethod
    def reasonable(romol: Chem.Mol) -> bool:
        return all([len(romol.GetSubstructMatches(p)) == 0 for p in IonizedStates.unreasonable_patterns])
    

    def ionize(self, smiles: str | None = None) -> int:
        num_added_states = 0
        
        if smiles is None:
            smiles = self.smiles

        if smiles not in self.sites:
            self.sites[smiles] = self.set_ionization_sites(smiles)
        
        (indices, subject, charge) = self.sites[smiles]
        
        if (charge >= self.charge_max) or (charge <= self.charge_min):
            # formal charge will be increased or decreased by protonation/deprotonation
            # so, if the charge of current state is already max or min
            # there is nothing to do
            return num_added_states
            
        for (i, acid_or_base) in indices:
            edmol = Chem.RWMol(subject) # edmol preserves Hs
            if acid_or_base == 'A': # de-protonate
                A = edmol.GetAtomWithIdx(i)
                if A.GetAtomicNum() == 1:
                    X = A.GetNeighbors()[0] # there must be only one neighbor
                    charge = X.GetFormalCharge() - 1
                    X.SetFormalCharge(charge)
                    edmol.RemoveAtom(i)
                else:
                    bonded_H_indices = [ H.GetIdx() for H in A.GetNeighbors() if H.GetAtomicNum() == 1 ]
                    nH = len(bonded_H_indices)
                    assert nH > 0, f"Cannot deprotonate an atom (idx={i}; no H)"
                    charge = A.GetFormalCharge() - 1
                    A.SetFormalCharge(charge)
                    edmol.RemoveAtom(bonded_H_indices[0])
            
            elif acid_or_base == 'B': # protonate
                # note that protonation at tertiary nitrogen may results in stereoisomers
                # current implementation ignores the stereochemistry
                # use rdworks.complete_stereoisomers() function to complete the stereoisomers
                B = edmol.GetAtomWithIdx(i)
                assert B.GetAtomicNum() > 1, f"Cannot protonate an atom (idx={i}; {B.GetAtomicNum()})"
                charge = B.GetFormalCharge() + 1
                B.SetFormalCharge(charge)
                nH = B.GetNumExplicitHs()
                B.SetNumExplicitHs(nH+1)
                edmol = Chem.AddHs(edmol)
            
            # clean up and save SMILES
            ionized_smiles = IonizedStates.clean_smiles(edmol)
            ionized_mol = Chem.MolFromSmiles(ionized_smiles)
            ionized_mol = Chem.AddHs(ionized_mol)
            ionized_charge = Chem.GetFormalCharge(ionized_mol)
            if self.reasonable(ionized_mol):
                if ionized_smiles in self.states:
                    continue
                self.states[ionized_smiles] = (ionized_mol, ionized_charge)
                num_added_states += 1
            
                # store acid-base pair information for pKa
                if acid_or_base == 'A':
                    self.pairs.append((i, smiles, ionized_smiles))
                elif acid_or_base == 'B':
                    self.pairs.append((i, ionized_smiles, smiles))

        return num_added_states
    
    
    def ensemble(self) -> None:
        # populate initial states
        self.ionize()

        # propagate
        num_added_states = None       
        while num_added_states is None or num_added_states > 0:
            states = self.states.copy() # dictionary
            # self.ionize(smiles) below will change self.states
            # so we cannot iterate self.states. Instead we will
            # iterate over a copy of the self.states
            for smiles in states:
                num_added_states = self.ionize(smiles) 
                
    
    def count(self) -> int:
        return len(self.states)


    def get_sites(self) -> dict:
        return self.sites
    
    
    def get_smiles(self) -> list[str]:
        return [smiles for smiles in self.states]
    

    def get_rdmol(self) -> list[Chem.Mol]:
        return [romol for smiles, (romol, charge) in self.states.items()]
    

    def get_pairs(self) -> list:
        return self.pairs
    


class QupkakeMicrostates():

    def __init__(self, origin: Mol, calculator: str = 'xTB'):
        self.origin = origin
        self.calculator = calculator
        self.basic_sites = []
        self.acidic_sites = []
        self.states = []
        self.mols = []
        self.reference = None
    

    def enumerate(self) -> None:
        # Qu pKake results must be stored at .confs
        for conf in self.origin:
            pka = conf.props.get('pka', None)
            if pka is None:
                # no protonation/deprotonation sites
                continue
            if isinstance(pka, str) and pka.startswith('tensor'):
                # ex. 'tensor(9.5784)'
                pka = float(pka.replace('tensor(','').replace(')',''))
            if conf.props.get('pka_type') == 'basic':
                self.basic_sites.append(conf.props.get('idx'))
            elif conf.props.get('pka_type') == 'acidic':
                self.acidic_sites.append(conf.props.get('idx'))

        # enumerate protonation/deprotonation sites to generate microstates

        np = len(self.basic_sites)
        nd = len(self.acidic_sites)
        P = [c for n in range(np+1) for c in itertools.combinations(self.basic_sites, n)]
        D = [c for n in range(nd+1) for c in itertools.combinations(self.acidic_sites, n)]
        
        PD = list(itertools.product(P, D))
        
        for (p, d) in PD:
            conf = self.origin.confs[0].copy()
            conf = conf.protonate(p).deprotonate(d).optimize(calculator=self.calculator)
            charge = len(p) - len(d)
            self.states.append(SimpleNamespace(
                charge=charge, 
                protonation_sites=p, 
                deprotonation_sites=d,
                conf=conf,
                smiles=Mol(conf).smiles,
                delta_m=None,
                PE=None))
            
        # sort microstates by ascending charges
        self.states = sorted(self.states, key=lambda x: x.charge)


    @staticmethod
    def Boltzmann_weighted_average(potential_energies: list) -> float:
        """Calculate Boltzmann weighted average potential energy at pH 0.

        Args:
            potential_energies (list): a list of potential energies.

        Returns:
            float: Boltzmann weighted average potential energy.
        """
        pe_array = np.array(potential_energies)
        pe = pe_array - min(potential_energies)
        Boltzmann_factors = np.exp(-pe/kT)
        Z = np.sum(Boltzmann_factors)
        p = Boltzmann_factors/Z

        return float(np.dot(p, pe_array))


    def populate(self) -> None:
        for microstate in self.states:
            mol = Mol(microstate.conf).make_confs(n=4).optimize_confs()
            # mol = mol.drop_confs(similar=True, similar_rmsd=0.3, verbose=True)
            # mol = mol.optimize_confs(calculator=calculator)
            # mol = mol.drop_confs(k=10, window=15.0, verbose=True)
            PE = []
            for conf in mol.confs:
                conf = conf.optimize(calculator=self.calculator, verbose=True)
                # GFN2xTB requires 3D coordinates
                # xtb = GFN2xTB(conf.rdmol).singlepoint(water='cpcmx', verbose=True)
                PE.append(conf.potential_energy(calculator=self.calculator))
                # xtb = GFN2xTB(conf.rdmol).singlepoint(verbose=True)
                # SimpleNamespace(
                #             PE = datadict['total energy'] * hartree2kcalpermol,
                #             Gsolv = Gsolv,
                #             charges = datadict['partial charges'],
                #             wbo = Wiberg_bond_orders,
                #             )
            microstate.PE = self.Boltzmann_weighted_average(PE)
            logger.info(f"PE= {PE}")
            logger.info(f"Boltzmann weighted= {microstate.PE}")            
            self.mols.append(mol)

    def get_populations(self, pH: float) -> list[tuple]:
        # set the lowest dG as the reference
        self.reference = self.states[np.argmin([microstate.PE for microstate in self.states])]
        for microstate in self.states:
            microstate.delta_m = microstate.charge - self.reference.charge
        dG = []
        for microstate in self.states:
            dG.append((microstate.PE - self.reference.PE) + microstate.delta_m * C * pH)
        dG = np.array(dG)

        logger.info(f"dG= {dG}")
        Boltzmann_factors = np.exp(-dG/kT)
        Z = np.sum(Boltzmann_factors)
        p = Boltzmann_factors/Z
        idx_p = sorted(list(enumerate(p)), key=lambda x: x[1], reverse=True)
        # [(0, p0), (1, p1), ...]

        return idx_p

    def get_ensemble(self) -> list[Mol]:
        return self.mols

    def get_mol(self, idx: int) -> Mol:
        return self.mols[idx]
    
    def count(self) -> int:
        return len(self.states)