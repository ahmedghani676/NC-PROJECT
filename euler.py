# Python library for symbolic mathematics it gives function as sub symbols which make working with formulas ike 2x or sinx much more easier.
import sympy as sp
from math import log as ln  # for mathematical operations

print("Enter the lower limits:")
a = float(input())
print("Enter the upper limit")
b = float(input())
print("enter the value of h")
h = float(input())
# value of x and y assigned by the user
print("enter the initial value of t and the y value")
c = float(input())
m = float(input())
print("value of y is:")
print(m)
x = sp.symbols('x')  # x and y symbols
y = sp.symbols('y')
function = "e**(x-y)"  # function to be entered by the user
function = function.replace("e*", "E*")
func = sp.sympify(function)
i = a
ans = h*sp.N(func.subs(x, 0.5))
while True:
    if i == b:
        break
    # x and y are being subsituted by the values of i and m which is continuously updating
    ans = m+h*sp.N(func.subs(x, i).subs(y, m))
    # formula above stated for the euler method which is (Yi+1=yi+hf(xi,yi))
    print("value of y is :")
    print(ans)
    m = ans
    # increment in the value of i according to the value assigned  by the user of H->which is basically the gap to maintain btw the limits.
    i += 0.5
