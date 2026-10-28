"""Reproducible tests of the F01 identifiability / operational MI candidate."""
import math
import unittest
from toe001.me007_identity import (Pair,covariance,correlation,mutual_information_nats,
    information_susceptibility,mi_from_covariance,gibbs_samples,empirical_covariance,energy_sources,operational_summary)

class InformationIdentityTests(unittest.TestCase):
    def test_equilibrium_covariance_inverse(self):
        p=Pair(); a,b,c=covariance(p)
        self.assertAlmostEqual(p.m2*a+p.gamma*b,1/p.beta,places=13)
        self.assertAlmostEqual(p.m2*b+p.gamma*c,0,places=13)
        self.assertAlmostEqual(p.gamma*a+p.M2*b,0,places=13)
        self.assertAlmostEqual(p.gamma*b+p.M2*c,1/p.beta,places=13)
    def test_gaussian_mi_closed_form(self):
        p=Pair();self.assertAlmostEqual(mutual_information_nats(p),mi_from_covariance(*covariance(p)),places=14)
    def test_information_response_matches_cross_covariance(self):
        for gamma in (-.5,-.25,0,.25,.5):
            p=Pair(gamma=gamma,beta=2)
            analytic=information_susceptibility(p)
            c12=covariance(p)[1]
            self.assertAlmostEqual(analytic, -p.beta*c12,places=14)
            eps=1e-5
            deriv=(mutual_information_nats(Pair(gamma=gamma+eps))-
                   mutual_information_nats(Pair(gamma=gamma-eps)))/(2*eps)
            self.assertAlmostEqual(analytic,deriv,places=8)

    def test_zero_mixing_means_zero_mi(self):
        self.assertEqual(mutual_information_nats(Pair(gamma=0)),0)
        self.assertEqual(correlation(Pair(gamma=0)),0)
    def test_mi_independent_of_beta(self):
        self.assertAlmostEqual(mutual_information_nats(Pair(beta=.1)),mutual_information_nats(Pair(beta=27)),places=14)
    def test_sign_reversal_preserves_mi_not_correlation(self):
        self.assertEqual(mutual_information_nats(Pair(gamma=.25)),mutual_information_nats(Pair(gamma=-.25)))
        self.assertEqual(correlation(Pair(gamma=.25)),-correlation(Pair(gamma=-.25)))
    def test_stability_boundary(self):
        self.assertGreater(mutual_information_nats(Pair(gamma=1.999)),mutual_information_nats(Pair(gamma=.25)))
        with self.assertRaises(ValueError):Pair(gamma=2)
        with self.assertRaises(ValueError):Pair(gamma=3)
    def test_invalid_covariance(self):
        for x in [(1,1,1),(1,2,1),(0,0,2)]:
            with self.assertRaises(ValueError):mi_from_covariance(*x)
    def test_partition_invariance_and_nonunique_info(self):
        p=Pair(); baselines=[];subtotals=[]
        for a in (0,.2,.5,.8,1):
            for k in (.1,.5,1,3,-2):
                s=energy_sources(.7,-.3,.2,-.1,.2,0,p,a,k)
                self.assertAlmostEqual(s['rho_total'],s['rho_reconstructed'],places=13)
                self.assertAlmostEqual(s['p_total'],s['p_reconstructed'],places=13)
                baselines.append((s['rho_total'],s['p_total']))
                subtotals.append(s['rho_information'])
        self.assertEqual(len(set(baselines)),1)
        self.assertGreater(len(set(round(x,9) for x in subtotals)),3)
    def test_two_alpha_partitions_same_dynamics_but_distinct_information(self):
        p=Pair()
        x=energy_sources(.7,-.3,.2,-.1,.2,0,p,.1,1)
        y=energy_sources(.7,-.3,.2,-.1,.2,0,p,.9,1)
        self.assertEqual(x['rho_total'],y['rho_total'])
        self.assertNotAlmostEqual(x['rho_information'],y['rho_information'],places=10)
    def test_kappa1_R_density_equals_chi_and_mix(self):
        p=Pair();s=energy_sources(.7,-.3,.2,-.1,.2,0,p,.5,1)
        self.assertEqual(s['rho_R_for_SM_as_ordinary_kappa1'],s['rho_chi_plus_mix'])
    def test_empirical_mi_approximates_population(self):
        p=Pair();sample_cov=empirical_covariance(gibbs_samples(p,80000,20261028))
        self.assertLess(abs(mi_from_covariance(*sample_cov)-mutual_information_nats(p)),.0035)
    def test_null_sampler_independence(self):
        s=empirical_covariance(gibbs_samples(Pair(gamma=0),80000,20261028))
        self.assertLess(mi_from_covariance(*s),.0001)
    def test_summary_keeps_claim_gate_false(self):
        r=operational_summary(Pair(),n=500,seed=4)
        self.assertFalse(r['is_efmw_specific'])
        self.assertFalse(r['me006_recursive_tensor_physically_identified'])
        self.assertFalse(r['gravity_from_information_derived'])
        self.assertFalse(r['experiment_on_real_physical_data'])
if __name__=='__main__':unittest.main()
