"""F03 regression tests of synthetic classical oscillators, not informational gravity."""
import tempfile
import unittest
from pathlib import Path
from toe001.me007_experiment import (
    Calibration,expected_mi,expected_covariance,coupled_langevin,
    csv_read,csv_write,_mi,summarize,file_sha256)

class F03Tests(unittest.TestCase):
    def test_normalization_and_null(self):
        self.assertAlmostEqual(expected_mi(Calibration()),.007874178484069584,places=14)
        self.assertEqual(expected_mi(Calibration(gamma=0)),0)
    def test_signed_crosscovariance_and_even_mi(self):
        a=Calibration(gamma=.5);b=Calibration(gamma=-.5)
        self.assertEqual(expected_mi(a),expected_mi(b))
        self.assertAlmostEqual(expected_covariance(a)[1],-expected_covariance(b)[1])
    def test_equilibrium_matrix_inverse(self):
        p=Calibration();a,b,c=expected_covariance(p)
        self.assertAlmostEqual(p.beta*(p.m2*a+p.gamma*b),1)
        self.assertAlmostEqual(p.beta*(p.gamma*a+p.M2*b),0)
        self.assertAlmostEqual(p.beta*(p.gamma*b+p.M2*c),1)
    def test_dynamics_repeatable(self):
        p=Calibration()
        a=list(coupled_langevin(p,steps=100,burn=20,seed=1))
        b=list(coupled_langevin(p,steps=100,burn=20,seed=1))
        self.assertEqual(a,b)
    def test_dynamics_seed_independent(self):
        p=Calibration()
        a=list(coupled_langevin(p,steps=100,burn=20,seed=1))
        b=list(coupled_langevin(p,steps=100,burn=20,seed=2))
        self.assertNotEqual(a,b)
    def test_dynamic_record_not_iid_cov_generator(self):
        p=Calibration();r=list(coupled_langevin(p,steps=6000,burn=1000,stride=1))
        self.assertEqual(len(r),5000)
        x=[v[1] for v in r];mean=sum(x)/len(x)
        var=sum((z-mean)**2 for z in x)
        lag=sum((x[i]-mean)*(x[i-1]-mean) for i in range(1,len(x)))
        self.assertGreater(lag/var,.97)
    def test_simulated_mi_tracks_theory_with_error_tolerance(self):
        p=Calibration(gamma=.6)
        r=list(coupled_langevin(p,steps=80000,burn=8000,stride=8,seed=83))
        value=summarize(r,p,bootstrap=25)['observed_MI_nats']
        self.assertLess(abs(value-expected_mi(p)),.025)
    def test_zero_coupling_null_approximately_zero(self):
        p=Calibration(gamma=0)
        r=list(coupled_langevin(p,steps=60000,burn=7000,stride=7,seed=42))
        self.assertLess(summarize(r,p,bootstrap=20)['observed_MI_nats'],.012)
    def test_signed_cross_correlation_in_dynamic_data(self):
        p=Calibration(gamma=1.0)
        r=list(coupled_langevin(p,steps=100000,burn=10000,stride=10,seed=91))
        m=summarize(r,p,bootstrap=20)
        self.assertLess(m['estimated_correlation'],0)
    def test_csv_roundtrip_and_hash(self):
        p=Calibration();r=list(coupled_langevin(p,steps=900,burn=30,stride=3))
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'data.csv';csv_write(path,r)
            q=csv_read(path)
            self.assertEqual(len(q),len(r))
            self.assertEqual(len(file_sha256(path)),64)
    def test_reject_too_short_measured_file(self):
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'data.csv';csv_write(path,[(1,2,3),(2,3,4)])
            with self.assertRaises(ValueError):csv_read(path)
    def test_reject_bad_time(self):
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'data.csv';csv_write(path,[(1,2,3)]*150)
            with self.assertRaises(ValueError):csv_read(path)
    def test_positive_noise_debiasing(self):
        p=Calibration(noise_phi=.1,noise_chi=.1)
        a,b,c=expected_covariance(p)
        mi,rho,cov=_mi((a+.01,b,c+.01),p)
        self.assertAlmostEqual(mi,expected_mi(p),places=12)
    def test_invalid_covariance_rejected(self):
        with self.assertRaises(ValueError):_mi((.1,1,.1),Calibration())
    def test_invalid_model(self):
        for x in ({'gamma':2},{'dt':.5},{'damping':0},{'noise_phi':-1}):
            with self.assertRaises(ValueError):Calibration(**x)
    def test_claim_gates_fail_closed(self):
        p=Calibration();r=list(coupled_langevin(p,steps=4000,burn=200,stride=7))
        s=summarize(r,p,bootstrap=10)
        self.assertEqual(s['pass_physics'],'UNRESOLVED')
        self.assertFalse(s['q_field_identified_by_measurement'])
        self.assertFalse(s['distinguishes_EFMW_from_ordinary_oscillators'])
    def test_partition_parameters_absent(self):
        p=Calibration()
        self.assertNotIn('alpha',vars(p))
        self.assertNotIn('kappa',vars(p))
    def test_analysis_time_validation(self):
        with self.assertRaises(ValueError):
            summarize([(1,1,2)]*200,Calibration(),bootstrap=10)

if __name__=='__main__':unittest.main()
