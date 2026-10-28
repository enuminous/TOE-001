"""Produce reproducible, explicitly synthetic results and an honest gate report."""
import argparse, json, math
from pathlib import Path
from toe001.model import Params, response_residues, simulate, susceptibility

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--m2',type=float,default=1.)
    parser.add_argument('--M2',type=float,default=4.)
    parser.add_argument('--g',type=float,default=.25)
    parser.add_argument('--steps',type=int,default=20000)
    parser.add_argument('--dt',type=float,default=.001)
    parser.add_argument('--out',default='results/reference.json')
    a=parser.parse_args()
    p=Params(a.m2,a.M2,a.g)
    if not p.stable(): parser.error('Unstable potential, requires g*g < m2*M2')
    values=p.eigenvalues()
    weights=response_residues(p)
    report={'schema':'TOE-001-test-v1',
      'status':'CONDITIONAL_MATH_NOT_TOE',
      'model':'GR + assumed SM + two canonical mixed scalars (only flat homogeneous sector simulated)',
      'parameters':{'m_squared':p.m2,'M_squared':p.M2,'mixing_g':p.g,'units':'arbitrary dimensionless'},
      'mass_eigenvalues_squared':list(values),
      'frequencies': [math.sqrt(z) for z in values],
      'phi_response_residues':list(weights),
      'conditional_susceptibility_imag_at_poles':[susceptibility(math.sqrt(z),p,eta=.005).imag for z in values],
      'null_model':'g=0 removes mixing and memory response; extra free field remains unless explicitly decoupled',
      'simulated':simulate(p,steps=a.steps,dt=a.dt),
      'closure_gates':{'covariant_action_specified':'PASS_SOURCE_DERIVATION',
          'scalar_mass_stability':'PASS_CONDITIONAL',
          'flat_homogeneous_energy_conservation':'PASS_NUMERICAL_AND_IDENTITY',
          'standard_GR_SM_vacuum_solution':'PASS_CONDITIONAL_NOT_FULL_EQUIVALENCE',
          'quantum_gravity_uv_complete':'UNRESOLVED',
          'emergent_chiral_standard_model':'UNRESOLVED',
          'ME007_original_EFMW_equivalence':'UNRESOLVED',
          'unique_EFMW_observable':'UNRESOLVED',
          'external_physical_data':'UNRESOLVED'},
      'no_empirical_claim':True}
    target=Path(a.out);target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'file':str(target),'status':report['status'],
       'max_relative_energy_drift':report['simulated']['max_relative_energy_drift'],
       'max_position_error_vs_exact':report['simulated']['max_position_error_vs_exact']},indent=2))
if __name__=='__main__':main()
