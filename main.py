#Building your own function
def plusone(a):
    """add 1 to a"""
    b=a+1
    return b
#Using your function
print(plusone(6))

help(plusone)
#build functions with multiple parameters
def Mult(a,b):
    c=a*b
    return c
#Using your function

print(Mult(30,10))

#You can also multiply strings, but this is not recommended.
print(Mult(3," Hello world Hello"))

#Print strings in your functions
def CS():
    print('Computer Science')

CS()

#Create empty functions. Only allowed with the pass keyword, else it fails to run given the empty body.
##This will print a "None" object.

def Empt():
    pass

print(Empt())

#You can clearly see what the return function does in this example.
def Ftest(a):
    b=a+1
    print(a,"plus one equals", b)
    return b
Ftest(3)

#You can use loops in functions
##First we define our loop function
def looptions(som):
    for i,s in enumerate(som):
        print("Game", i, "is ranked:", s)

game_ratings=[8,5,10]

looptions(game_ratings)

#The following function contains a Variadic parameter, that allows us
##to input multiple elements

def GameName(*names):
    for name in names:
        print(name)

GameName('Dark Souls','Mario 64', 'Fallout 3')

#You can set the scope of a function to global. Then, the element after the keyword global will be stored
## in the global enviroment


def Mario():
    global Date
    Date=1990
    return Date

Mario()

print(Date)