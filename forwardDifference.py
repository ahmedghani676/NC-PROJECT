# Python library for symbolic mathematics it gives function as sub symbols which make working with formulas ike 2x or sinx much more easier.
import sympy as sp
import math
from math import factorial, log as ln


# function basically access list2 and append its content in the templist,where multiple lists are being appended which is further being appended into list4
def addItemToTable(list4, count, list2):
    # where it will be printed out on the screeen.

    tempList = []
    for i in range(len(list2)):
        if(i < count):
            tempList.append("{:.5f}".format(list2[i]))
        else:
            tempList.append("")
    list4.append(tempList)


mainCount = 1
list1 = [] 				 # values of x
list2 = []				 # values of fx
list3 = []   		 	 	 # value of a0,a1,a2
# temp-list is being appended which has the multiple list computed through the table.
list4 = []

x = sp.symbols('x')

print("do u want to give values of f(X) or give a function\n")
# Program asks for both the choices to insert function
decis = int(input("1-value of fx   2-function "))
# or directly assign the values.
if(decis == 2):
    print("Enter the Function:")
    function = input()
val = int(input("enter how many value of x to be inserted\n"))
listTempCount = val
for i in range(val):
    k = float(input("enter values of x \n"))
    list1.append(k)
    if(decis == 1):
        functionvalue = float(input("enter value of fx"))
        list2.append(functionvalue)
    elif(decis == 2):
        symFunction = sp.sympify(function)
        solFunc = sp.N(symFunction.subs(x, k))
        list2.append(solFunc)
addItemToTable(list4, listTempCount, list1)
addItemToTable(list4, listTempCount, list2)
list3.append(list2[0])
temp = val
while (val > 1):
    for i in range(val-1):
        if(i == 0):
            a = list2[i+1]-list2[i]
            list3.append(a)
            list2[i] = a
        else:
            a = list2[i+1]-list2[i]
            list2[i] = a
    mainCount += 1
    val -= 1
    listTempCount -= 1
    addItemToTable(list4, listTempCount, list2)
strs = ''
for li in range(len(list4)-2):
    strs += str(li+1)+'DD\t\t'  # Headings like 1dd ,2dd are being generated.
print("x\ty\t"+strs)
for i in range(len(list1)):
    for j in range(len(list4)):
        # Table in its proper format  is being printed here.
        print(list4[j][i], end='\t')
    print('\n')
difference = list1[1]-list1[0]
count = 0
x = 0.0
print("Enter the function value :")
func = float(input())
ans = 0
p = (func-list1[0])/difference
print("P" + str(temp-1) + " = ")
counter = 0
# The whole for loop scope covers the logic or the equation to be used to take out
for i in range(len(list3)):
    # the final answer for the table with a function value assigned by the user
    if(i == 0):  # which will help in calculating the p->X-X0/H.
        ans += (list3[i]/factorial(i))
    else:
        temp = 1
        for j in range(counter):
            temp = temp*(p-j)
        temp = temp*list3[i]
        temp = temp/factorial(i)
        ans += temp
    counter = counter+1
print("The Ans is")
print("{:.5f}".format(ans))
