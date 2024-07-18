
# STRING HANDLING

# userName = 'Honest'

# print(userName)

# a = 'suresh'
# b = 'ramesh'
# # print("before-->,"b)

# b = a
#  # print('after-->',b)

# a = "suresh"
# b = "ramesh"
# c = b
# b = a

# INDEXING

# Indexing - Getting the characters in the given string based on the index number
# Positive Indexing - Index with positive numbers - Example - print(name[0]) =s print(name[3]) =e
# Negative Indexing - Index with negative numbers - Example - print(name[-1]) =h print(name[-5]) =u
# name = "suresh"

# SLICING

# We can take some set of characters in this method or if we need 3 or 4 letters in the string, we can use this.
# We have to add extra 1 number to get the exact value
# If we need 3 characters means we have to mention 4, if we need 5 characters we have to mention 5.
# In positive slicing, if we have only 5 characters SURES - If we post more than 5 numbers, it will consider till the end.
# But in negative slicing it will not work, shows empty
# name = "suresh"
# print(name[0:8])
# print(name[-6:-1])

# RANGING

# We can take even to the last letter but in slicing it will not work.
# We we leave after collen empty, it will consider to the last letter.
# Example:
# print(name[0:])
# print(name[0:5])
# print(name[-5:-2])
# print(name[-4:])

# STRING FORMATTING

# Normal Formatting
# Manual Formatting
# Automatic Formatting


# name = "Honest"
# age = "24"
# emailid = "honestraj@gmail.com"

# Normal Formatting - CONCATENATION
# Adding two strings using + is called manual formatting.
# It is also called as Concatenation


# formatted = "my name is" + " " + name + " " + and my age is" + "24" + "and my email id is" + emailid
# print(formatted)

# AUTOMATIC FORMATTING

# In Automatic formatting, we dont need to add variables in the middle curvy brakets.
# It will automatically assingned in the brackets that what we assign in the last brackets before .format
# We must use .format in this method

# formater = "my name is {} and my age is {} and my email id is {}".format(name,age,emailid)
# print(formater)

# formatting = "my name is %s and my age is %s and my email id is %s".format(name,age,emailid)
# formatting = "my name is {name} and my age is {age} and my email id is {emailid}".format(name,age,emailid)



# MANUAL FORMATTING

# We can assign index numbers according to the variables that what we want.
# It will calculate variables according to the index number.
# We must add f in this method

# formatting = "my name is {1} and my age is {2} and my email id is {0}".format(emailid,name,age)
# print(formatting)


# name = "Honest"
# employeeid = "5091"
# dob = "1/9/1999"
# worklocation = "chennai"
# shift = "shift"

# details = f"My name is {name}. My employee id is {employeeid}. I was born on {dob}. I'm currently working in {worklocation} in day {shift}".format(name,employeeid,dob,worklocation,shift)
# print(details)

#-----------------------------------------------------------------------------------------------------------------

# String Built In Functions

# Capitalize - We can change first letter as Caps.
# Upper - We can change all letters in Caps.
# Lower - We can change all letters in Small.
# Title - We can change each words first letter as Caps.
# Swapcase - We can Swap Caps to Small and Small to Caps.
# Find - It shows index number of the specific letter. If the letters are more, it will show the first index number.
# Count - It counts the letters.
# Index - 
# Replace - We can replace letters and words.
# Isalpha - It shows True only when the Alphabets exits.
# Isnumeric - It shows the True only when the Numbers exits.
# Isalnum - It shows both Alphabets and Numbers exits.
# Startswith - We can check with letters or words starts with. If it is exits it shows True, if not it shows False.
# Endswith - We can check with letters or words ends with. If it is exits it shows True, if not it shows False.
# Strip, Lstrip, Rstrip:
# Strip - It removes both front and last spaces in the string.
# Lstrip - It removes front (leftside) space in the string.
# Rstrip - It removes last (right) space in the string.
# Partition - It seperates the letters and words and shows in the Tuple. 
# Split - It removes letter or words and shows the rest in the List.

# name = 'softlogic'
# name = name[1:]
# capword = 'S'
# name = capword + name
# name = "{}{}".format(capword, name)
# name = f"{capword}{name}"
# print(name)

# name = "  my Institute is Softlogic  "
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# name = name.title()
# name = name.swapcase()
# name = name.index()
# name = name.lstrip()
# nam3 = name.rstrip()
# print(name)


#name = "My Institute y is y softlogic"
#yIndexnumber = name.find("y")
#yIndexnumber = name.find('x')
#yIndexnumber = name.index('x')
#yIndexNumber = name.find('x')

# print(yIndexnumber>=1)
# print(yIndexnumber!=-1)

#name = "My Institution isy Softlogic"
# counter = name.count("y")

# name = " My Iynstitution is Soyftlogic "
# gen = name.replace("y", "@")
#gen = name.lstrip()
#gen = name.rstrip()
#gen = name.replace(" ","")

#name = 'HonestRaj2711'
#gen = name.isalpha()
#gen = name.isnumeric()
#gen = name.isalnum()
#print(gen)

#name = "softlogilc is my"
#gen = name.partition('l')
#gen = name.partition('x')
#gen = name.split('l')
#gen = name.split(' ')
#print(gen)

name = "my-institute-is-softlogic"
#remove the hifen and slice from second letter upto tenth letter
# and then add underscore on middle...and show output and show the length aso

# gen = name.replace("-","")
# gen = (gen[1:11])

# firsthalf = gen[0:5] 
# secondhalf = gen[5:]
# name = f'{firsthalf}_{secondhalf}'
# print(name,len(name))

name = name.replace("-","")[1:11]
firsthalf = name [:len(name)//2]
secondhalf = name[len(name)//2:]
name = f"{firsthalf}_{secondhalf}"
print(name,len(name))















