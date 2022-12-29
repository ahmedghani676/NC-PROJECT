import sympy as sp
# All math libraries used for mathemtical operations like a factorial used in the final eq to calculate the value at a given function value.
from math import factorial
from math import log as ln


# function basically access list2 and append its content in the templist,where multiple lists are being appended which is further being appended into list4
def addItemToTable(list4, count, list2):
    # where it will be printed out on the screeen.
    # print(1)
    tempList = []
    for i in range(len(list2)):
        if(i < count):
            tempList.append("{:.5f}".format(list2[i]))
        else:
            tempList.append("")
    list4.append(tempList)


mainCount = 1
list1 = []  					# values of x
list2 = [] 					# values of fx
list3 = []  					# value of a0,a1,a2
# temp-list is being appended which has the multiple list computed through the table.
list4 = []

x = sp.symbols('x')
#unction = "2*x"
print("do u want to give values of f(X) or give a function\n")
decis = int(input("1-value of fx   2-function "))
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
        list2.append(round(functionvalue,5))
    elif(decis == 2):
        symFunction = sp.sympify(function)
        solFunc = sp.N(symFunction.subs(x, k))
        list2.append(solFunc)
difference = list1[1]-list1[0]
# list have been reversed here to follow the rules of backward formula to make the calculations in an reverse order.
list1.reverse()
# we decided as a grp that in backward the last elements of a list is used so we can use python reverse func to easily solve this issue.
list2.reverse()
addItemToTable(list4,listTempCount,list1)
addItemToTable(list4, listTempCount, list2)
list3.append(list2[0])

temp = val
while (val > 1):  # list3 values are being computed here which is the (Delta Y,Y^2,Y^3....)
    for i in range(val-1):
        if(i == 0):
            a = list2[i]-list2[i+1]
            list3.append(round(a, 5))
            list2[i] = round(a, 5)
        else:
            a = list2[i]-list2[i+1]
            list2[i] = round(a, 5)
    mainCount += 1
    val -= 1
    listTempCount -= 1
    addItemToTable(list4, listTempCount, list2)
for temp in range(len(list4)):
    list4[temp].reverse()
strs = ''
for li in range(len(list4)-2):
    strs += str(li+1)+'DD\t\t'  # Headings like 1dd ,2dd are being generated.
print("x\ty\t"+strs)
for i in range(len(list1)):
    for j in range(len(list4)):
        # Table in its proper format  is being printed here.
        print(list4[j][i], end='\t')
    print('\n')

print("Enter the function value :")
func = float(input())
ans = 0

p = float((func-list1[0])/difference)
print("P" + str(temp-1) + " = ")
counter = 0
for i in range(len(list3)):  # The whole for loop scope covers the logic or the equation to be used to take out the final answer for the table with a function value assigned by the user
    if(i == 0):  # which will help in calculating the p->X-X0/H.
        ans += (list3[i]/factorial(i))
    else:
        temp = 1
        for j in range(counter):
            temp = temp*(p+j)
        temp = temp*list3[i]
        temp = temp/factorial(i)
        ans += temp
    counter = counter+1
print("The Ans is")
print("{:.5f}".format(ans))
