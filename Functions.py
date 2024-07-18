

# FUNCTIONS

# Built in function
# User defined function - We have to write "return" to execute or else it shows None.
# Recursion Type function
# Anonymous function

# def addition():
#     return 2+2       
# result = addition()
# print("this is result" ,result)

# Parameters And Arguments

# def add(num1, num2):
#     return num1 + num2

# result = add(4,7)
# print('this is result', result)

# result = add(10,10)
# print('this is result',result)

# result = add(20,20)
# print('this is result',result)


# def user(name,age,email):
#     print(f'my name is {name} and my age is {age} and my email is {email}')
# user("Honest",23,"honest@gmail.com")

# def add(num1, num2):
#     return num1 + num2
# result = add(5,9)
# print(result)

# def add(num1, num2):
#     return num1 + num2 


# Positional Argurments - It runs with 1st for 1st, 2nd for 2nd order basis.

# def user(name,age,email,addition):
#     result = addition(3,6)
#     print(result)
#     print(f'my name is {name} and my age is {age} and my email is {email}')

# user("Honest",23,"honest@gmail.com",add)


# Keyword Arguments - It runs with keywords even if we change the orders.

# def user(name,age,email):
#      print(f'my name is {name} and my age is {age} and my email is {email}')
# user(age=23, name= "suresh", email = "suresh@gmail.com")


# Default Argurments - If user doesn't have variable, we can directly assign dummy value by default.

# def user(name,age,email="dummy@gmail.com"):
#       print(f'my name is {name} and my age is {age} and my email is {email}')
# user (age=23,name= "Honest")


# Arbitary Arguments - If we need two or more values in one variable, we have to add * before that last variable and its shows in the tuple.

# def user(name,age,*subjects):

#        print(f'my name is {name} and my age is {age} and my subjects is {subjects}')
# user ("Honest",24,"maths","science")


# name = "softlogic"
# output = ""

# for i in range(len(name)):
#         output += name[-(i+1)]
# print(output)
# if name == output:
#         print (" the given string is palindrome")
# else:
#         print (" the given string is not palindrome")



# def palindromechecker(data):
    
#     output = ""
#     for i in range(len(data)):
#         output += data[-(i+1)]

#     if data == output:
#         return " the given string is palindrome"
#     else:
#         return " the given string is not palindrome"
    
# result = palindromechecker("softlogic")
# print("this is softlogic result",result)

# result = palindromechecker("madam")
# print("this is madam result",result)


# def palindromechecker(data):

#     if data =="" :
#         return " the string is empty"
#     output = ""
#     for i in range(len(data)):
#         output += data[-(i+1)]

#     if data == output:
#         return " the given string is palindrome"
#     else:
#         return " the given string is not palindrome"
    
# result = palindromechecker("")
# print("this is testing----",result)


# def gf(name, hobbies,age,love, email= "none"):
#     print(f'my gf name is {name}.She is {age} years old. Her hobbies is {hobbies}. Her mail id is {email} and she loves {love}. ')

# gf(name = "Likitha",age =24, hobbies ="watching movies",email= "likitha@gamil.com", love ="Honey")



name = "Honest Raj"
output = ""
for i in range(len(name)):
    output += name[-(i+1)]
    print(output)

print(output)
output = name[-(i+1)]
print(output)