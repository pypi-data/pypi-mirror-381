from multiprocessing.spawn import prepare
from rdworks import State, StateEnsemble, StateNetwork
import pytest


@pytest.fixture
def prepared_state():
    smiles = 'c1ccc(CNc2ncnc3ccccc23)cc1'
    st = State(smiles=smiles)
    return st


def test_site(prepared_state):
    """Ionizable site"""
    st = prepared_state
    assert st.site_info() == [
        ('N', 5, 0, True, True),
        ('N', 7, 0, True, False), 
        ('N', 9, 0, True, False), 
        ]
    # SMILES: c1ccc(CNc2ncnc3ccccc23)cc1
    # Formal charge: 0
    # Origin: None
    # Transformation: None
    # Ionizable sites:
    # - atom_idx=  5, atom=  N, q= +0, hs= 1, pr= 1, de= 1, acid_base= B:A:A, name= Amine:Amide:Amide vinylogue
    # - atom_idx=  7, atom=  N, q= +0, hs= 0, pr= 1, de= 0, acid_base= B, name= Aza-aromatics
    # - atom_idx=  9, atom=  N, q= +0, hs= 0, pr= 1, de= 0, acid_base= B, name= Aza-aromatics
    
    smiles = 'C1=Nc2ccccc2C(N=Cc2ccccc2)N1'
    st = State(smiles=smiles)
    assert st.site_info() == [
        ('N', 1, 0, True, False), 
        ('N', 9, 0, True, False), 
        ('N', 17, 0, True, True)]
    # SMILES: C1=Nc2ccccc2C(N=Cc2ccccc2)N1
    # Formal charge: 0
    # Origin: None
    # Transformation: None
    # Ionizable sites:
    # - atom_idx=  1, atom=  N, q= +0, hs= 0, pr= 1, de= 0, acid_base= B, name= Imine
    # - atom_idx=  9, atom=  N, q= +0, hs= 0, pr= 1, de= 0, acid_base= B, name= Imine
    # - atom_idx= 17, atom=  N, q= +0, hs= 1, pr= 1, de= 1, acid_base= A, name= Amide


def test_tautomers():
    smiles = 'c1ccc(CNc2ncnc3ccccc23)cc1'
    st1 = State(smiles=smiles, tautomerize_rule='rdkit')
    se1 = StateEnsemble(st1.make_tautomers())
    assert se1.size() == 2
    st2 = State(smiles=smiles, tautomerize_rule='comprehensive')
    se2 = StateEnsemble(st2.make_tautomers()) 
    assert se2.size() == 20


def test_protonate(prepared_state):
    st = prepared_state
    ps = st.make_protonated(atom_idx=9)
    assert len(ps) == 1
    assert ps[0].site_info() == [
        ('N', 5, 0, True, True),
        ('N', 7, 0, True, False), 
        ('N', 9, 1, False, True),
        ]
    # SMILES: c1ccc(CNc2nc[nH+]c3ccccc23)cc1
    # Formal charge: 1
    # Origin: c1ccc(CNc2ncnc3ccccc23)cc1
    # Transformation: +H
    # Ionizable sites:
    # - atom_idx=  5, atom=  N, q= +0, hs= 1, pr= 1, de= 1, acid_base= B:A:A, name= Amine:Amide:Amide vinylogue
    # - atom_idx=  7, atom=  N, q= +0, hs= 0, pr= 1, de= 0, acid_base= B, name= Aza-aromatics
    # - atom_idx=  9, atom=  N, q= +1, hs= 1, pr= 0, de= 1, acid_base= A, name= Aza-aromatics

    ps = st.make_protonated(site_idx=2)
    assert len(ps) == 1
    assert ps[0].site_info() == [
        ('N', 5, 0, True, True),
        ('N', 7, 0, True, False), 
        ('N', 9, 1, False, True),
        ]

    se = StateEnsemble(st.make_protonated())
    assert se.size() == 3
    results = [_.smiles for _ in se]
    expected = ['c1ccc(C[NH2+]c2ncnc3ccccc23)cc1',
                'c1ccc(CNc2[nH+]cnc3ccccc23)cc1',
                'c1ccc(CNc2nc[nH+]c3ccccc23)cc1'
                ]
    assert set(results) == set(expected)



def test_deprotonate(prepared_state):
    st = prepared_state
    des = st.make_deprotonated(atom_idx=5)
    assert len(des) == 1
    assert des[0].site_info() == [
        ('N', 5, -1, True, False),
        ('N', 7, 0, True, False), 
        ('N', 9, 0, True, False),
    ]

    des = st.make_deprotonated(site_idx=0)
    assert len(des) == 1
    assert des[0].site_info() == [
        ('N', 5, -1, True, False),
        ('N', 7, 0, True, False), 
        ('N', 9, 0, True, False),
    ]

    des = st.make_deprotonated(atom_idx=7)
    assert len(des) == 0

    se = StateEnsemble(st.make_deprotonated())
    assert se.size() == 1
    results = [_.smiles for _ in se]
    expected = ['c1ccc(C[N-]c2ncnc3ccccc23)cc1']
    assert set(results) == set(expected)


def test_statenetwork():
    sn = StateNetwork()
    smiles = 'O=C(NCCCC)[C@H](CCC1)N1[C@@H](CC)C2=NN=C(CC3=CC=C(C)C=C3)O2'
    G = sn.build(smiles=smiles, verbose=True)


# def test_ionizedstate():    
#     smiles = 'O=C(NCCCC)[C@H](CCC1)N1[C@@H](CC)C2=NN=C(CC3=CC=C(C)C=C3)O2'
#     x = IonizedStates(smiles)

#     assert x.count() == 7
    
#     d = x.get_sites()
#     print('sites:')
#     for k, v in d.items():
#         print(k, v)
#     print()

#     p = x.get_pairs()
#     print('pairs:')
#     for k in p:
#         print(k)
#     print()

#     indices = d['CCCCNC(=O)[C@@H]1CCCN1[C@@H](CC)c1nnc(Cc2ccc(C)cc2)o1'][0]
    
#     assert (11, 'B') in indices
#     assert (16, 'B') in indices
#     assert (17, 'B') in indices

#     expected = ['CCCCNC(=O)[C@@H]1CCCN1[C@@H](CC)c1nnc(Cc2ccc(C)cc2)o1', 
#                 'CCCCNC(=O)[C@@H]1CCCN1[C@@H](CC)c1[nH+]nc(Cc2ccc(C)cc2)o1', 
#                 'CCCCNC(=O)[C@@H]1CCC[NH+]1[C@@H](CC)c1nnc(Cc2ccc(C)cc2)o1', 
#                 'CCCCNC(=O)[C@@H]1CCCN1[C@@H](CC)c1n[nH+]c(Cc2ccc(C)cc2)o1', 
#                 'CCCCNC(=O)[C@@H]1CCC[NH+]1[C@@H](CC)c1[nH+]nc(Cc2ccc(C)cc2)o1', 
#                 'CCCCNC(=O)[C@@H]1CCCN1[C@@H](CC)c1[nH+][nH+]c(Cc2ccc(C)cc2)o1', 
#                 'CCCCNC(=O)[C@@H]1CCC[NH+]1[C@@H](CC)c1n[nH+]c(Cc2ccc(C)cc2)o1']
#     results = x.get_smiles()
#     assert set(expected).intersection(set(results)) == set(expected)


# def test_gypsum_dl():
#     import gypsum_dl
#     smiles = 'O=C(NCCCC)[C@H](CCC1)N1[C@@H](CC)C2=NN=C(CC3=CC=C(C)C=C3)O2'
#     state_smiles = list(
#         gypsum_dl.GypsumDL(smiles,
#             min_ph=6.4,
#             max_ph=8.4,
#             pka_precision=1.0,
#             thoroughness=3,
#             max_variants_per_compound=5,
#             second_embed=False,
#             skip_optimize_geometry=False,
#             skip_alternate_ring_conformations=False,
#             skip_adding_hydrogen=False,
#             skip_making_tautomers=False,
#             skip_enumerate_chiral_mol=False,
#             skip_enumerate_double_bonds=False,
#             let_tautomers_change_chirality=False,
#             use_durrant_lab_filters=True,
#             job_manager='serial',
#             num_processors=1,
#             ))
#     for smi in state_smiles:
#         print(smi)
    
if __name__ == '__main__':
    test_ionizedstate()
    # test_gypsum_dl()