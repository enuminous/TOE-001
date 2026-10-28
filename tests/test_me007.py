"""Tests of NEW ME-007 candidate (not the historical EFMW tensor)."""
import math
import unittest
from toe001.model import Params
from toe001.me007 import (Gravity, potential, stress, energy_exchange,
    initial_state, hubble_constraint, derivative, derivative_sectors,
    rk4, simulate_flrw)

class TestME007Candidate(unittest.TestCase):
    def setUp(self):
        self.p=Params()
        self.gr=Gravity()
        self.y=initial_state(self.p,self.gr)

    def test_frozen_reference_has_no_constraint_violation(self):
        self.assertLess(abs(hubble_constraint(self.y,self.p,self.gr)),1e-14)

    def test_stable_mass_quadratic_nonnegative(self):
        for phi,chi in [(1,0),(0,1),(-0.5,1.3),(1,1),(-2,-.2)]:
            self.assertGreaterEqual(potential(phi,chi,self.p),0)

    def test_source_partition_matches_total_for_varied_allocations(self):
        for alpha in (0, 0.12, .5, .8, 1):
            for kappa in (0.1,1,2.0,-3.0):
                gr=Gravity(kappa=kappa,allocation=alpha)
                s=stress(*self.y[:4],self.y[6],self.p,gr)
                self.assertAlmostEqual(s['rho_assembled'],s['rho_total'])
                self.assertAlmostEqual(s['p_assembled'],s['p_total'])

    def test_exchange_is_on_shell_balance_for_all_splits(self):
        for alpha in (0,.3,.5,1):
            for kappa in (0.5,1,3):
                gr=Gravity(kappa=kappa,allocation=alpha,w=1/3)
                y=initial_state(self.p,gr)
                q1,q2=energy_exchange(*y[:4],self.p,gr)
                b1,b2=derivative_sectors(y,self.p,gr)
                self.assertAlmostEqual(q1,b1,places=12)
                self.assertAlmostEqual(q2,b2,places=12)
                self.assertAlmostEqual(b1+kappa*b2,0.,places=12)

    def test_nonconservation_of_individual_sectors_is_real(self):
        gr=Gravity(allocation=0)
        y=initial_state(self.p,gr)
        q1,q2=energy_exchange(*y[:4],self.p,gr)
        self.assertNotAlmostEqual(q1,0.,places=8)
        self.assertAlmostEqual(q1+gr.kappa*q2,0.,places=12)

    def test_zero_mixing_sector_exchanges_vanish(self):
        p=Params(g=0)
        for a in (0,.5,1):
            gr=Gravity(allocation=a)
            y=initial_state(p,gr)
            q1,q2=energy_exchange(*y[:4],p,gr)
            self.assertEqual(q1,0)
            self.assertEqual(q2,0)

    def test_nec_and_raychaudhuri_nonpositive(self):
        s=stress(*self.y[:4],self.y[6],self.p,self.gr)
        self.assertGreaterEqual(s['rho_plus_p_scalar'],0)
        self.assertLessEqual(derivative(self.y,self.p,self.gr)[5],0)

    def test_parameter_validation(self):
        for kw in [dict(mpl2=0),dict(kappa=0),dict(allocation=-.1),dict(allocation=1.1),dict(w=-2),dict(w=float('nan'))]:
            with self.assertRaises(ValueError): Gravity(**kw)

    def test_initial_matter_continuity(self):
        gr=Gravity(w=1/3)
        y=initial_state(self.p,gr)
        dy=derivative(y,self.p,gr)
        self.assertAlmostEqual(dy[-1],-4*y[5]*y[6])

    def test_rk4_flat_friedmann_preservation(self):
        r=simulate_flrw(steps=2400,dt=.001)
        self.assertLess(r['max_relative_friedmann_residual'],1e-8)
        self.assertLess(r['max_partition_exchange_error'],1e-12)
        self.assertLess(r['max_total_source_mismatch'],1e-12)
        self.assertFalse(r['full_theory_of_everything'])

    def test_rk4_convergence_ratio(self):
        p=self.p;gr=self.gr
        a=simulate_flrw(p,gr,steps=400,dt=.004)['final_state']
        b=simulate_flrw(p,gr,steps=800,dt=.002)['final_state']
        c=simulate_flrw(p,gr,steps=1600,dt=.001)['final_state']
        ea=abs(a[0]-b[0]); eb=abs(b[0]-c[0])
        self.assertGreater(ea, 10*eb)

    def test_flat_total_evolution_independent_of_allocation(self):
        a=simulate_flrw(gr=Gravity(allocation=0.1,kappa=0.5),steps=300,dt=.002)
        b=simulate_flrw(gr=Gravity(allocation=.8,kappa=3),steps=300,dt=.002)
        self.assertEqual(a['final_state'],b['final_state'])

    def test_reject_unstable_initial_model(self):
        with self.assertRaises(ValueError):initial_state(Params(g=3),Gravity())

    def test_total_flrw_energy_continuity(self):
        y=self.y; gr=self.gr;p=self.p
        phi,chi,u,v,a,H,rho=y
        f=derivative(y,p,gr)
        drho=f[-1]+u*f[2]+v*f[3]+(p.m2*phi+p.g*chi)*u+(p.M2*chi+p.g*phi)*v
        st=stress(phi,chi,u,v,rho,p,gr)
        self.assertAlmostEqual(drho+3*H*(st['rho_total']+st['p_total']),0,places=12)

if __name__=='__main__':unittest.main()
