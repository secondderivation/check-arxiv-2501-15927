#!/usr/bin/env python3
"""Independent standard-library audit. No CLASS code is imported or executed."""
import math,json,pathlib,time,signal,functools,bisect
signal.alarm(60)
t0=time.monotonic()
def psi(a): return .015*2.9**5.6*a**2.9/(1+(2.9*a)**5.6)
def psip(a):
 t=(2.9*a)**5.6
 return psi(a)/a*(2.9-5.6*t/(1+t))
def quad(fn,a,b,tol):
 if a==b:return 0.
 if a>b:return -quad(fn,b,a,tol)
 fa,fb,fm=fn(a),fn(b),fn((a+b)/2)
 def rec(a,b,fa,fb,fm,S,eps,n):
  m=(a+b)/2; fl=fn((a+m)/2); fr=fn((m+b)/2)
  L=(m-a)*(fa+4*fl+fm)/6; R=(b-m)*(fm+4*fr+fb)/6
  if abs(L+R-S)<=15*eps:return L+R+(L+R-S)/15
  if n==0:raise RuntimeError('Quadrature did not converge')
  return rec(a,m,fa,fm,fl,L,eps/2,n-1)+rec(m,b,fm,fb,fr,R,eps/2,n-1)
 return rec(a,b,fa,fb,fm,(b-a)*(fa+4*fm+fb)/6,tol,35)
@functools.lru_cache(None)
def I(a,tol=1e-14): return quad(lambda x:psi(x)/x if x else 0.,a,1.,tol)
close=lambda v,r:abs(v-r)<=1e-9+1e-6*abs(r)
r=1-.287; D0=3*r
# Independent spline via full tridiagonal second-derivative equations.
x=[math.exp(math.log(1e-20)+i*math.log(1e20)/999) for i in range(1000)]; x[-1]=1.
f=[psi(v)/v for v in x]; y=[0.]
for k in range(1,len(x)):y.append(y[-1]+(f[k]+f[k-1])*(x[k]-x[k-1])/2)
y=[v-y[-1] for v in y]
def slope(xx,yy,at):
 v=0.
 for i in range(3):
  j,k=[v for v in range(3) if v!=i]
  v+=yy[i]*(2*at-xx[j]-xx[k])/((xx[i]-xx[j])*(xx[i]-xx[k]))
 return v
n=len(x); h=[x[k+1]-x[k] for k in range(n-1)]; delta=[(y[k+1]-y[k])/h[k] for k in range(n-1)]
l=[0.]*n; d=[0.]*n; u=[0.]*n; rhs=[0.]*n
d[0]=2*h[0];u[0]=h[0];rhs[0]=6*(delta[0]-slope(x[:3],y[:3],x[0]))
for k in range(1,n-1):l[k]=h[k-1];d[k]=2*(h[k-1]+h[k]);u[k]=h[k];rhs[k]=6*(delta[k]-delta[k-1])
l[-1]=h[-1];d[-1]=2*h[-1];rhs[-1]=6*(slope(x[-3:],y[-3:],x[-1])-delta[-1])
for k in range(1,n):
 factor=l[k]/d[k-1];d[k]-=factor*u[k-1];rhs[k]-=factor*rhs[k-1]
M=[0.]*n; M[-1]=rhs[-1]/d[-1]
for k in range(n-2,-1,-1):M[k]=(rhs[k]-u[k]*M[k+1])/d[k]
def spline(a):
 k=max(0,min(n-2,bisect.bisect_right(x,a)-1)); H=h[k]; t=(a-x[k])/H
 v=(1-t)*y[k]+t*y[k+1]+H*H/6*(((1-t)**3-(1-t))*M[k]+(t**3-t)*M[k+1])
 dv=(y[k+1]-y[k])/H+H/6*((1-3*(1-t)**2)*M[k]+(3*t*t-1)*M[k+1])
 return v,dv
out={'grid':'grid.json','CAS':'not_run: sympy unavailable; analytic derivation in CONVENTIONS-AND-DERIVATION.md','points':[],'tolerance':{'relative':1e-6,'absolute':1e-9},'implementation':'standard library independent quadrature and spline; not CLASS execution'}
for pt in json.loads(pathlib.Path('results/grid.json').read_text())['points']:
 a=float(pt['a']);q=float(pt['q']) if '/' not in pt['q'] else -3298.4/72.3**2
 R=lambda v:r-8*q*I(v)
 D=lambda v:3*R(v)
 W=lambda v:-1-8*q*psi(v)/D(v)
 J=lambda v:math.log(R(v)/r)
 iv=I(a);dv=D(a);pv=psi(a);pp=psip(a);assert dv>0
 w=W(a);dw=8*q*(-pp*dv+24*q*pv*pv/a)/dv**2
 fd=[]
 for rel in [1e-3,1e-4,1e-5]:
  hh=a*rel;approx=(W(a+hh)-W(a-hh))/(2*hh)
  density_w=-1-a*(R(a+hh)-R(a-hh))/(2*hh)/(3*R(a))
  jp=(J(a+hh)-J(a-hh))/(2*hh)
  fd.append({'relative_step':rel,'dw':approx,'dw_absolute_error':abs(approx-dw),'dw_pass':close(approx,dw),'density_w':density_w,'density_w_pass':close(density_w,w),'J_prime':jp,'J_prime_pass':close(jp,-3*(1+w)/a)})
 iz,izp=spline(a); ds=D0+24*q*iz; ws=-1-8*q*pv/ds
 dw_formula=8*q*(-pp*ds+24*q*pv*pv/a)/ds**2
 dw_actual=-8*q*(pp*ds-pv*24*q*izp)/ds**2
 out['points'].append({'a':a,'q':q,'I_reference':iv,'quadrature_refinement_absolute_change':abs(iv-I(a,1e-12)),'D':dv,'w_corrected':w,'w_parent_printed':-1-8*q*pv/(D0+6*q*iv),'dw_corrected':dw,'J':J(a),'finite_differences':fd,'spline':{'Iz':iz,'I_absolute_error':abs(iz+iv),'I_pass':close(-iz,iv),'Iz_prime':izp,'Iz_prime_reference':pv/a,'Iz_prime_pass':close(izp,pv/a),'w':ws,'w_vs_continuum_pass':close(ws,w),'w_absolute_error':abs(ws-w),'dw_formula':dw_formula,'dw_of_interpolated_w':dw_actual,'dw_consistency_pass':close(dw_formula,dw_actual),'J':math.log(ds/D0),'J_derivative_consistency_pass':close(24*q*izp/ds,-3*(1+ws)/a)}})
I0=I(0.)
out['limits']={'I_at_zero':I0,'positive_q_global_bound_at_grid_matter':r/(8*I0),'q_0435_J_at_zero':math.log((r-8*.435*I0)/r),'example_q_1_early_D_using_example_matter_and_zero_photons_upper_bound':3*(1-(.02238280+.1201075)/.67810**2)-24*I0,'note':'Last D is an upper bound because positive photons lower it further. No CLASS run.'}
out['elapsed_seconds']=time.monotonic()-t0
pathlib.Path('results/raw-stdlib-checks.json').write_text(json.dumps(out,indent=2)+'\n')
summary={'point_count':len(out['points']),'finest_fd_w_all_pass':all(p['finite_differences'][-1]['density_w_pass'] for p in out['points']),'finest_fd_dw_all_pass':all(p['finite_differences'][-1]['dw_pass'] for p in out['points']),'finest_fd_J_all_pass':all(p['finite_differences'][-1]['J_prime_pass'] for p in out['points']),'max_quadrature_refinement_change':max(p['quadrature_refinement_absolute_change'] for p in out['points']),'spline_w_failures':sum(not p['spline']['w_vs_continuum_pass'] for p in out['points']),'spline_dw_consistency_failures':sum(not p['spline']['dw_consistency_pass'] for p in out['points']),'spline_J_derivative_failures':sum(not p['spline']['J_derivative_consistency_pass'] for p in out['points']),'max_spline_w_abs_error':max(p['spline']['w_absolute_error'] for p in out['points']),'limits':out['limits'],'elapsed_seconds':out['elapsed_seconds']}
pathlib.Path('results/stdlib-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
