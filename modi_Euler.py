# Python library for symbolic mathematics it gives function as sub symbols which make working with formulas ike 2x or sinx much more easier.
import sympy as sp
from math import log as ln  # for mathematical operations.

print("Enter the lower limits:")
a = float(input())
print("Enter the upper limit")
b = float(input())
print("enter the value of h")  # gap btw the limits assigned
h = float(input())
# value of x0 and y0 assigned by the user
print("enter the initial value of t and the y value")
c = float(input())
m = float(input())
print("value of y is:")
print(m)
x = sp.symbols('x')
y = sp.symbols('y')
function = input()
function = function.replace("e*", "E*")
print(function)
func = sp.sympify(function)
i = a

while True:
    if i == b:  # if value of i which is in this case the lower limit assigned by the user,becomes equal to the lower limit it will break.
        break
    k1 = h*sp.N(func.subs(x, i).subs(y, m))               # k1=hf(ti,wi)
    k2 = h*sp.N(func.subs(x, i+h).subs(y, m+k1))           # k2=hf(ti+1,wi+k1)
    answer = m + (1/2*(k1+k2))				 # wi+1=wi+1/2(k1+k2)
    # above stated formulas will be used to devise the answer for the modified euler eq
    print("value of y is :")
    print(answer)
    m = answer  # answer will be printed.
    # increment in the value of i according to the value assigned  by the user of H->which is basically the gap to maintain btw the limits.
    i += 0.5
