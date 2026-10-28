"""Frozen reference reproducibility (toy-model evidence, not physical data)."""
from pathlib import Path
import json
import math
import unittest
from toe001.model import Params
from toe001.me007 import Gravity, simulate_flrw

ROOT=Path(__file__).resolve().parents[1]

class TestFrozenME007Reference(unittest.TestCase):
    def test_reproduce_reference_diagnostics(self):
        frozen=json.loads((ROOT/'results/me007_flrw_reference.json').read_text())
        p=Params(m2=frozen['parameters']['m2'],M2=frozen['parameters']['M2'],g=frozen['parameters']['mixing'])
        cfg=Gravity(mpl2=frozen['parameters']['Mpl2'],cosmological_constant=frozen['parameters']['Lambda'],
                    kappa=frozen['parameters']['kappa'],allocation=frozen['parameters']['allocation'],w=frozen['parameters']['w'])
        y=frozen['initial_conditions']
        result=simulate_flrw(p,cfg,steps=frozen['steps'],dt=frozen['dt'],
                             phi=y['phi'],chi=y['chi'],u=y['phidot'],v=y['chidot'],rho_m=y['rho_m'])
        for key in ('max_relative_friedmann_residual','max_partition_exchange_error','max_total_source_mismatch'):
            self.assertTrue(math.isclose(result[key],frozen[key],abs_tol=1e-12,rel_tol=0),key)
        for actual,expected in zip(result['final_state'],frozen['final_state']):
            self.assertAlmostEqual(actual,expected,places=12)
        self.assertFalse(result['historical_efmw_information_tensor_identified'])
        self.assertFalse(result['full_theory_of_everything'])

    def test_reference_contains_only_conditional_claims(self):
        frozen=json.loads((ROOT/'results/me007_flrw_reference.json').read_text())
        self.assertEqual(frozen['status'],'CONDITIONAL_CLASSICAL_FLRW_ONLY')
        self.assertEqual(len(frozen['trace']),25)
        self.assertFalse(frozen['quantum_gravity_derived'])

if __name__=='__main__':unittest.main()
