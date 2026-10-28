#!/usr/bin/env python3
"""Independent symbolic algebra gates for the selected TOE-001 ME-007 realization.

Requires SymPy. Confirms scalar energy identities in homogeneous FLRW; it is
NOT a four-dimensional formalization or evidence of a new fundamental theory.
"""
from __future__ import annotations
import json
import sympy as sp
from pathlib import Path

phi, chi, u, v, H, rm, m2, M2, gm, alpha, kappa, mpl2, w, Lambda = sp.symbols(
    'phi chi u v H rho_m m2 M2 g alpha kappa Mpl2 w Lambda', real=True)
vars_=[phi,chi,u,v,H,rm]
vel=[u,v,-3*H*u-m2*phi-gm*chi,-3*H*v-M2*chi-gm*phi,
     -(u*u+v*v+(1+w)*rm)/(2*mpl2),-3*H*(1+w)*rm]
V=(m2*phi**2+M2*chi**2)/2+gm*phi*chi
rho_sc=(u*u+v*v)/2+V
p_sc=(u*u+v*v)/2-V
rho_o=rm+u*u/2+m2*phi**2/2+alpha*gm*phi*chi
p_o=w*rm+u*u/2-m2*phi**2/2-alpha*gm*phi*chi
rho_i=(v*v/2+M2*chi**2/2+(1-alpha)*gm*phi*chi)/kappa
p_i=(v*v/2-M2*chi**2/2-(1-alpha)*gm*phi*chi)/kappa
rho=rm+rho_sc
p=w*rm+p_sc

def Dt(f):
    return sp.expand(sum(sp.diff(f,x)*dx for x,dx in zip(vars_,vel)))

def zero(name,expr):
    simplified=sp.factor(sp.cancel(expr))
    if simplified != 0:
        raise AssertionError(f'{name}: {simplified}')
    return {'name':name,'status':'PASS','residual':str(simplified)}

Q=-gm*((1-alpha)*chi*u-alpha*phi*v)
F=3*mpl2*H**2 - Lambda*mpl2-rho
checks=[
    zero('total density decomposition',rho_o+kappa*rho_i-rho),
    zero('total pressure decomposition',p_o+kappa*p_i-p),
    zero('ordinary exchange',Dt(rho_o)+3*H*(rho_o+p_o)-Q),
    zero('information exchange',Dt(rho_i)+3*H*(rho_i+p_i)+Q/kappa),
    zero('total conservation',Dt(rho)+3*H*(rho+p)),
    zero('Friedmann constraint propagation',Dt(F)),
    zero('Raychaudhuri sign source',(-2*mpl2*vel[4])-(u*u+v*v+(1+w)*rm)),
    zero('normal-mode determinant',sp.det(sp.Matrix([[m2,gm],[gm,M2]]))-(m2*M2-gm**2)),
]
result={
    'kind':'TOE-001-ME007-offshell-expression-substitution-symbolic-gates',
    'status':'PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL',
    'count':len(checks),
    'scope':'Polynomial identities along specified flat-FLRW on-shell equations, using SymPy, not Lean verification of general 4D geometry.',
    'checks':checks,
    'scientific_closure':False,
}
if __name__=='__main__':
    output=Path('results/me007_symbolic_checks.json')
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['count'],'file':str(output)}))
