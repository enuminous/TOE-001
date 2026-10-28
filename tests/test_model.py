import math
import unittest
from toe001.model import Params, energy, exact_solution, force, response_residues, simulate, susceptibility, verlet_step

class TOE001Tests(unittest.TestCase):
    def test_reference_mass_eigenvalues(self):
        a,b=Params().eigenvalues()
        self.assertAlmostEqual(a, (5-math.sqrt(9.25))/2, places=12)
        self.assertAlmostEqual(b, (5+math.sqrt(9.25))/2, places=12)
        self.assertTrue(a>0)
    def test_stability_boundary(self):
        self.assertTrue(Params(g=.5).stable())
        self.assertFalse(Params(g=2.0).stable())
        self.assertFalse(Params(g=2.1).stable())
        with self.assertRaises(ValueError):
            simulate(Params(g=2.1), steps=2)
    def test_negative_or_nan_mass_rejected(self):
        for p in (dict(m2=0),dict(M2=-1),dict(g=float('nan'))):
            with self.assertRaises(ValueError): Params(**p)
    def test_diagonalization(self):
        p=Params()
        for val, vec in zip(p.eigenvalues(),p.eigenvectors()):
            eq=(-p.m2*vec[0]-p.g*vec[1],-p.g*vec[0]-p.M2*vec[1])
            for i in (0,1): self.assertAlmostEqual(eq[i], -val*vec[i],places=12)
    def test_orthonormality(self):
        u,v=Params().eigenvectors()
        self.assertAlmostEqual(sum(x*y for x,y in zip(u,v)),0,places=13)
        self.assertAlmostEqual(sum(x*x for x in u),1,places=13)
    def test_residues(self):
        a,b=response_residues(Params())
        self.assertGreater(a,0)
        self.assertGreater(b,0)
        self.assertAlmostEqual(a+b,1,places=14)
    def test_null_exact_decoupling(self):
        p=Params(g=0)
        q,v=exact_solution(2.1,(1.,.5),(0.,0.),p)
        self.assertAlmostEqual(q[0],math.cos(2.1))
        self.assertAlmostEqual(q[1],.5*math.cos(4.2))
        w=.75
        self.assertAlmostEqual(susceptibility(w,p).real,
            (1/(p.m2-(w+.005j)**2)).real,places=12)
    def test_numerical_recovery(self):
        r=simulate(Params(),steps=20000,dt=.001)
        self.assertLess(r['max_relative_energy_drift'], 1e-5)
        self.assertLess(r['max_position_error_vs_exact'], 5e-5)
        self.assertLess(r['max_velocity_error_vs_exact'], 5e-5)
    def test_energy_derivative_cancels(self):
        p=Params()
        q=(.7,-.2);v=(.3,.4)
        ax,ay=force(q,p)
        # dE/dt computed with equations of motion is exactly zero.
        val=v[0]*(ax+p.m2*q[0]+p.g*q[1])+v[1]*(ay+p.M2*q[1]+p.g*q[0])
        self.assertAlmostEqual(val,0.,places=14)
    def test_zero_field_vacuum(self):
        p=Params()
        self.assertEqual(force((0,0),p),(0.,0.))
        self.assertEqual(energy((0,0),(0,0),p),0.)
    def test_nonzero_g_two_response_poles(self):
        p=Params()
        w1,w2=(math.sqrt(x) for x in p.eigenvalues())
        for w in (w1,w2):
            self.assertGreater(susceptibility(w,p,eta=.002).imag,0.)
        self.assertLess(abs(w1-w2),2)
    def test_unstable_solver_fails_closed(self):
        with self.assertRaises(ValueError): exact_solution(1,(1,0),(0,0),Params(g=2.2))
    def test_bad_timesteps_rejected(self):
        with self.assertRaises(ValueError): verlet_step((1,0),(0,0),0,Params())
    def test_dt_convergence(self):
        a=simulate(Params(),steps=5000,dt=.002)
        b=simulate(Params(),steps=10000,dt=.001)
        self.assertLess(b['max_position_error_vs_exact'],a['max_position_error_vs_exact'])
    def test_stability_vs_mass_gap(self):
        p=Params(m2=2.,M2=3.,g=.1)
        self.assertAlmostEqual(sum(p.eigenvalues()),5.)
        a,b=p.eigenvalues()
        self.assertAlmostEqual(a*b, 6-.01)

if __name__=='__main__': unittest.main()
