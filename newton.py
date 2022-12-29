import sympy as sp
from sympy import sympify, N
from math import exp as e
from math import log as ln


def NewtonMethod(point, func, deri):
    return point-(func/deri)


iterations = 0
print("Do you want to enter iterations if not enter 0:")
iterations = int(input())
if(iterations == 0):
    print("Enter the Epsilon val:")
    epsilons = input()
    index = epsilons.find("**")
    if(epsilons[index+2] == "-"):
        f = -1
        d = int(epsilons[index+3])
        epsilon = pow(10, f*d)
    else:
        d = int(epsilons[index+2])
        epsilon = pow(10, d)

print("Enter the main point of function:")
point = float(input())
iteration = []
x = sp.symbols('x')
print("Enter func:")
function = input()
function = function.replace("e**", "E**")
func = sympify(function)
deri = sp.diff(func)
# print(N(func.subs(x, 1)))
i = 0
error = 0
if(iterations > 0):
    for i in range(iterations):
        s = N(func.subs(x, point))
        d = N(deri.subs(x, point))
        point = NewtonMethod(point, s, d)
        iteration.append(point)
else:
    while True:
        s = N(func.subs(x, point))
        d = N(deri.subs(x, point))
        point = NewtonMethod(point, s, d)
        point2 = abs(point-error)
        if(point2 < epsilon):
            print("break")
            break
        iteration.append(point)
        error = point
for i in iteration:
    print(i)
