#Content
##Functions

##Exception handling
###Try...Except statement
###Try...Except...Else statement
###Try...Except...Else...Finally statement

#Types and classes in Python
##Creating your own class
##Data attributes
##Methods

#Downloading, Reading and opening data in Python
##Download
##Reading
###Read method
###Readline method
###Readlines method
##Writing
##Appending

#Pandas
##Importing Pandas
##Reading excels with pandas
##Working with excels in pandas

#NumPy
##NumPy array or ND in one dimension
###Assigning values
###Slicing ND arrays
###Other ND attributes
##Useful NumPy tools for Data science
###Vector addition
###Vector broadcasting
###Mean of the elements
##Math functions
##Linspace

##2 Dimension NumPy array or ND

#APIs
##Definition and types
##Examples of APIs
###PyCoinGecko

#Requests Module

#Web Scraping
##Beautiful Soup objects and how to browse through them
###Tags
###Children, Parents and siblings
###Navigable String
##Filters
###find all filter
###find filter
###HTML Attributes
###Navigable strings
##Downloading and Scraping the contents of a Web Page

#How to work with tidfferent file formats
##csv, xml, json, xlsx





######If you're using PyCharm, you can select the chunk of code and run it by pressing alt+shift+e.
######Remember to import the libraries when necessary. At least in PyCharm, you will


                                        #####Functions#####
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

GameName('Dark Souls','Mario 64', 'Zelda: Ocarina of Time')

#You can set the scope of a function to global. Then, the element after the keyword global will be stored
## in the global enviroment


def Mario():
    global Date
    Date=1990
    return Date

Mario()

print(Date)

                        #######Exception Handling.#######
#I.E: entering numbers in a only letter input field and an error code and/or message

# The Try...Except statement will "Try" to execute its code block, but when an error occurs,
## the "except" code will run and do the exception handling once the program reaches the exception that matches
### and run the code. It should print an error message related to the specific error. You may add multiple
#### exceptions with different error codes and messages. Exceptions can be seen while you use Python I.E.
####dividing by 0 (try running: 1/0)

t=1
try:
    b=int(input("Please enter a number to divide t"))
    t=t/b
    print("Accepted. t=", t)
except ZeroDivisionError:
    print("You can't divide by 0")
except ValueError:
    print("You should only provide numbers")
except:
    print("Not a valid input")
# Try...except...else will give you the opportunity to execute another block of code if there was no exception
##or error on your code
F=2
try:
    d=int(input("Please enter a number"))
    F=F/d
    print("The new value for F is", F)

except ZeroDivisionError:
    print("You cant divide by 0")

except ValueError:
    print("Please enter a number")

else:
    if(F<1): #For more info on this one, check the else if and else elif statements.
        print("F is smaller than one: F=", F)
    elif(F>1):
        print("F is larger than 1: F=", F)
    elif(F==1):
        print("F is equal to 1: F=", F)



# If you want something to happen after the code has been executed, you can use the "Try...Except...
## Else...Finally" Statement. I.E: closing the file after it has been edited.
G=5
try:
    H=int(input("Please enter a number"))
    G=G/H
except ZeroDivisionError:
    print("You can't divide by 0")

except ValueError:
    print("Please enter a number.")
else:
    if(G<1):
        print("G is smaller than one. G is equal to:", G)
    elif(G>1):
        print("G is bigger than one. G is equal to:", G)
    elif(G==1):
        print("G is equal to 1. G=", G)
finally:
    print("Thank you for joining me in my exception handling coding.")

#Types in Python: There are many. I.E: integer, float, String, List, Dictionary, Boolean. Every time we create any of these
##you create a instance or Object of that type. You can use the type() command to find the type of your object.
type(3)

#For every type, theres a Method you can use with that class of object. Methods are functions that a class or type
##provide. It is the way you can interact with the data. One example of this, is the sort method.

ratings=[3,2.0,3.2,5.7,8.2,3,10]
print(ratings)
ratings.sort()
print(ratings)

#There's another common method: the reverse method.
print(ratings)

ratings.reverse()

print(ratings)

                                            #####Classes#####

# You can create your own types or classes
## You first create a class, then assign attributes and methods to it.
### For example, a Circle has a radius attribute.
#### To create a new class: First, you declare you want to create a new class, then the name of the class
##### and finally the class/type parent. Then, you have to define attributes, in this case radius and we'll add color too.
###### The init function tells Python you are creating a new class. The self parameter indicates the new
####### instance/object created with its class. Self will contain all the data attributes of the object.

class Circle(object ):
    def __init__(self, radius, color):
        self.radius=radius;
        self.color=color;

#We will now create a new class called rectangle, contained in its parent class, object

class Rectangle(object ):
    def __init__(self, color ,height, width):
        self.color=color;
        self.height=height;
        self.width=width;

#Now we create objects with the new classes created. We call the code by using the class name and then we have to
##input its attributes between parenthesis.

BlueCircle= Circle(10,"red" )
GreenRectangle= Rectangle("green", 5, 7 )

#You can also check the value of the attribute of each object/instance.

BlueCircle.radius

GreenRectangle.width

#You can also change their attributes

BlueCircle.radius=4

#Methods are the functions that interact and change attributes of the data.
## We can create a method to add radius to a circle:
class Ctest(object ):
    #Constructor
    def __init__(self, radius, color):
        self.radius=radius;
        self.color= color;
    #Method
    def add_radius(self, r):
        self.radius=self.radius+r
        return(self.radius)

Ctestred=Ctest(2,"red")
#To call the method, you have to input the name of the object, followed to the radius you'd like to add.
Ctestred.radius

Ctestred.add_radius(3)

Ctestred.radius

#You can get the attributes and methods of a class with the dir() function
dir(Ctest)


                                    ####Files in Python#####

#Downloading files:
import urllib.request
    url= 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
    filename='Example1.txt'
    urllib.request.urlretrieve(url, filename)


#There are two different ways to open a file. The second one is better practice, because it runs the code
##and then it closes the file again.

#First, we'll use the open command by itself to create the file object. Then we will check the name of the file
##with the data name attribute as well as the mode the file is open in with the mode data attribute. Remember
###To always close the file after opening it to avoid further problems and free resources.
example1= 'Example1.txt'

File1 =open('Example1.txt', "r")

#Data attribute name
File1.name

#Data atribute mode
File1.mode

#Reading the object content.
objectcontent = File1.readlines()
print (objectcontent)
objectcontent
#Object method close
File1.close()

#Now we will use the with statement. This code will run everything within the indent. In this case, we will print
##the file content, after using the read method.
with open('Example1.txt') as File1:
    file_stuff=File1.read()
    print(file_stuff)
    File1.mode
    File1.name

print(file_stuff)

#If you input a number in the read method, you will get the first X characters of the file. As input more read methods,
##the script will read the next characters in the next line.
with open('Example1.txt') as File1:
    print(File1.read(4))
    print(File1.read(10))
    print("'Custom message.'", File1.read(20))


#You can create loops to iterate the code in every line.

with open('Example1.txt', 'r') as File1:
    i=0
    for line in File1:
        print('iteration number ', (i+1), line)
        i=i+1

#And we can save the values of the file as a list:
with open('Example1.txt') as File1:
    MyList= File1.readlines()

MyList[0]

#Writing files with the open function and the write method:

with open('C:/Users/CrsTn/PycharmProjects/Repo_CTeufel/Example2.txt', "w") as File1:
    File1.write("This is the first new line \n")
    File1.write("This will be the second new line \n")

#You can also use the for loop to write lines:

Lines=['Line number one \n', 'Line number two\n', 'Line number three \n']

with open('C:/Users/CrsTn/PycharmProjects/Repo_CTeufel/Example2.txt', "w") as File1:
    for line in Lines:
        File1.write(line)

#Appending: uses an existing file to write in it. This will add the new line.

with open('C:/Users/CrsTn/PycharmProjects/Repo_CTeufel/Example2.txt', "a") as File1:
    File1.write("Line number four \n")

#You can copy one file into another one by using 'read' mode for the original file, then
##for the copied file, you use the 'write' mode

with open("Example1.txt", "r") as readfile:
    with open("Example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)

#To test if the files have been written correctly, use the print function
##within the with indent.
with open("Example3.txt", "r") as writefile:
    print(writefile.readlines())

with open ("example1.txt", "r") as readfile
    with open("Example3.txt", "w") as writefile:
    for line in readlines:
        writefile.write(line)


#We can also write in files without deleting older content with the append
##mode and the write method.

lines2=['This is line four \n', 'This is line five\n']
with open("Example3.txt", "a") as writefile:
    for line in lines2:
        writefile.write(line)

with open('Example3.txt', 'r') as writefile:
    print(writefile.read())

                                                #####Libraries######
                                                ######PANDAS#######

#Pandas is a library, popular for its pre-built classes and functions for data analysis. Libraries or dependencies
##contain codes to solve problems. We will ned the xlrd dependency to install pandas
!pip install xlrd

#Importing Pandas with the import command. We will use the as statement to shorten to make the library less tedious
##to call with. The new and common abreviation will be "pd". You can also leave the library without

import pandas as pd

#Panda allows you to work with data frames and its data. To load a csv file with Pandas as a data frame, we will use
##the read_csv method. The file used as an example is one provided to us for an R 'Business Intelligence' elective
###course during my last semesters in university. I've seen it over the internet, but I'm not sure who was the first
####to publish it. Credits to that person for it.

NoShows='No shows.csv'
df=pd.read_csv(NoShows)

type(df)

#Read the headers of the data frame with the columns function
print(df.columns)

#We can make different Data frames with the values of a specific column like this:

dfgender=df[['Gender']]
##Note: when using double brackets, one will get the data in a dataframe. With one bracket, you will get a series.

#To check unique values, we can apply the method unique()
print(df['Gender'].unique())

#We could also get information out of this data frame. For example, we can count people per gender.
dfgender.value_counts(['Gender'])
df.value_counts(['Gender'])


#If we want to get all the rows with people of gender F in a new data frame, we can use the following code

df_f=df[df['Gender']=='F']

#This is a new data frame
df_f['Gender'].unique()

#To save this new data frame as a .CSV, we use the to_csv file like this
df_f.to_csv('df_females.csv')

#You can access the first, second or any specific row and column one would want to retrieve with the iloc method.
##If you ask yourself where the name of the method comes from, I'm also not sure, but I believe and have read
###it comes from integer location, therefore it only works with integers that represent the coordinates you want to call.
####There is also the 'loc' function, that works with strings, like the column name.
df.iloc[0, ] ##First row

df.iloc[0,0] ##First row, first column

df.iloc[1,5] ##second row, fifth column

#The loc method also supports names>
df.loc[20, 'PatientId']

#You can also take slices of the sample with both methods. Remember, when slicing with the """iloc""" method,
##one will get the index upper limit minus 1. Unlike iloc, the """loc""" method will count the upper limit if numbers
###used, ie, iloc[2:5, 1:3] will retrieve from row 2 to 4 and from column 1 down to 2. (Remember 0 is the first row/col)

df.loc[20:23, 'Age'] #from 20 to 23

df.iloc[0:2, 0:1 ] #from 20 to 21,



                                        ######NumPy#######
#Numpy is a library used for scientific computing and has advantages like its speed and memory. It is also the basis
## for panda.

#How to create a NumPy array
## A NumPy array or ND is similar to a list. It is normally fixed in size and every element is of the same type.

import numpy as np

a=np.array([0,1,2,3,4,])

#Let's check the type of this element
type(a)

#As you can see, it is a numpy.ndarray. One could also check the size and the number of dimension the array has with the
##.size and .ndim attribute. The shape attribute will indicate the size of the array in each direction in a tuple.
a.size
a.ndim
a.shape
#Just like lists, we can check the values in the array, starting by 0.

a[0]
a[1]

#ND arrays can also contain floats. One could see what kind of numbers the array contains with the 'dtype'. 'a' list
##contains 'int32' data or integers, while b list contains 'float64', as it contains float numbers.
b=np.array([10, 20.1, 3.5, 6.9, 5.6])

b.dtype
a.dtype

#Elements can be modified as follows. In this case, the first and the third element

b[0]=100.2
b[2]=3.6

#One can also slize ND arrays, just like lists. We will assign the new array to the letter c and we will retrieve
##the second to the third row.

c=b[1:4]
c

#And one can modify more than one value this way:
c[0:2]=23, 50
c

#Vector addition: NumPy arrays can be added as vectors in a very simple way. Just add them as you would do in simple math

d=a+b
d

#One is allowed to do a multiplication with a scalar as well:
e=d*2
e

#Hadamard product is the product between two vectors. This process is simplified by NumPy, as you'd need a function
##to do it manually, just like the scalar multiplication and addition.

f=a*b
f

#Another usefull tool is the dot product, that tells you how similar your vectors are.

dot_prod=np.dot(a,b)
dot_prod

#If you want to add a constant to every value, NumPy will make it easier. This property is called broadcasting
adding=np.array([4,2,1,3,5])
addingresult= adding+1
addingresult


#There are universal functions, which are functions that operate in ND arrays

#The mean of the elements is easily obtainable with the mean function
meanresult=addingresult.mean()
meanresult

#To find the maximum value, use the max method.

addingresult.max()

#NumPy contains pi number as well. We could notate values in radians using the np.pi function. There is also a sin
##function.
x=np.array([0, np.pi/2, np.pi])
x

y=np.sin(x)
y

#If you want to plot mathematical functions in a evenly spaced plot, you can use the linspace function, which returns
## spaced numbers in an interval. The num parameter determines the number of samples in the sequence.

np.linspace(-3,3, num=7)

import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi, 100)
y=np.sin(x)
plt.plot(x,y)
plt.show()

#Two dimensional NumPy arrays
##We will now create a 2D numpy array as follows
import numpy as np
import matplotlib.pyplot as plt

a=[[10, 13, 15], [20,23,25], [30,23,35]]
a
A=np.array(a)
A

#One can use the ndim attribute to get  the dimensions, shape attribute to get the size of every dim. and the size, which
## will obtian the number of elements in the array.
A.ndim
A.shape
A.size
type(A)
#Accessing elements in the array:
##Say we want the middle element in the last array we've created
##We can do it this way. As always, to get the row and column you want, you have to substract 1 from the actual index.
##We will also retrieve the third row completely one by one and the whole row by itself. See the results to understand.
####Hint: they're all the same after the first element obtained.

A[1,1]

A[2,0]
A[2,1]
A[2,2]

A[2]

A[2,0:3]
A[2][0:3]


#Adding, multiplying two arrays or :
##NumPy simplifies the operations with arrays/matrix, because the attributes and functions is added in the
### numpy.ndarray class.
####First, we will need another array

b=[[1,2,3],[4,5,6],[7,8,9]]
B=np.array(b)
A+B

A*B

2*B

#In multiplication when using the * symbol, means that you will obtain the multiplication of M1(i1,j1) and
##M2(i2,j2) with i1=i2 and j1=j2

C=np.array([[1,2,3], [4,5,6]])
D=np.array([[9,8,7],[6,5,4]])
E=C*D
E

#Getting the multiplication of two matrix:
np.dot(A,B)
np.dot(C,D)
#This means, you're getting the dot product of every line and column.

#To get the transposed matrix, use the T attribute
E.T

                                ######## APIs #########

#What is an API? An API helps two different softwares communicate with each other through inputs and
##outputs. It stands for Application Program Interface For example, Panda.

#There are REST APIs as well. They let two different softwares communicate through the internet, which allows you to
##access many services that are not accessible off-line. RE stands for representational, S for State and T for transfer.
###They have rules regarding to them:
####1. Communication
####2. Input or Request
####3. Output or Response

#Example of APIs

##PyCoinGecko
!pip install pycoingecko
from pycoingecko import CoinGeckoApi
cg=CoinGeckoApi()


                                           ####HTTP Protocol#####
#It is a protocol for transferring information through the internet. The REST APIs send a request communicated via HTTP
##Message. Normally, this HTTP message contains a JSON file. When you enter a Web Page, first, you send a request to
###the web server. If it arrives successfully, the server will give a response, usually by default in "index.html"

#The uniform resource locator or URL is the link to the resources on the web. It's three parts are:
## Scheme: The protocol. I.E http://
##Internet Address or base URL. I.E www.google.com
##Route: It is the location on the web server. I.E /images/IDSNlogo.png



                                    #######Requests library########
import requests

#We will use the solotodo webpage to check on prices when the knowledge is enough. First, we need to create
##an object for the URL and use the get function. Then we will check the responses of the server.
url='https://www.solotodo.cl'
r= requests.get(url)
r.status_code                   ##200 stands for ok
stbody=r.request.body
stheaders=r.headers
r.encoding

stheaders['date']


#The GET request is used to modify the request of the query. We will use httbin.org, which is a simple HTTP Request
##and Response service. The GET request is used to retrieve information from a source.
url_get='http://httpbin.org/get'
payload={"name": "Joseph", "ID":"123"}

r=requests.get(url_get, params=payload)
r.url
r.request.body
r.status_code
r.text
r.headers['Content-Type'] #Checking the type of data
r.json() #Reading the data in the data type it is formated in.

#The POST request is similar to the GET request. The main difference is, you will get the response in the body, which
##was usually empty in the GET request. The post request is used to insert or update data. The HTTBIN service will send
###Back the "posted" info or sent data  in the body of the request.

url_post= "http://httpbin.org/post"
payload={"name":"Carsten","ID":"123"}
r_post= requests.post(url_post, data=payload)

#As we can see, the requested info is the get request, but not in the post request.
r.url
r_post.url

r.body
r_post.body

                                    ########Web Scraping###########

#This are the APIs we will be utilizing for Web Scraping. Web Scraping helps the coder retrieve information and data
##from a certain Web Page. This is useful when one is in need of large for data analysis pieces of data or
### information that is constantly updated from a web page

from bs4 import BeautifulSoup
import requests

#One can store HTML code in a string. The following HTML code was created by the Cognitive Lab

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

#To parse and analyze the html code, the BeautifulSoup API is useful. This API will transform the data into a complex tree
##of Python objects.
bkbsalaries= BeautifulSoup(html,'html5lib')

#If you'd like to get the HTML in the nested structure displayed, use prettify method.
print(bkbsalaries.prettify())

#Say, we are retrieving title of the page and the name of the top paid player from the HTML code.

tag_object=bkbsalaries.title
print(tag_object) #This is the page title.
type(tag_object) #As we can see, the object is a Beautiful Soup 4 object.

mostpaid= bkbsalaries.h3
print('The top paid player is', mostpaid)

#We can access child objects navigating down the branches of the tag_object. In this case we will navigate to the
##next bold object.

tag_child=mostpaid.b
print(tag_child)

#Then, we can navigate to the parent object with the parent attribute
parent_tag=tag_child.parent
parent_tag

#This is the same as
mostpaid

#To access the next sibling object, use the next_sibling att

sibling_1=mostpaid.next_sibling
sibling_1

sibling_2=sibling_1.next_sibling
sibling_2


#In the case of our HTML code, there is an id "boldest" in it. To access this id, treat the object like a dicionary or
##use the attrs attribute.

tag_child['id']

tag_child.attrs

#Or you could use the get method
tag_child.get('id')

#A string is the piece of text within the tag. NavigableString class contains text. To obtain the text or string within
##the tag, use the .string att
tag_string= tag_child.string
tag_string
#Check the type. It is a NavigableString by bs4 API

type(tag_string)

#The only difference between this object and a str python object, is that the NavigableString suppors some BeautifulSoup
##features. You can convert this NavigableString to a python string using the str function
pythstring= str(tag_string)
pythstring

#Now we will use tables. First, our table element. This one was also created by Cognitive class (thanks to them again)
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"

#Then, we will transform this HTML table into a Beautifulsoup table

table_bs=BeautifulSoup(table,'html5lib')

#To search through a code and extract specific tags

table_rows=table_bs.find_all('tr')
table_rows[0] #this are the headers of the table for the first second and third existing columns.
type(table_rows)

#To obtain the child of the first header, in this case the table data (td) in the first column of the header,
## use the td attribute.

t_headers=table_rows[0]
t_headers.td

#One could iterate through the table to display, in our example, all the first column values with the for... in loops
for i,row in enumerate(table_rows):
    print('This is row',i,'.', ' Code:', row)


#row is a cell object within the HTML table. To get all the cell data we use the following code
table_data= table_bs.find_all('td')
print(table_data)

#This might look a little complex to read, so we'll make it more human-friendly with a for...in loop to give it a check.

for i,row in enumerate(table_rows):
    print("row", i)
    cells=table_bs.find_all('td')
    for j, cell in enumerate(cells):
        print('column',j, 'cell', cell)

#To match cells within a same row, we can use the following code.
list_input=table_bs.find_all(name=['tr','td'])
list_input

#If we want to be more specific when searching for something in an HTML code, we can search for attributes in tags. For
##example, the first td elements have an id=flight. To search for these we do the following thinga

table_bs.find_all(id='flight')

#We could search for specific clickable links too (href)
table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")

#Or we can check for any tag specific content by using true or false boolean values
table_bs.find_all(href=True)

#Then, we can use the string attribute when looking for specific strings

table_bs.find_all(string="Texas")

#While the find_all method searches for a value in every line within a document, the find method will find only the first
##element with the input. We will use two tables for this example (Ty cognitivelabs uwu). We will store their HTML
###code within the two_tables object

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"


#Then we create a Beautiful Soup object with these two tables

rocketsnpizza=BeautifulSoup(two_tables,'html.parser')

#Now to search for the first table, we can use the find function

rocketsnpizza.find('table')

#To add more than to variables to our 'find' search, we can do so like this:
two_tables_bs.find("table",class_='pizza') #As we used 'class' word related to the HTML code, we add the underscore
##to make Python understand we're not meaning the keyword from Python (class)


#Now we are going to check how to download an scrap content of a Web Page
import requests
from bs4 import BeautifulSoup
url='http://www.falabella.com'

#To download the content of the webpage in text format, we use get.
data_falabella= requests.get(url).text

#Then we create a Beautiful Soup object for the Falabella Webpage
data_fb_bs= BeautifulSoup(data_falabella,'html5lib' )
#To get all the links, for example
for link in data_fb_bs.find_all('a', href=True):  #'a' stands for anchor or link.

    print(link.get('href'))

#Scraping the images of the page

for link in data_fb_bs.find_all('img'):
    print(link)
    print(link.get('src'))

#This source has a table about colors, their names and codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

#Again, we want the code displayed as text

data_table=requests.get(url).text

#Then we transform it to a BS object
table_color_bs=BeautifulSoup(data_table,'html5lib')

#Scraping data form an HTML table
table_html=table_color_bs.find('table')


#To retrieve all the rows, we do the following

for row in table_html.find_all('tr'): #tr stands for table row. First we need every row, then we extract the column
    #now we want to get all columns in every row. A cell or column is contained within the td or table data tag
    cols=row.find_all('td')
    color_name=cols[2]
    hex_code=cols[3]
    print("{}--->{}".format(color_name,hex_code)) #The format method will let us get the name of the color and the color
                                                ###in their respective hex codes.



#Now, let's scrape data from HTML tables, then convert them into a DataFrame using BS and Pandas

import pandas as pd

url = "https://en.wikipedia.org/wiki/World_population" #This url contains info about the population in the world

world_data = requests.get(url).text

world_data_bs=BeautifulSoup(world_data, 'html5lib')

wd_table=world_data_bs.find_all('table') #HTML for table is table. EZ

#To check how many tables we've got, we can use the len method
len(wd_table)

#As an example, we will get the '10 most densely populated countries' table

for index, table in enumerate(wd_table):
    if ('10 most densely populated countries' in str(table)):
        table_index=index
print(table_index)

print(wd_table[table_index].prettify())
population_data=pd.DataFrame(columns=['Rank', 'Country', 'Population', 'Area', 'Density'])

for row in wd_table[table_index].tbody.find_all('tr'):
    col=row.find_all('td')
    if (col !=[]):
        rank=col[0].text
        country=col[1].text
        population=col[2].text.strip()
        area=col[3].text.strip()
        density=col[4].text.strip()
        population_data= population_data.append({'Rank':rank, 'Country':country, 'Population': population, 'Area':area, 'Density':density}, ignore_index=True)


population_data

#How to o scrape data from HTML tables into a DataFrame with BeautifulSoup and read_html, to make things easier.

dataframe_list = pd.read_html(url, flavor='bs4') #This function returns a list of data frames and we need to pick
                                                    #The one we need

len(dataframe_list)

population_data_read_html= pd.read_html(str(wd_table[5]), flavor='bs4')[0]

population_data_read_html


#How to scrape data from a HTML table into a Data Frame with read_html

dataframe_list=pd.read_html(url, flavor='bs4')

len(dataframe_list)

dataframe_list[5]


#Finally, we can use the match parameter to retrieve a specific table. When the table contains the provided string,
##it will be read

pd.read_html(url, match='10 most densely populated countries', flavor='bs4')[0]

                                ######Data Engineering#####

#One of the critical and basic skills of any Data Scientist is Data Engineering.
#The three steps in Data Engineering are known as ETL, that stands for:
#1. Extract - This is the step where the information is gathered from multiple sources, which can be in different file
    # formats, like JSON, CSV, XLSX, or others.
#2. Transform: This means to remove data that is not useful for analysis and to convert the data from different sources
    # from their format  to the same format for every source.
#3. Load: To load data inside a warehouse after the previous process.

                         ########How to work with different file formats#########

#there are different file formats like csv, xml, json, xlsx. Pandas will help us with this. To get the pandas API, we
##use the import function

import pandas as pd

#We can read json files too with the json API. First, we import, then we read. Remember to use the with open as command
##for opening the file then closing it. Json files are a file type similar to Python dictionaries.

import json

#For xml or extensible markup Language, we need two different APIs, since Pandas can not read this type of file.
##We will need the xml.etree.ElementrTree Api to do this.
import pandas as pd
import xml.etree.ElementTree as etree

tree=eetree.parse('fileExample.xml') #To read the file
root=tree.getroot()
columns=['Name', 'Phone Number', 'Birthday'] #To create the headers of the columns in the dataframe
df=pd.DataFrame(columns=columns) #We assign the headers to the Data Frame

for node in root:           #This loop will go through the document and collect the necessary info, for a later appending.
    name=node.find('name').text
    phonenumber=node.find('phonenumber.text')
    birthday=node.find('birthday').text

#This is how we read a csv file. First we need the PD API, then the file and finally we use the read_csv method

import pandas as pd
url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url)

df

#As the csv file contains no column names, we add them like this

df.columns=['First Name', 'Last Name', 'Location', 'City', 'State', 'Area Code']

df

#To select one column, we do this (I'm kinda tired of writing and this is the final part of the Course, so I'll be short)

df["First Name"]
type(df)
#To select different columns we use two brackets like this
df_2=df[['First Name', 'Last Name', 'Location']]
df_2

#The loc and iloc will help us with getting info from specific indexes.

df.loc[0] #First row
df.loc[[0,1,2], 'First Name'] #0th, 1ts and 2nd rows for the First name column



#The iloc uses the indexes based searching mmethod. We need to pass an integer index.

df.iloc[[0,1,2],0] #0th, 1st, 2nd row of the first column 'First Name'


#The transform function returns a self-produced dataframe with values it transformed after applying the parameters specified
##in the function. This is how it works

import pandas as pd
import numpy as np

df=pd.DataFrame(np.array([[0,1,2], [3,4,5], [6,7,8]]), columns=['a', 'b', 'c'])
df

#If we wanted to add 10 to every element in the dataframe, we can use the lambda function of python
df=df.transform(func=lambda x : x+10)
df

#Now we will find the square root for each element in the matrix.

result=df.transform(func=['sqrt'])
result


#JSON files or JavaScript Object Notation is a data interchange format with a lightweight. Easy for humans to understand
##and write.

#It is built on two structures:
    #1. A collection of name/value pairs, like dictionaries in Python. In different languages, this is known as object,
        #record, struct, dictionary, hash, table, keyed list or associative array.
    #2. An ordered list of values. This is usually known as an array, vector, list, or sequence

#JSON is a language-independent data format. Derived from Javascript, but many recent programming languages code to
##create and parse JSON formatted data and can be used in a diverse range of applications.

#Similar to dictionaries in Python, JSON uses string that contain values in a key-value mappings within {} brackets.
##The builtin package json in Python supports JSON code.

import json


#To write files in JSON:
##The concept usually used for the process of converting an object in a specific format suitabgle for web
### transmission is "Serialization".

#This is the dictionary we will use to transform into a JSON file. It was created by IBM and its cognitiveclass.

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

#To serialize in json, we can use the dump() function, wich converts the dictionary into a JSON file.
## The parameters are
    #1. dictionary- Name of the dictionary to convert
    #2. file pointer- which mode you will open it. Write, read or append, etc.

with open('person.json', 'w') as f:         #Serializing into a file
    json.dump(person, f)

#To create a JSON object from a dictionary, we use the json.dumps() to convert it.
## Its parameters are
    #1. dictionary- Name of the dictionary
    #2. indent- Number of units for indentation

json_object=json.dumps(person, indent=4) #Indent is the number of separations, we use this to make the code more readable

json_object


#To do the opposite and to read JSON to a file, we call it Deserialization and it uses the load function
## The only parameter it needs is the
    #1. File Pointer- Points to a JSON file

with open('sample.json', 'r') as openfile: #open a JSON file
    json_object=json.load(openfile) #reading the file

print(json_object)
print(type(json_object))


#To read a data from XLSX file. This file is known as a Microsoft Excel Open XML file format. Just another type of
##Spreadsheet file format. It is organized under cells and columns

import pandas as pd
import urllib.request

urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")
df = pd.read_excel("sample.xlsx")

df

#To read the XML file format. This format is known as  Extensible Markup Language. It uses tags to define objects.
##It is human-readable and machine-readable

#As Pandas include methods to read it, we can use the xml.eetree.ElementrTree to read it. It is built-in with Python.
##It will let us parse and create XML documents. It represents the XML doc as a tree, in which we can move across the nodes,
### that represent elements and sub-elements of the XML file.

import xml.etree.ElementTree as ET

#To create the file structure
employee= ET.Element('employee')
details= ET.SubElement(employee, 'details')
first= ET.SubElement(details, 'firstname')
second=ET.SubElement(details,'lastname')
third=ET.SubElement(details, 'age')
first.text='Carsten'
second.text='Teufel'
third.text='25'

#To write a XML file with the results
mydata1= ET.ElementTree(employee)
with open('new_example.xml', 'wb') as files:
    mydata1.write(files)



#To reading xml with the xml.etree.ElementTree method

import pandas as pd

import xml.etree.ElementTree as ET
import requests
url= 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml'
response= requests.get(url)

with open('Sample-employee-XML-file.xml', 'wb') as file:
    file.write(response.content)

#First, we need to parse the XML file and create a list of columns for our data frame, to later extract useful info
##from the XML file, then add it to a pandas Data Frame

#Example

tree=etree.parse('Sample-employee-XML-file.xml')

root= tree.getroot()
columns=['firstname', 'lastname', 'title', 'division', 'building', 'room']
dataframe=pd.DataFrame(columns=columns)
for node in root:
    firstname = node.find("firstname").text

lastname = node.find("lastname").text

title = node.find("title").text

division = node.find("division").text

building = node.find("building").text

room = node.find("room").text

dataframe = dataframe.append(pd.Series([firstname, lastname, title, division, building, room], index=columns),
                               ignore_index=True)

dataframe


#To save data, we can use the dataframe.to_csv()

dataframe.to_csv('employee.csv', index=False)

#To read a Image File, PIL will help. It's the Python Imaging Library, which provides python an interpreter with
##image editing capabilities.

from PIL import Image

import urllib.request

#To download the dataset

urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

#Reading the image
img=Image.open('dog.jpg')

display(img)


                                    ########Data Analysis########


import pandas as pd
path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv'
df=pd.read_csv(path)

print("The first 5 rows of the dataframe")
df.head(5)

#Dimensions of the dataframe
df.shape

#For statistical overview of dataset

df.info() #This will give you the column names, how many non-null rows there are and the Dtype or datatype


df.describe() #This is for basic statistical details, like percentile, mean, Std dev. When applied to series of strings
                #the result is others.


#To check for null values (missing values) Python has two methods: isnull() and notnull()

missing_data=df.isnull()
missing_data.head(5)
missing_data.shape

#To count for missing values in each column, we do the following:

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")



#To correct the data format, we need to check for dtypes or data types in the df

df.dtypes


#For visualization, we will use matplotlib and seaborn. Visualization is one of the best ways to get information and
##insight from the dataset.

import matplotlib.pyplot as plt
import seaborn as sns

labels='Diabetic','Not Diabetic'
plt.pie(df['Outcome']. value_counts(), labels=labels, autopct='%0.02f%%')
plt.legend()
plt.show()
