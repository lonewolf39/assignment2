            #ASSIGNMENT 2

# Q.1- Print Something
print("Hello Sir Assignment Check Krlo")

# Q.2- Concatinate Strings
a=("Hello sir ")
b=("Assignment Check Krlo")
print(a+b)

# Q.3- Print 3 User Defined Variables
x=int(input("Enter first Variable: "))
y=int(input("Enter second Variable: "))
z=int(input("Enter third Variable: "))
print(x)
print(y)
print(z)

# Q.4- Print Let's Get Started
x=("Let's Get Started")
print(x)

# Q.5- Print The Given Values Using Placeholders
x=('LoneWolf')
y=('King')
z=(3939)
print("Name: %s , Aim: %s , Age: %d" %(x,y,z))

# Q.6- Find The area of circle with user defined Radius
r=float(input("enter the radius"))
pi=3.14
a=pi*(r**2)
print("area of circle:" ,a)


                     #ASSIGNMENT 3
                    #ASSIGNMENT 3
                    #ASSIGNMENT 3
                    #ASSIGNMENT 3


# Q.1- Create a list
l1=[]
a=int(input("Enter no. of integers"))
print(" Enter elements")
for i in range(a):
    x=int(input())
    l1.append(x)
print(l1)

# Q.2- Concatinate Lists
l2=['Dragon Ball','Hunter X Hunter','Fairy Tail']
l1.extend(l2)
print(l1)

# Q.3- Count the Occurance in a list
l3=[1,2,3,3,4,5,6,7,8,9,9,8]
print(l3.count(3))

# Q.4- Sort the List
l4=[10,11,1,5,44,5,8,39]
l4.sort()
print(l4)

#Q.5- Conctinate and sort 2 sorted arrays
l5=[2,3,5,64,56]
l6=[34,65,23,23,45]
print("sorted list: ",l5)
print("sorted list: ",l6)
l5.extend(l6)
print("merged: ",l5)
l5.sort()
print(l5)

#Q.6- Count Even and Odd numbers in a list
c1=0
c2=0
for i in l5:
    if(i%2==0):
        c1+=1
    else:
        c2+=1
print(c1)
print(c2)

#Q.7- Print a Tuple in reverse order
l7=[]
y=int(input("Enter Element"))
print("Enter integer")
for i in range(y):
    z=int(input())
    l7.append(z)
c3=tuple(l7)
print("tuple is:", c3)
r=reversed(c3)
print(tuple(r))

#Q.8- Find largest and smallest element of tuples
l8=[]
y=int(input("Enter Element"))
print("Enter integer")
for i in range(y):
    z=int(input())
    l8.append(z)
c3=tuple(l8)
print(max(c3),min(c3))

#Q.9- Convert a string to uppercase
s=(input("enter string\n"))
print(s.upper())

#Q.10- check if the string contains all numeric characters
s=(input("enter string\n"))
c=0
for i in range(len(s)):
    if s.isdigit():
        c=1;
    else:
        c=0;
        break;
if c==1:
    print("True")
else:
    print("False")

#Q.11- Replace the given string with your name
s=("Hello Sir")
print(s.replace("Hello Sir","Lonewolf"))
