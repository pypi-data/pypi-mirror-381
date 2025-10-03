from rdworks import State, StateEnsemble, StateNetwork
import numpy as np
import math
import pytest


@pytest.fixture(scope='module') # Runs once for every test module (file).
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
    st1 = State(smiles=smiles, tautomer_rule='rdkit')
    se1 = StateEnsemble(st1.make_tautomers())
    assert se1.size() == 2
    st2 = State(smiles=smiles, tautomer_rule='comprehensive')
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


# def test_sn():
#     smiles = 'c1ccc(CNc2ncnc3ccccc23)cc1'
#     sn1 = StateNetwork()
#     sn1.build(smiles=smiles, tautomer_rule=None)
#     assert len(sn1.visited_states) == 11
#     assert len(sn1.graph.nodes()) == 11
#     sn2 = StateNetwork()
#     sn2.build(smiles=smiles, tautomer_rule='rdkit')
#     assert len(sn2.visited_states) == 33
#     assert len(sn2.graph.nodes()) == 33
#     sn3 = StateNetwork()
#     sn3.build(smiles=smiles, tautomer_rule='comprehensive')
#     assert len(sn3.visited_states) == 183
#     assert len(sn3.graph.nodes()) == 183
    

def test_pka_pop():
    smiles = 'c1ccc(CNc2ncnc3ccccc23)cc1'
    sn = StateNetwork()
    sn.build(smiles=smiles, max_formal_charge=3, tautomer_rule=None)
    assert len(sn.visited_states) == 12
    assert len(sn.graph.nodes()) == 12

    # calculated from Uni-pKa
    LN10 = math.log(10)
    TRANSLATE_PH = 6.504894871171601
    # Uni-pka model specific variable for pH dependent deltaG
    # Free energy might be obtained at pH 6.504...
    PE = [-6.025253772735596, -2.9201512336730957, -2.7405877113342285, 
          -2.9639060497283936, 7.656927108764648, 19.67357063293457, 
          21.269811630249023, 11.911577224731445, 7.5623698234558105, 
          10.144123077392578, 21.36874008178711, 12.132856369018555]
    
    micro = sn.micro_pKa(PE, beta=1.0)
    macro = sn.macro_pKa(PE, beta=1.0)
    pop74 = sn.population(PE, pH=(7.4-TRANSLATE_PH), C=LN10, kT=1.0)
    pop12 = sn.population(PE, pH=(1.2-TRANSLATE_PH), C=LN10, kT=1.0)

    micro_pKa = {}
    for k, v in micro.items():
        micro_pKa[k] = (np.array(v)/LN10 + TRANSLATE_PH).tolist()
    
    expected_micro_pKa = {
        5: [5.263056256779453, 12.37074708270436], 
        7: [5.190629233663213], 
        9: [5.280577863433882],
        }
    
    assert micro_pKa.keys() == expected_micro_pKa.keys()
    for k,v in micro_pKa.items():
        for x, y in zip(v, expected_micro_pKa[k]):
            assert math.isclose(x, y)

    expected_macro_pKa = [5.248700101444452, 12.3693201962264]

    macro_pKa = (np.array(macro)/LN10 + TRANSLATE_PH).tolist()
    for x, y in zip(macro_pKa, expected_macro_pKa):
        assert math.isclose(x, y)

    expected_pop74 = [
        9.83819164e-01, 5.61411430e-03, 4.69134966e-03, 5.86521215e-03,
        8.82926902e-06, 1.10115230e-13, 2.23156084e-14, 2.58724940e-10,
        1.23562113e-06, 9.34639510e-08, 2.57359096e-15, 1.62870756e-09]
    
    expected_pop12 = [
        2.69350204e-05, 2.43603364e-01, 2.03563465e-01, 2.54498810e-01,
        1.52519994e-16, 7.57267677e-06, 1.53465501e-06, 1.77926373e-02,
        3.38288596e-11, 2.55885788e-12, 2.80505611e-01, 7.06716357e-08]
    
    for x, y in zip(pop74, expected_pop74):
        assert math.isclose(x, y, abs_tol=1e-6)
    
    for x, y in zip(pop12, expected_pop12):
        assert math.isclose(x, y, abs_tol=1e-6)

    print()
    for k, st in enumerate(sn.visited_states):
        print(f"{k:2} {st.smiles:50} {PE[k]:8.3f} {pop12[k]:8.3g} {pop74[k]:8.3g}")