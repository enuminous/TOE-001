"""Generate deterministic synthetic operational-information reference JSON."""
import json
from pathlib import Path
from toe001.me007_identity import Pair,operational_summary,energy_sources,information_susceptibility

def main():
    p=Pair()
    a=operational_summary(p,n=80000,seed=20261028)
    a['information_susceptibility_dMI_dgamma']=information_susceptibility(p)
    a['crosscovariance_response_identity_error']=abs(information_susceptibility(p)+p.beta*a['exact_covariance'][1])
    a['null_zero_mixing']=operational_summary(Pair(gamma=0),n=80000,seed=20261028)
    a['stability_boundary']='requires m2*M2 > gamma**2'
    a['canonical_me006']='I_mu_nu = T_phi_mu_nu + R_mu_nu (R not independently specified)'
    a['canonical_me007']='G_mu_nu + Lambda*g_mu_nu = 8piG*(T_mu_nu+kappa*I_mu_nu)'
    a['baseline']={ 'type':'standard two-mode Gaussian equilibrium', 'distinctive_EFMW_observable':False}
    a['stress_partition_example']={}
    for alpha,kappa in ((0,1),(.5,1),(1,1),(.5,3)):
        s=energy_sources(.7,-.3,.2,-.1,.2,0,p,alpha,kappa)
        a['stress_partition_example'][f'alpha={alpha},kappa={kappa}']={k:round(s[k],12) for k in ('rho_ordinary','rho_information','rho_total','rho_reconstructed')}
    dest=Path('results/me007_identity_reference.json')
    dest.parent.mkdir(exist_ok=True,parents=True)
    dest.write_text(json.dumps(a,indent=2)+'\n')
    print(json.dumps({k:a[k] for k in ['exact_MI_nats','sample_MI_nats','exact_correlation','n_samples']},indent=2))
    print('wrote',dest)
if __name__=='__main__':main()
