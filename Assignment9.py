import math
import string 
# #predefined modules used below
k=43.5
print("Original value of K =",k)
print("Ciel = ",math.ceil(k))
print("Floor = ",math.floor(k))
m=64
print("Original value of M =",m)
print("Square root of M =",math.sqrt(m))
w=[1,2,3,4,5]
print("Elements present in W : ",w)
print("Sum of all elements in W = ",math.fsum(w))
print("------------------------------------------------------")


# #user defined module its functions present in my_module.py file
# #using * provides access to all functions present in file usage without importing individually
add=5
subtract=5
multiply=10
divide=20
print("* Provide Values and get its addition,subtraction,division,multiplication *")
a = int(input("Enter value of A : "))
b = int(input("Enter value of B : "))
print("Addition of A and B = ",add(a,b))
print("Subtraction of A and B = ",subtract(a,b))
print("Multiplication of A and B = ",multiply(a,b))
print("Division of A and B = ",divide(a,b))  #divide
print("---------------------------------------------------------")

string_concat=10
print("* Strings Module Functions *") # String calling 
x=input("Enter string1 : ")
y=input("Enter string2 : ")
print("Concate string successfully...")
print("result = ",string_concat(x,y))       #this is user defined

#storing the complete string in T
t=string_concat(x,y)
print("Converting into uppercase :",str.upper(t))
print("Converting into lowercase :",str.lower(t))

print("------------------")
fruits='mango orange apple jackfruit'
print("New String :",fruits)
print("Splitting a string when a space is detected...")
print(fruits.split())