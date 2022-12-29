# Python library for symbolic mathematics it gives function as sub symbols which make working with formulas ike 2x or sinx much more easier.
import sympy as sp
mainCount = 1
list1 = []  				# values of x
list2 = [] 				 # values of fx
list3 = []  # value of a0,a1,a2
list4 = []
x = sp.symbols('x')


def addItemToTable(list4, count, list2):
    # where it will be printed out on the screeen.

    tempList = []
    for i in range(len(list2)):
        if(i < count):
            tempList.append("{:.5f}".format(list2[i]))
        else:
            tempList.append("")
    list4.append(tempList)


print("do u want to give values of f(X) or give a function\n")
# choice given to the  user to enter a function or enter the values directly.
decis = int(input("1-value of fx   2-function "))
if(decis == 2):
    print("Enter the Function:")
    function = input()
val = int(input("enter how many value of x to be inserted\n"))
tableTempCount = val
for i in range(val):
    k = float(input("enter values of x \n"))
    list1.append(k)
    if(decis == 1):
        functionvalue = float(input("enter value of fx"))
        list2.append(functionvalue)
    elif(decis == 2):
        symFunction = sp.sympify(function)
        # values of x being stored in the solFUNC
        solFunc = sp.N(symFunction.subs(x, k))
        list2.append(solFunc)
addItemToTable(list4, tableTempCount, list1)
addItemToTable(list4, tableTempCount, list2)
list3.append(list2[0])
temp = val
while (val > 1):
    count2 = 0
    count3 = mainCount
    for i in range(val-1):
        if(i == 0):
            # f(Xi+1)-f(Xi) takes place which is further divided by difference of x values to yield 1DD,and the whole process foloowws again to yeild 2DD,3DD etc.
            a = list2[i+1]-list2[i]
            b = list1[count3]-list1[count2]
            c = (a/b)
            list3.append(c)
            list2[i] = c
        else:
            count3 += 1
            count2 += 1
            a = list2[i+1]-list2[i]
            b = list1[count3]-list1[count2]
            c = (a/b)
            list2[i] = c
    mainCount += 1
    val -= 1
    tableTempCount -= 1
    addItemToTable(list4, tableTempCount, list2)
strs = ''
for li in range(len(list4)-2):
    strs += str(li+1)+'DD\t'  # Headings like 1dd ,2dd are being generated.
print("x\ty\t"+strs)
for i in range(len(list1)):
    for j in range(len(list4)):
        # Table in its proper format  is being printed here.
        print(list4[j][i], end='\t')
    print('\n')


x = 0.0
# Function value is being asked by the user on which we will generate the formula and insert its value to find the output.
print("Enter the function value :")
func = float(input())
print("P" + str(temp-1) + " = ")
# formula for P(1/2/3..) is being generated in which funct value will be inserted and then finally x will store its value and printed out.
for i in range(temp-1):
    c = 1.0
    if(i == 0):
        x += list3[i]
    elif(i > 0):
        j = i-1
        while(j >= 0):
            c = c*(func-list1[j])
            j -= 1
        k = list3[i]*c
        x += k

print("The Ans is")
print("{:.5f}".format(x))
