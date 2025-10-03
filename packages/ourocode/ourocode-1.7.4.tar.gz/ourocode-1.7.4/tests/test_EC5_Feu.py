#! env\Scripts\python.exe
# Encoding in UTF-8 by Anthony PARISOT
# pytest --cov=. --cov-report html
import sys
import pytest
import forallpeople as si

si.environment("structural")
sys.path.insert(1, "./")
from ourocode.eurocode import EC5_Element_droit as EC5
from ourocode.eurocode import EC5_Feu as EC5_feu


@pytest.fixture
def barre():
    return EC5.Barre(
        b=100,
        h=300,
        section="Rectangulaire",
        classe="GL24h",
        cs=2,
        effet_systeme="True",
    )


@pytest.fixture
def feu(barre):
    return EC5_feu.Feu._from_parent_class(
        barre,
        t_expo=30,
        haut="Pas d'exposition",
        bas="1 plaque de platre type F joints vides",
        gauche="1 plaque de platre type A joints comblés",
        droite="Aucune protection",
        double_couches=False,
        hp=12,
        rho_k_protect=0,
        tf=15,
    )


def test_feu_initialisation(feu):
    assert feu.t_expo == 30
    assert feu.haut == "Pas d'exposition"
    assert feu.bas == "1 plaque de platre type F joints vides"
    assert feu.gauche == "1 plaque de platre type A joints comblés"
    assert feu.droite == "Aucune protection"
    assert feu.hp == 12 * si.mm
    assert feu.rho_k_protect == 0
    assert feu.tf == 15


def test_feu_get_section_reduction(feu):
    assert feu.b_calcul.value == 0.05044
    assert feu.h_calcul.value == 0.26958528


@pytest.fixture
def traction(feu):
    traction = EC5_feu.Traction_feu._from_parent_class(feu)
    traction.sigma_t_0_d(20)
    traction.f_t_0_d()
    traction.taux_t_0_d()
    return traction


@pytest.fixture
def compression(feu):
    compression = EC5_feu.Compression_feu._from_parent_class(
        feu, lo_y=7000, lo_z=7000, type_appuis="Rotule - Rotule"
    )
    compression.sigma_c_0_d(50)
    compression.f_c_0_d()
    compression.taux_c_0_d()
    return compression


@pytest.fixture
def flexion(feu):
    flexion = EC5_feu.Flexion_feu._from_parent_class(
        feu, lo_rel_y=7000, lo_rel_z=3500, coeflef_y=0.9, coeflef_z=0.8, pos="Charge sur fibre tendue"
    )
    flexion.sigma_m_d(100, 50)
    flexion.f_m_d()
    flexion.taux_m_d()
    return flexion


class Test_Flexion(object):
    @pytest.fixture(autouse=True)
    def setup_method(self, flexion, compression, traction):
        self.flexion = flexion
        self.flexion.taux_m_d(traction=traction, compression=compression)

    def test_init(self):
        assert self.flexion.lo_rel_y == 7 * si.m
        assert self.flexion.lo_rel_z == 3.5 * si.m
        assert self.flexion.coeflef_y == 0.9
        assert self.flexion.coeflef_z == 0.8
        assert self.flexion.pos == "Charge sur fibre tendue"

    def test_Kh(self):
        assert self.flexion.K_h == {"y": 1.0717734625362931, "z": 1.1}

    def test_sigma_m_d(self):
        assert self.flexion.sigma_m_rd["y"].value == 163675555.10053056
        assert self.flexion.sigma_m_rd["z"].value == 437396117.6737902

    def test_f_m_d(self):
        assert self.flexion.f_type_rd == 30.360 * si.MPa

    def test_taux_m_d(self):
        # print(self.flexion.taux_m_rd)
        assert self.flexion.taux_m_rd == {
            "equ6.11": 14.260362922063692,
            "equ6.12": 16.680502659534092,
            "equ6.19": 14.201857224168222,
            "equ6.20": 16.621996961638622,
            "equ6.33y": 10.532177484564267,
            "equ6.33z": 13.097260680135049,
            "equ6.35yzy": 176.85536603459653,
            "equ6.35yzz": 189.9370741374112,
            "equ6.35zyy": 38.68645109817827,
            "equ6.35zyz": 131.89068257593286,
        }


class Test_Traction:
    @pytest.fixture(autouse=True)
    def setup_method(self, traction):
        self.traction = traction

    def test_f_t_0_d(self):
        assert self.traction.f_type_rd == 22.080 * si.MPa

    def test_sigma_t_0_d(self):
        assert self.traction.sigma_t_0_rd.value == 1470817.3450310654

    def test_taux_t_0_d(self):
        assert self.traction.taux_t_0_rd == {"equ6.1": 0.062152224068775346}


class Test_Compression:
    @pytest.fixture(autouse=True)
    def setup_method(self, compression, flexion):
        self.compression = compression
        compression.taux_c_0_d(flexion)

    def test_f_c_0_d(self):
        assert self.compression.f_type_rd == 27.600 * si.MPa

    def test_sigma_c_0_d(self):
        assert self.compression.sigma_c_0_rd.value == 1666666.6666666667

    def test_taux_c_0_d(self):
        # print(self.compression.taux_c_0_rd)
        assert self.compression.taux_c_0_rd == {
            "equ6.23": 14.485211187279445,
            "equ6.24": 24.485009764900642,
            "equ6.2": 0.0603864734299517,
        }


class Test_Cisaillement:
    @pytest.fixture(autouse=True)
    def setup_method(self, feu):
        self.cisaillement = EC5_feu.Cisaillement_feu._from_parent_class(feu)
        self.cisaillement.Kv(200, 40, 0, ent="Dessous")
        self.cisaillement.tau_d(50)
        self.cisaillement.f_v_d()
        self.cisaillement.taux_tau_d()

    def test_Kv(self):
        assert self.cisaillement.K_v == 0.6460641104990499

    def test_f_v_d(self):
        assert self.cisaillement.f_type_rd == 4.025 * si.MPa

    def test_tau_d(self):
        assert self.cisaillement.tau_rd.value == 13086491.57740332

    def test_taux_tau_d(self):
        assert self.cisaillement.taux_tau_rd == {
            "equ6.13": 3.2513022552554838,
            "equ6.60": 5.032476193026768,
        }
