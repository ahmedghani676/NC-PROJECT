# Python library for symbolic mathematics it gives function as sub symbols which make working with formulas ike 2x or sinx much more easier.
import sympy as sp
from sympy import sympify, N
from math import exp as e
from math import log as ln


# Formula to calculate the iteration value [Pn-f(Pn-1)/f'(Pn-1)]
def NewtonMethod(point, func, deri):
    return point-(func/deri)
    d = int(epsilons[index+2])
    epsilon = pow(10, d)


iterations = 0
# iterations ask from user
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
# sp.diff is used to find the derivative of the function which will be further used in the eq.
deri = sp.diff(func)
# print(N(func.subs(x, 1)))
i = 0
error = 0
if(iterations > 0):
    list4 = []
    points = []
    for i in range(iterations):
        points.append("{:.5f}".format(point))
        s = N(func.subs(x, point))
        d = N(deri.subs(x, point))
        point = NewtonMethod(point, s, d)
        # iteration answers are being appended in the iteration list
        iteration.append("{:.5f}".format(point))
    list4.append(points)
    list4.append(iteration)
    print("points\t   iterations")
    for i in range(len(points)):
        for j in range(len(list4)):
            # Table in its proper format  is being printed here.
            print(list4[j][i], end='\t')
        print('\n')
else:
    list4 = []
    points = []
    errors = []
    while True:
        points.append("{:.5f}".format(point))
        s = N(func.subs(x, point))
        d = N(deri.subs(x, point))
        point = NewtonMethod(point, s, d)
        point2 = abs(point-error)
        if(point2 < epsilon):
            print("break")
            break
        iteration.append("{:.5f}".format(point))
        error = point
        errors.append("{:.5f}".format(error))
    print("points\titerations\terrors")
    for i in range(len(points)):
        for j in range(len(list4)):
            # Table in its proper format  is being printed here.
            print(list4[j][i], end='\t')
        print('\n')
