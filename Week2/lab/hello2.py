# hello2.py 
# display a personalised greeting
# Author: Amy Reynolds (Andrew Beatty - lab 2.2 - first programs)

name = input ("enter you name:")
print ("Hello " + name)
# Using \t to create tab separation for greeting 
print ("Hello \t nice to meet you " + name)
print ("Hello "+ name +"\t nice to meet you ")

# Using \n to create new line for greeting 
print ("Hello \nNice to meet you " + name)
print ("Hello " + name + "\nNice to meet you ")

# format function
print ("Hello {} ".format (name))

# format function - tab separation for greeting 
print ("Hello {} \tNice to meet you " .format (name))

# format fucntion - new line separation for greeting
print ("Hello {} \nNice to meet you " .format (name))