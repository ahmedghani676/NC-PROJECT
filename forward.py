# Python library for symbolic mathematics it gives function as sub symbols which make working with formulas ike 2x or sinx much more easier.
import sympy as sp


# Function to check forward diff and backward difference if function value and user value both are given
def forwardDiff(func, index, list, h):
    a = list[index]+h
    if a in list:
        indexs = list.index(a)
        return (func[indexs]-func[index])/h
    else:
        return "No"

# def backwardDiff(func,index,list,value,h):


# Function to check forward and backward difference if user input and a fucntion is given.
def forward(value, h, func):
    val = value+h
    a = sp.N(func.subs(x, val))
    b = sp.N(func.subs(x, value))
    c = (a-b)/h
    return c


points = []
print("Enter the number of value:")
values = int(input())
# Choice to user is given
print("1:Values and function values\n2:Values and function")
choice = int(input())
if(choice == 1):  # Forwad/Backward difference logic made with h+/h-
    forwards = []
    backward = []
    functionVal = []
    list4 = []
    print("Please enter values and functions\n")
    for i in range(values):
        points.append(float(input()))
        functionVal.append(float(input()))
    list4.append(points)
    list4.append(functionVal)
    h = points[1]-points[0]
    hBack = h*(-1)
    forwardDiff(functionVal, 0, points, h)
    for i in range(len(points)):
        forwards.append(forwardDiff(functionVal, i, points, h))
        backward.append(forwardDiff(functionVal, i, points, hBack))
    list4.append(forwards)
    list4.append(backward)
    strs = ''
    strs += 'Forward\tBackWard'  # Headings like 1dd ,2dd are being generated.
    print("x\ty\t"+strs)
    for i in range(values):
        for j in range(len(list4)):
            # Table in its proper format  is being printed here.
            print(list4[j][i], end='\t')
        print('\n')

else:
    forwards = []
    backward = []
    list4 = []
    print("Please enter values\n")
    for i in range(values):
        points.append(float(input()))
    list4.append()
    print("Please enter function:")
    function = input()
    x = sp.symbols("x")
    func = sp.sympify(function)
    h = points[1]-points[0]
    hBack = h*(-1)
    for i in range(len(points)):
        forwards.append(forward(points[i], h, func))
        backward.append(forward(points[i], hBack, func))
    list4.append(forwards)
    liist4.append(backward)
    strs = ''
    strs += 'Forward\tBackWard'  # Headings like 1dd ,2dd are being generated.
    print("x\ty\t"+strs)
    for i in range(values):
        for j in range(len(list4)):
            # Table in its proper format  is being printed here.
            print(list4[j][i], end='\t')
        print('\n')
