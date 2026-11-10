"""Strict recursive saved-reference comparator; no scientific code executes on import."""
import math
def compare(expected,actual,issues,at=''):
 if isinstance(expected,dict):
  if not isinstance(actual,dict) or set(expected)!=set(actual):issues.append(at+': keys differ');return
  for k in expected:
   if k!='elapsed_seconds':compare(expected[k],actual[k],issues,at+'/'+k)
 elif isinstance(expected,list):
  if not isinstance(actual,list) or len(expected)!=len(actual):issues.append(at+': length differs');return
  for i,(e,a) in enumerate(zip(expected,actual)):compare(e,a,issues,at+'/'+str(i))
 elif isinstance(expected,bool):
  if type(actual) is not bool or expected is not actual:issues.append(at+': boolean type/value differs')
 elif expected is None:
  if actual is not None:issues.append(at+': null value differs')
 elif isinstance(expected,str):
  if type(actual) is not str or expected!=actual:issues.append(at+': string type/value differs')
 elif isinstance(expected,(int,float)):
  if type(actual) not in (int,float) or not math.isfinite(actual) or abs(expected-actual)>1e-9+1e-6*abs(expected):issues.append(at+': tolerance failed')
 else:raise TypeError(at)
