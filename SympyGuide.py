#   A quick guide to sympy
from sympy import *

#   INITIALIZE
x,y,z = symbols('x y z')
f = x**3 + exp(x) + cos(3*x) + log(sin(x))
print('function: '); print(f)

    #initialize with string:
expression = "x**3 + exp(x) + cos(3*x) + log(sin(x))"
f = sympify(expression)

print()
#   VALUE
value = f.subs(x,3)
print('symbolic f(3): '); print(value)

value = N(value)    # or evalf()
print('numeric f(3): '); print(value)

value = value.evalf(100)    # up to 1e-100 precision ?!
print('numagic f(3): '); print(value)

print('1/6: ') # don't test 1/7 
value = (x/6).subs(x,1); print(value.evalf(100))

    #multivariable
f1 = x*y*z
print('with x=2, y=4, z=3 then f1 = x*y*z = ')
value = f.subs( [(x,2),(y,4),(z,3)] )
print(value)

print()
#   DERIVATIVE
df = diff(f,x)
print('first order derivative: '); print(df)

df = diff(f,x,2)    # or diff(f, x, x)
print('second order derivative: '); print(df)

    #multivariable
df = diff(x*y*z + x**y, x, y)   #derivative with respect to x then y
print(df)

print(value)

print()
#   INTEGRAL

print()
#   MATRIX

print()
#   SOLVER  f(x) = 0
fx = x**2 - 5
solution = solveset(fx, x, domain=S.Reals)
print(solution)

fx = sin(x) - 1
solution = solveset(fx, x, domain=S.Reals)
print(solution)

#