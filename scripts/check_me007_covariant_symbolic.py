"""F02 independent symbolic checks of selected 0+1D FLRW scalar--tensor reductions.

Proves algebraic identities in the assumed FLRW sector, NOT general curved-space
formal verification or physical identification of information with q.
"""
import json
from pathlib import Path
import sympy as sp

q,v,H,Hdot,qdd,rhop,md,z,xi,mu2,lam,press = sp.symbols('q v H Hdot qdd rhop md z xi mu2 lam press',real=True)
# md stands for M_Pl^2. md,z,mu2 positive in the physical test.
F=md*(1-xi*q*q)
Fq=sp.diff(F,q);Fqq=sp.diff(Fq,q);K=md*z;U=sp.Rational(1,2)*md*mu2*q*q;Uq=sp.diff(U,q)
R=6*(2*H*H+Hdot)
# Full scalar and acceleration equations, in a 0+1D reduction.
E_q=K*(qdd+3*H*v)+Uq-sp.Rational(1,2)*Fq*R
E_H=-2*F*Hdot-(rhop+K*v*v+Fqq*v*v+Fq*qdd-H*Fq*v)
sol=sp.solve((E_q,E_H),(qdd,Hdot),dict=True)[0]
# qdd= (src +3Fq Hdot)/K, Hdot =-(rhop+(K+Fqq)v²-HFqv+Fq/K*src)/(2F+3Fq²/K)
src=-3*H*K*v-Uq+6*Fq*H**2
hformula=-(rhop+(K+Fqq)*v*v-H*Fq*v+(Fq/K)*src)/(2*F+3*Fq*Fq/K)
qformula=(src+3*Fq*hformula)/K
# Friedmann identity dC/dt=3H*(-EH), after matter and q EOM are applied.
# C=3 F H²+3 H Fdot-rho_base-rho_q, q kinetic has K v²/2.
# dot rho_base=-3H(rho_base+p_base).
# dot rho_q=K v*qdd+Uq*v.
Cdot=(3*Fq*v*H*H+6*F*H*Hdot+3*Hdot*Fq*v+3*H*(Fqq*v*v+Fq*qdd)
      +3*H*rhop-(K*v*qdd+Uq*v))
# The expected total identity is only a linear combination of E_q and E_H,
# avoiding the circular assertion that it is zero by replacing field eqs first.
# E_H=-2 F Hdot -(rhop+K v²+Fqqv²+Fq qdd-HFqv).
# Derive Cdot = -3 H E_H - v E_q: test:
comb=sp.expand(Cdot+3*H*E_H+v*E_q)
results={
 'scalar_equation_solved':sp.simplify(E_q.subs(sol))==0,
 'acceleration_equation_solved':sp.simplify(E_H.subs(sol))==0,
 'explicit_Hdot_formula':sp.simplify(sol[Hdot]-hformula)==0,
 'explicit_qdd_formula':sp.simplify(sol[qdd]-qformula)==0,
 'constraint_ward_identity':sp.simplify(comb)==0,
 'F_derivative':sp.simplify(Fq+2*md*xi*q)==0,
 'constant_nonzero_q_obstruction':sp.simplify(Uq-sp.Rational(1,2)*Fq*R-md*q*(mu2+xi*R))==0,
 'no_coupling_planck_recovery':sp.simplify(F.subs(xi,0)-md)==0,
}
record={
 'kind':'F02_scalar_tensor_FLRW_symbolic_checks_not_historical_EFMW',
 'status':'PASS' if all(results.values()) else 'FAIL',
 'count':len(results),
 'checks':[{'name':key,'status':'PASS' if val else 'FAIL','residual':'0' if val else 'nonzero'} for key,val in results.items()],
 'scope':'Independent SymPy identities for a chosen Jordan-frame FLRW scalar-tensor model; no unique observable-to-field mapping; no external experiment.',
 'information_field_physically_identified':False,
 'quantum_gravity_derived':False,
}
if __name__=='__main__':
 p=Path('results/me007_covariant_symbolic.json');p.parent.mkdir(exist_ok=True,parents=True)
 p.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n',encoding='utf8')
 print(json.dumps({'status':record['status'],'count':len(results),'failed':[k for k,v in results.items() if not v]}))
 if record['status']!='PASS':raise SystemExit(1)
