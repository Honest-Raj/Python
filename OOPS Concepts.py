
# OOPS Concepts
# Object Oriented Programming Structure


# Class - A template or Blueprint of an object or instance
# Object -

# Have to use self or any string mandatory while using Class function

# Self is traditional style

# class Calculator:
#     def add(self,a,b):
#         return a+b

#     def sub(self,a,b):
#         return a-b
    
#     def mul(self,a,b):
#         return a*b

#     def div(self,a,b):
#         return a//b
    
# calc = Calculator()

# res = calc.add(3,5)
# print(res)

# print(calc.add(4,6))

# sub = calc.sub(3,5)
# print(sub)

# mul = calc.mul(10,20)
# print(mul)

# div = calc.div(20,10)
# print(div)





# class StringHandLings:
#     def reverseString(self,givenString):
#         output = ""
#         for i in range(len(givenString)):
#             output += givenString[-(i+1)]
#         return output
    
#     def addUnderscore(self,givenString):
#         output = ""
#         for i in givenString:
#             output += i + "_"
#         return output
    
#     def countWord(self,word,letter):
#         return word.count(letter)
    
# sth = StringHandLings()
# countRes = sth.countWord("Ramesh","R")
# print("countres--->", countRes)

# addUnderscoreRes = sth.addUnderscore("Ramesh")
# print(addUnderscoreRes)

# reverseString = sth.reverseString("Ramesh")
# print(reverseString)


# Basic User Interface Function

# def add(a,b):
#     print(a+b)

# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))

# add(num1,num2)


# users = [
#     {
#         "name": "suresh",
#         "age": 12,
#         "email": "suresh@gmail.com",
#         "phone": 9080716503
#     },
#     {
#         "name": "ramesh",
#         "age": 23,
#         "email": "ramesh@gmail.com",
#         "phone": 90808587685
#     },
#     {
#         "name": "neha",
#         "age": 29,
#         "email": "neha@gmail.com",
#         "phone": 9080734521
#     },
#     {
#         "name": "raju",
#         "age": 32,
#         "email": "raju@gmail.com",
#         "phone": 9080745632
#     },
#     {
#         "name": "jyoti",
#         "age": 24,
#         "email": "jyoti@gmail.com",
#         "phone": 9080756743
#     },
#     {
#         "name": "anil",
#         "age": 27,
#         "email": "anil@gmail.com",
#         "phone": 9080767854
#     },
#     {
#         "name": "rekha",
#         "age": 34,
#         "email": "rekha@gmail.com",
#         "phone": 9080778965
#     },
#     {
#         "name": "santosh",
#         "age": 19,
#         "email": "santosh@gmail.com",
#         "phone": 9080789076
#     },
#     {
#         "name": "meena",
#         "age": 22,
#         "email": "meena@gmail.com",
#         "phone": 9080790187
#     },
#     {
#         "name": "vikram",
#         "age": 30,
#         "email": "vikram@gmail.com",
#         "phone": 9080701298
#     },
#     {
#         "name": "deepa",
#         "age": 26,
#         "email": "deepa@gmail.com",
#         "phone": 9080712309
#     },
#     {
#         "name": "priya",
#         "age": 31,
#         "email": "priya@gmail.com",
#         "phone": 9080723410
#     },
#     {
#         "name": "mohan",
#         "age": 28,
#         "email": "mohan@gmail.com",
#         "phone": 9080734521
#     },
#     {
#         "name": "geeta",
#         "age": 25,
#         "email": "geeta@gmail.com",
#         "phone": 9080745632
#     },
#     {
#         "name": "arjun",
#         "age": 33,
#         "email": "arjun@gmail.com",
#         "phone": 9080756743
#     },
#     {
#         "name": "nidhi",
#         "age": 21,
#         "email": "nidhi@gmail.com",
#         "phone": 9080767854
#     },
#     {
#         "name": "manish",
#         "age": 36,
#         "email": "manish@gmail.com",
#         "phone": 9080778965
#     },
#     {
#         "name": "sona",
#         "age": 20,
#         "email": "sona@gmail.com",
#         "phone": 9080789076
#     },
#     {
#         "name": "rahul",
#         "age": 27,
#         "email": "rahul@gmail.com",
#         "phone": 9080790187
#     },
#     {
#         "name": "tina",
#         "age": 32,
#         "email": "tina@gmail.com",
#         "phone": 9080701298
#     },
#     {
#         "name": "amit",
#         "age": 28,
#         "email": "amit@gmail.com",
#         "phone": 9080712309
#     },
#     {
#         "name": "kavita",
#         "age": 24,
#         "email": "kavita@gmail.com",
#         "phone": 9080723410
#     },
#     {
#         "name": "vijay",
#         "age": 35,
#         "email": "vijay@gmail.com",
#         "phone": 9080734521
#     }
# ]

# email = 'vijay@gmail.com'
# age = 25
# for i in users:
#     if i['email']== email:
#          i['age']= age
#          i.update({'age':age})
        
# print(users)


# for i in users:
#     if i['email']== email:
#         i.pop("email")
# print(users)


# users = []

# class UserRegister:
#     def addUser(self):
#         print("----- Enter all the user details ----")
#         name = input("Enter user name: ")
#         age = int(input("Enter user age: "))
#         email = input("Enter user email : ")
#         print("----for dept choose any option below ----")
#         print('1. EEE')
#         print('2. MECH')
#         print('3. CSC')
#         print("4. IT")
#         dept = int(input("Enter your dept number: "))
#         userDic = {
#             "name": name,
#             "age": age,
#             "email": email,
#             "dept" : "EEE" if dept == 1 else "MECH" if dept == 2 else "CSC" if dept == 3 else "IT"
#         }
#         users.append(userDic)
#         print("------- user added successfully -------")
#     def getAllUsers(self):
#         print( "all users ---->", users)
    
#     def updateUser(self):
#         print("-----Please enter details for update-----")
#         email = input("Enter user email : ")
#         key = input("Enter the key to change : ")
#         value = input("Enter the value to change : ")

#         for i in users:
#             if i['email'] == email:
#                 i[key] = value

#         print("------user updated successfully------")

#     def deleteUser(self):
#         email = input("Enter user email id : ")
#         for i in users:
#             if i['email'] == email:
#                 users.remove(i)
#         print("----- user deleted successfully --------")

#     def deptCount(self):
#         pass
    
    

# usr = UserRegister()



# while True:
#     print("----Choose any options -------")
#     print("1. to add User")
#     print("2. to get all users")
#     print("3. Update User")
#     print("4. Delete user")
#     print
#     print("5. Exit")
#     option = int(input("Enter your option number: "))
#     if option == 1:
#         usr.addUser()
#     elif option == 2:
#         usr.getAllUsers()
#     elif option == 3:
#         usr.updateUser()
#     elif option == 4:
#         usr.deleteUser()
#     else:
#         break


# users = []
# class UserRegistration:
#     def addUser(self):
#         print("Add User")
#         name = input("Enter your name:")
#         age = int(input("Enter your age:"))
#         phone = int(input("Enter your phone number:"))
#         print("1.B.com")
#         print("2.MBA")
#         print("3.BCA")
#         print("4.MCA")
#         dept = int(input("Enter your dept number:"))
        
#         userDic ={
#             "name" : name,
#             "age" :age,
#             'phone' : phone,
#             "dept" : "B.com" if dept==1 else "MBA" if dept==2 else "BCA" if dept ==3 else "MCA" 

#         }
#         users.append(userDic)
#         print("user added")

#     def getUser(self):
#         print("All users",users)

# usr = UserRegistration()

# while True:
#     print("1.Add User")
#     print("2.Get User")
#     print('3.Exit')
#     option = int(input("Enter your options:"))
#     if option ==1:
#         usr.addUser()
#     elif option ==2:
#         usr.getUser()
#     else:
#         option ==3
#         break




# Constructor - It is a special type of function. It calls automatically whenever an object declared for the class

# class UserRegister:
#     def _init_(self) -> None:
#         self.users = []
#     def addUser(self):
#         print("----- Enter all the user details ----")
#         name = input("Enter user name: ")
#         if not name.isalpha():
#             print("Please enter a valid user name")
#             return 
#         age = input("Enter user age: ")
#         if age.isnumeric():
#             age = int(age)
#         else:
#             print("Please enter a valid age")
#             return 
#         email = input("Enter user email : ")
#         if (not email.endswith("@gmail.com")) or (not email.islower()):
#             print("Please enter a valid email")
#             return
#         print("----for dept choose any option below ----")
#         print('1. EEE')
#         print('2. MECH')
#         print('3. CSC')
#         print("4. IT")
#         dept = input("Enter your dept number: ")
#         if dept.isnumeric():
#             dept = int(dept)
#         else:
#             print("Please enter a valid dept")
#             return 
#         userDic = {
#             "name": name,
#             "age": age,
#             "email": email,
#             "dept" : "EEE" if dept == 1 else "MECH" if dept == 2 else "CSC" if dept == 3 else "IT"
#         }
#         self.users.append(userDic)
#         print("------- user added successfully -------")
#     def getAllUsers(self):
#         print( "all users ---->", self.users)
    
#     def updateUser(self):
#         print("-----Please enter details for update-----")
#         email = input("Enter user email : ")
#         key = input("Enter the key to change : ")
#         value = input("Enter the value to change : ")

#         for i in self.users:
#             if i['email'] == email:
#                 i[key] = value

#         print("------user updated successfully------")

#     def deleteUser(self):
#         email = input("Enter user email id : ")
#         for i in self.users:
#             if i['email'] == email:
#                 self.users.remove(i)
#         print("----- user deleted successfully --------")

#     def deptCount(self):
#         departmentCounts = dict()
#         for i in self.users:
#             departmentCounts[ i['dept'] ] = departmentCounts.setdefault(i['dept'] , 0) + 1          
#         return departmentCounts

#     def spificDeptStudents (self):
#         deptName = input("Enter the department name : ")
#         filteredUsers = list(filter(lambda a: a['dept'] == deptName, self.users))
#         if len(filteredUsers) > 0:
#             return filteredUsers
#         else:
#             return "Users not found"


# usr = UserRegister()


# while True:
#     print("----Choose any options -------")
#     print("1. to add User")
#     print("2. to get all users")
#     print("3. Update User")
#     print("4. Delete user")
#     print("5. get all department count")
#     print("6. get specific department students")
#     print("7. Exit")
#     option = (input("Enter your option number: "))
#     if option.isnumeric() == True:
#         option = int(option)
#         if option == 1:
#             usr.addUser()
#         elif option == 2:
#             usr.getAllUsers()
#         elif option == 3:
#             usr.updateUser()
#         elif option == 4:
#             usr.deleteUser()
#         elif option == 5:
#             print( "department counts :", usr.deptCount())
#         elif option == 6:
#             print(usr.spificDeptStudents())
#         else:
#             break
#     else:
#         print("Please enter valid option")


# DILLI NOTES
# users = []

# class UserRegister:
#     def addUser(self):
        
#         print("----- Enter all the user details ----")
#         while True:
#          name = input("Enter user name: ")
#          if name[0].isupper():
#             break
#          else:
#             print("Enter name in capital letter")
         
#         while True:
#             age = (input("Enter user age: "))
#             if age.isnumeric():
#                age =int(age)
#                break
#             else:
#               print("enter the age in number")
            
            
#         while True:  
#          email = input("Enter user email : ")
#          atPos = email.find('@')
#          dotPos = email.find('.')
#          if  email.islower() and atPos != -1 and dotPos != -1 and atPos < dotPos and atPos>0 and dotPos<len(email)-1:
#             break
#          else:
#           print("Enter a valid email address")
  

#         print("----for dept choose any option below ----")
#         print('1. EEE')
#         print('2. MECH')
#         print('3. CSC')
#         print("4. IT")

#         while True:
#           dept=input("enter the department:")
#           if dept.isnumeric():
#              dept=int(dept)
#              break
#           else:
#             print("enter the number only in department")   
            
#         userDic = {
#             "name": name,
#             "age": age,
#             "email": email,
#             "dept" : "EEE" if dept == 1 else "MECH" if dept == 2 else "CSC" if dept == 3 else "IT"
#         }
#         users.append(userDic)
#         print("------- user added successfully -------")
#     def getAllUsers(self):
#         print( "all users ---->", users)
    
#     def updateUser(self):
#         print("-----Please enter details for update-----")
#         email = input("Enter user email : ")
#         key = input("Enter the key to change : ")
#         value = input("Enter the value to change : ")

#         for i in users:
#             if i['email'] == email:
#                 i[key] = value

#         print("------user updated successfully------")

#     def deleteUser(self):
#         email = input("Enter user email id : ")
#         for i in users:
#             if i['email'] == email:
#                 users.remove(i)
#         print("----- user deleted successfully --------")
#     def addDeptCount(self):
#         eeeCount=0
#         mechCount=0
#         cscCount=0
#         ItCount=0
        
#         for i in users:
#             if i['dept'] == "EEE":
#                 eeeCount += 1
#             elif i['dept'] == "MECH":
#                 mechCount += 1
#             elif i['dept'] == "CSC":
#                 cscCount += 1
#             elif i['dept'] == "IT":
#               ItCount += 1

#         print("EEECOUNT",eeeCount)
#         print("MECHCOUNT",mechCount)
#         print("ITCOUNT",ItCount)
#         print("CSCCOUNT",cscCount) 

# usr = UserRegister()

# while True:
#     print("----Choose any options -------")
#     print("1. to add User")
#     print("2. to get all users")
#     print("3. Update User")
#     print("4. Delete user")
#     print("5.add department count")
#     print("6. Exit")
#     option = (input("Enter your option number: "))
#     if (option).isnumeric():
#         option=int(option)
        
#         #print("its not number ",str(option))
      
#         if option == 1:
            
#           usr.addUser()
#         elif option == 2:
#             usr.getAllUsers()
#         elif option == 3:
#          usr.updateUser()
#         elif option == 4:
#          usr.deleteUser()
#         elif option==5:
#          usr.addDeptCount()
#         else:
#          break
#     else:

#       print("Please enter a numeric value.")



# Constructor - is a special type function it calls automatically whenever an object declared for the class



# class Users:
#     def __init__(self):
#         self.name = 'suresh'
#         self.age = 23
#         print("this is constructor functions", self.name)


#     def add(self):
#         print("this is add function", self.name, self.age)


# obj = Users()



#  INHERITANCE-----------

# Types of Inheritance

# Single Inheritance - Oru class ah vechi combine or inherit pandradhu. Eg- Oru parent oru child ah inherit pandradhu
# Multiple Inheritance - Orey class ah vechi Rendu moonu class ah inherit pandradhu. Eg - Oru parent rendu moonu child ah inherit pandradhu
# Multilevel Inheritance - Oru class la level level ah sethu vechi sethu vechi pandradhu
# Hierarchy Inheritance - Orey parent multiple child

# Single Inheritance 

# class Parent:
#     pass

# class Child(Parent):
#     pass

# Multiple Inheritance

# class Parent:
#     pass

# class Child1:
#     pass

# class Child2(Parent,Child1):
#     pass

# obj  = Child2()

# Multilevel Inheritance

# class Parent:
#     pass

# class Child1(Parent):
#     pass

# class Child2(Child1):
#     pass

# Hierarchy Inheritance

# class LoginSignup:
#     pass

# class UserRegistration(LoginSignup):
#     pass

# class Attendance(LoginSignup):
#     pass


# class Class2:
#     def sub(self):
#         pass

# class Class1(Class2):
#     def add(self):
#         pass

# obj = Class1()
# obj.add()
# obj.sub()



# class LoginSignup:

#     def __init__(self):
#         self.loginDetails = []


#     def login(self):

#         username = input("Enter your username: ")
#         password = input("Enter your password: ")        
        
#         checkValid = len(list(filter(lambda x  : x['username'] == username and x['password'] == password, self.loginDetails))) > 0

#         if (checkValid == True):
#             for i in self.loginDetails:
#                 if i['username'] == username and i['password'] == password:
#                     i['isLoggedin'] = True

#             print(self.loginDetails)
#             return True
#         else:
#             print("invalid login credentials")
#             return False


#     # ----------------- logout functon --------------------------------
#     def logout(self):
#         for i in self.loginDetails:
#             if i.setdefault('isLoggedin') == True:
#                 i['isLoggedin'] = False
#             else:
#                 i['isLoggedin'] = False
#         print("user logged out successfully !!!")
#         return True


#     def signup(self):

#         username = input("Enter your username: ")
#         print("Please enter a valid user name")
    
#         password = input("Enter your password: ")

#         specialCharacters = '!@#$%^&*()_-?/|'

#         if (len(password) > 8):
            
#             checkUppercase = len(list(filter(lambda x: x.isupper(), password))) > 0
#             checkLowercase = len(list(filter(lambda x: x.islower(), password))) > 0
#             checkNumeric = len(list(filter(lambda x: x.isnumeric(), password))) > 0
#             checkSpecialChar = len(list(filter(lambda x: x in specialCharacters, password))) > 0

#             print(checkLowercase, checkUppercase, checkNumeric, checkSpecialChar)
#             if (checkLowercase == True and checkUppercase == True and checkNumeric == True and checkSpecialChar == True):
#                 dic = {
#                     "username": username,
#                     "password": password
#                 }
#                 self.loginDetails.append(dic)
#                 print("------------ account created successfully------------")
                
#         else:
#             print('''
#                 Valid password:
#                     1. length should be greater than 8.
#                     2. should have atleast one upper and lower case.
#                     3. should have atleast one number.
#                     4. should have atleast one special character.
#             ''')

# class UserRegister(LoginSignup) :
#     def __init__(self):
#         super().__init__()
#         print('----------------------------------------------')
#         self.users = [
#             {
#         "name": "suresh",
#         "age": 12,
#         "email": "suresh@gmail.com",
#         "phone": 9080716503,
#         "dept": "MECH"
#     },
#     {
#         "name": "ramesh",
#         "age": 23,
#         "email": "ramesh@gmail.com",
#         "phone": 90808587685,
#         "dept": "EEE"
#     },
#     {
#         "name": "neha",
#         "age": 29,
#         "email": "neha@gmail.com",
#         "phone": 9080734521,
#         "dept": "CSE"
#     },
#     {
#         "name": "raju",
#         "age": 32,
#         "email": "raju@gmail.com",
#         "phone": 9080745632,
#         "dept": "ECE"
#     },
#     {
#         "name": "jyoti",
#         "age": 24,
#         "email": "jyoti@gmail.com",
#         "phone": 9080756743,
#         "dept": "MECH"
#     },
#     {
#         "name": "anil",
#         "age": 27,
#         "email": "anil@gmail.com",
#         "phone": 9080767854,
#         "dept": "EEE"
#     }
#     ]

#         while True:

#             self.getLoggedinUser = list(filter(lambda x: x['isLoggedin'] == True, self.loginDetails))
#             if (len(self.getLoggedinUser) > 0):
#                 self.secondHalf()
#             else:
#                 self.firstHalf()
                
            

#     def firstHalf(self):
#             isUserLoggedIn = False
#             while True:
#                     print(" ---- Choose any one option ----")
#                     print("1. to Login")
#                     print("2. to Signup")
#                     print("3. Exit")
#                     option = (input("Enter your option number: "))
#                     if option.isnumeric() == True:
#                         option = int(option)
#                         if option == 1:
#                             isUserLoggedIn = self.login()
#                             if isUserLoggedIn == True:
#                                 break
#                         elif option == 2:
#                             self.signup()
#                         else:
#                             break
#                     else:
#                         print("Please enter valid option")

#     def secondHalf(self):
#             while True:
#                 print("----Choose any options -------")
#                 print("1. to add User")
#                 print("2. to get all users")
#                 print("3. Update User")
#                 print("4. Delete user")
#                 print("5. get all department count")
#                 print("6. get specific department students")
#                 print("7. Logout")
#                 option = (input("Enter your option number: "))
#                 if option.isnumeric() == True:
#                     option = int(option)
#                     if option == 1:
#                         self.addUser()
#                     elif option == 2:
#                         self.getAllUsers()
#                     elif option == 3:
#                         self.updateUser()
#                     elif option == 4:
#                         self.deleteUser()
#                     elif option == 5:
#                         print( "department counts :", self.deptCount())
#                     elif option == 6:
#                         print(self.spificDeptStudents())
#                     elif option == 7:
#                         logedOut = self.logout()
#                         if logedOut == True:
#                             break
#                     else:
#                         break
#                 else:
#                     print("Please enter valid option")
            
#     def addUser(self):
#         print("----- Enter all the user details ----")
#         name = input("Enter user name: ")
#         if not name.isalpha():
#             print("Please enter a valid user name")
#             return 
#         age = input("Enter user age: ")
#         if age.isnumeric():
#             age = int(age)
#         else:
#             print("Please enter a valid age")
#             return 
#         email = input("Enter user email : ")
#         if (not email.endswith("@gmail.com")) or (not email.islower()):
#             print("Please enter a valid email")
#             return
#         print("----for dept choose any option below ----")
#         print('1. EEE')
#         print('2. MECH')
#         print('3. CSC')
#         print("4. IT")
#         dept = input("Enter your dept number: ")
#         if dept.isnumeric():
#             dept = int(dept)
#         else:
#             print("Please enter a valid dept")
#             return 
#         userDic = {
#             "name": name,
#             "age": age,
#             "email": email,
#             "dept" : "EEE" if dept == 1 else "MECH" if dept == 2 else "CSC" if dept == 3 else "IT"
#         }
#         self.users.append(userDic)
#         print("------- user added successfully -------")
#     def getAllUsers(self):
#         print( "all users ---->", self.users)
    
#     def updateUser(self):
#         print("-----Please enter details for update-----")
#         email = input("Enter user email : ")
#         key = input("Enter the key to change : ")
#         value = input("Enter the value to change : ")

#         for i in self.users:
#             if i['email'] == email:
#                 i[key] = value

#         print("------user updated successfully------")

#     def deleteUser(self):
#         email = input("Enter user email id : ")
#         for i in self.users:
#             if i['email'] == email:
#                 self.users.remove(i)
#         print("----- user deleted successfully --------")

#     def deptCount(self):
#         departmentCounts = dict()
#         for i in self.users:
#             departmentCounts[ i['dept'] ] = departmentCounts.setdefault(i['dept'] , 0) + 1          
#         return departmentCounts

#     def spificDeptStudents (self):
#         deptName = input("Enter the department name : ")
#         filteredUsers = list(filter(lambda a: a['dept'] == deptName, self.users))
#         if len(filteredUsers) > 0:
#             return filteredUsers
#         else:
#             return "Users not found"


# usr = UserRegister()


class details:
     def signup():
        while True:
            username = input("Enter your username:")
            if username.isalpha():
                password = input("Enter your password:")
                if len(password)>8:
                    password.isnumeric
                else:
                    print("no password")
                    
                return
            
            else:
                print('no valid details')
                break
            
            
        
usr = details.signup()