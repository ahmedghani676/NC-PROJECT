import sympy as sp  			#Python library for symbolic mathematics it gives function as sub symbols which make working with formulas ike 2x or sinx much more easier.

from math import log as ln       	#for mathematical operations


def Lagrange(lists, j, solvedFunc):     #Gives out the ans and formula
    return (lists/j)*solvedFunc

pointStored = []
x = sp.symbols('x')
function = input()
function = function.replace("e*", "E*")
symFunction = sp.sympify(function)
print("Enter main point:")                  #Take the users function value assigned
point = int(input())
print("Enter the no of points you want to Enter:")  #Asks for the no of points from which user will select x values.
count = int(input())
print("Enter the "+str(count)+" points:")
for i in range(count):
    pointStored.append(float(input())+0.0)
ans = 0.0
temp3=1
temp4=1
for i in range(count):						#Lagrange formula will be generated according to the number of points given
    solFunc = sp.N(symFunction.subs(x, pointStored[i]))  	#F(x0,x1,x2...) values are being stored in the solfunct which are being substituted against x.
    for j in range(count):
        if(i != j):
            temp1=point-pointStored[j]
            temp2=pointStored[i]-pointStored[j]
            temp3=temp3*temp1
            temp4=temp4*temp2
    ans = ans+Lagrange(temp3, temp4, solFunc)
    temp3=1
    temp4=1
print("The Ans is")
print("{:.5f}".format(ans))#We are restricting the output to 5 decimal places in all the questions