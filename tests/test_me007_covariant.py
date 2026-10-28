"""Tests of F02 mathematical scalar-tensor ANSATZ, not evidence of information gravity."""
import math
import unittest
from toe001.me007_covariant import (Model, initial_state,derivative,identity_residuals,
    constraint,densities,rk4,simulate,dL_gw_over_em,frozen_thermal_identification_residual)

class Tests(unittest.TestCase):
    def test_positive_F(self):
        p=Model()
        self.assertGreater(p.F(.35),0)
        with self.assertRaises(ValueError):initial_state(Model(xi=1),q=1.1)
    def test_definitions(self):
        p=Model()
        for q in (0,.3,-.8):
            e=1e-6
            self.assertAlmostEqual((p.F(q+e)-p.F(q-e))/(2*e),p.Fq(q),places=8)
            self.assertAlmostEqual((p.U(q+e)-p.U(q-e))/(2*e),p.Uq(q),places=8)
    def test_constraint_initial(self):
        p=Model();y=initial_state(p)
        self.assertLess(abs(constraint(y,p)),1e-14)
    def test_scalar_eom(self):
        p=Model();y=initial_state(p)
        self.assertLess(abs(identity_residuals(y,p)['scalar_eom']),1e-13)
    def test_raychaudhuri(self):
        p=Model();y=initial_state(p)
        self.assertLess(abs(identity_residuals(y,p)['raychaudhuri']),1e-13)
    def test_no_cross_of_zero_F(self):
        with self.assertRaises(ValueError):initial_state(Model(xi=3),q=1.)
    def test_minimal_limit_q_zero(self):
        # q=0 and qdot=0 is an exact solution and reproduces TOE-001's FLRW equations.
        p=Model(xi=.25); y=initial_state(p,q=0,qdot=0)
        d=derivative(y,p); self.assertEqual(d[5],0)
        self.assertAlmostEqual(d[7],-(y[2]**2+y[3]**2+(1+p.w)*y[8])/(2*p.mpl2),places=13)
        self.assertAlmostEqual(y[7]**2,densities(y,p)['rho_base']/(3*p.mpl2),places=13)
    def test_xi_zero_still_has_separate_q(self):
        p=Model(xi=0);y=initial_state(p)
        self.assertAlmostEqual(p.F(y[4]),p.mpl2)
        self.assertNotEqual(densities(y,p)['rho_q'],0.)
    def test_ratio(self):
        self.assertEqual(dL_gw_over_em(1,1),1)
        self.assertAlmostEqual(dL_gw_over_em(4,1),.5)
        with self.assertRaises(ValueError):dL_gw_over_em(0,1)
    def test_constant_mi_q_obstruction(self):
        p=Model();q=p.MI()
        self.assertGreater(q,0)
        self.assertAlmostEqual(frozen_thermal_identification_residual(p,0),p.mpl2*p.mu2*q)
        self.assertGreater(frozen_thermal_identification_residual(p,1),0)
    def test_xi_zero_constant_mi_still_requires_source(self):
        p=Model(xi=0.)
        self.assertGreater(frozen_thermal_identification_residual(p,0),0)
    def test_step_convergence(self):
        p=Model()
        a=simulate(p,steps=200,dt=.01)['final_state'][4]
        b=simulate(p,steps=400,dt=.005)['final_state'][4]
        c=simulate(p,steps=800,dt=.0025)['final_state'][4]
        self.assertLess(abs(b-c),abs(a-b)/8)
    def test_simulation_constraint(self):
        r=simulate(steps=2400,dt=.001)
        self.assertLess(r['max_normalized_friedmann_residual'],1e-9)
        self.assertLess(r['max_q_eom_residual'],1e-12)
        self.assertLess(r['max_raychaudhuri_residual'],1e-12)
        self.assertGreater(r['min_F'],0)
    def test_claim_gates(self):
        s=simulate(steps=3)
        self.assertFalse(s['physical_information_field_identified'])
        self.assertFalse(s['new_EFMW_effect_established'])
        self.assertFalse(s['full_theory_of_everything'])
    def test_no_analogue_measurement(self):
        # The propagated q is chosen initial data; not measured or inferred from the Gibbs MI.
        p=Model();y=initial_state(p)
        self.assertNotAlmostEqual(y[4],p.MI())

if __name__=='__main__':unittest.main()
