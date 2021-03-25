# nameAndAge.py 
# Name and Age is requested and calculation performed againsted the age
# Author: Amy Reynolds (Andrew Beatty - lab 2.2 - first programs)

name = input("enter your name:")
print ("Hello " + name)

# int - convert whatever is read in into an integer / convert the string thats input to an integer 
age = int(input ("enter your age:"))
print ("your age is {} " .format (age))
print ("your age is " + str(age))

# format function and tab separation 
print ("Hello {}, \tyour age is {}".format (name,age))

print ("Hello " + name + ", your age is " + str(age))

# Extra Calculations
x = 21
y = 4
print (21-4)

x = 2 
y = 3
print (x==y)
