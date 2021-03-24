# Uses a variable to greet 
# Author: Amy Reynolds (Andrew Beatty) - prog 2.2.1 - First programs lab

name = "Andrew"
print ("hello " +  name )

# this won't work - age value will not print only the word "age" - syntax error Ln # 9 - can only concatenate str (not "int") to str
age = 34 
# print ("your age is " + age) 
# use str - convert values to a string in python - Ln 11
print ("your age is " + str(age))  
# called the function format  
# \t - tab 
print ("Hello {} \tyour age is {} " .format (name,age))
