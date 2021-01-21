from sympy.solvers import solve
from sympy.abc import x

def getDeepDotQuality(func, arg, val, n = 3):
  dy = func.diff(arg)
  dyn = dy.subs(arg, val)
  if (dyn == 0):
    return getDeepDotQuality(dy, arg, val, n+1)
  elif (n % 2 == 1):
    return 'has an inflection point'
  elif (dyn > 0):
    return 'is min'
  else:
    return 'is max'
  return 'aaaaaa'

def getDotQuality(func, arg, val):
  dy = func.subs(arg, val)
  if (dy > 0):
    return 'is min'
  elif (dy < 0):
    return 'is max'
  else:
    return getDeepDotQuality(func, arg, val)

def findExtremums(func, arg):
  dy = func.diff(arg)
  ddy = dy.diff(arg)
  extremums = solve(dy, arg)

  for val in extremums:
    print('%s %s for x=%s' % (func, getDotQuality(ddy, arg, val), val))

  return

findExtremums(x**2, x)
findExtremums(x**3 - 2*x**2 + x + 1, x)
findExtremums(2*x**4, x)
findExtremums(2*x**3, x)