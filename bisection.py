import sympy as sp
from sympy import sympify, N
from math import exp as e
from math import log as ln
import os
iterations = 0
h=1;
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

print("Enter the 1 main point of function:")
point = float(input())
print("Enter the 2 main point of function:")
point2 = float(input())
iteration = []
x = sp.symbols('x')
print("Enter func:")
function = input()
function = function.replace("e**", "E**")
func = sympify(function)
i = 0
error = 0
if(iterations > 0):
    for i in range(iterations):
        c=float((point+point2)/2)
        # print("c="+c)
        s = N(func.subs(x, c))
        print(f'Iteration {h} \ta={point:.5f}\tb={point2:.5f}\t\tc={c:.5f}\tf(x)={s:.5f}\terror={abs(c-error):.5f}')
        iteration.append(c)
        if(s>0):
            point2=c
        elif s<0:
            point=c
        else:
            break
        # iteration.append(c)
        error = c
        h=h+1
else:
    while True:
        c=(point+point2)/2
        s = N(func.subs(x, c))
        print(f'Iteration {h} \ta={point:.5f}\tb={point2:.5f}\t\tc={c:.5f}\tf(x)={s:.5f}\terror={abs(c-error):.5f}')

        
        if(s>0):
            point2=c
        elif s<0:
            point=c
        else:
            break
        if(abs(c-error) < epsilon):
            break
        error = c
        h=h+1
        
# 
    