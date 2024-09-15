

# LIST, TUPLE, SET, DICTIONARY

# LIST

# Indexed
# Ordered
# It allows duplicates
# Changeable

fruits = ['apple',['harry', 'potter'],"banana" ,'apple', 'grapes']

# res = fruits[1][1]
# print(res)

# fruits.append("kiwi")
# print(fruits)

# Builtin Functions of List

# Append
# Extend
# Insert
# Pop
# Remove

# fruits.append("Banana")
# fruits.insert(1,"orange")
# fruits.extend(['captain','America'])
# fruits.pop()
# fruits.pop(2) - Index number
# fruits.remove('banana')
# fruits.count()
# fruits.index()
# fruits.clear()
# fruits.reverse()
# fruits.sort()


# res = fruits[1].insert(1,"orange")
# print(fruits)

# index1 = fruits.remove("apple")
# index1 = fruits.insert(0,"apple1")
# fruits[0] = 'apple1'
# print(fruits)

# fruits = ['apple',['harry', 'potter'], 'apple', 'grapes', 'apple']
# count = 0
# for i in range(len(fruits)):
#     if fruits[i]=='apple':
#         count += 1
#         fruits[i]= 'apple'+str(count)
# print(fruits)


# result = fruits.copy()

# fruits.append('-----------')
# print('fruits-->', fruits)
# print('data--->',result)


# for i in fruits:
#     if i == "apple":
#         fruits.remove(i)
#         print(fruits)


# fruits = ['apple', 'orange',['harry','potter'],'apple',['captan',['tom',['banana', 'orange'],'jerry'],'america','tony'],'apple','apple']
# output = []

# for i in fruits:
#     if type(i)== list:
#         for j in i:
#             if type(j)==list:
#                 for k in j:
#                     if type(k)==list:
#                         for e in k:
#                             print(e)
#                     else:
#                         print(k)
#             else:
#                 print(j)
#     else:
#         print(i)

# Recursion Type Function 

# fruits = ['apple', 'orange',['harry','potter'],'apple',['captan',['tom',['banana', 'orange'],'jerry'],'america','tony'],'apple','apple']# def loopings(data):
#     for i in data:
#         if type(i)==list:
#             loopings(i)
#         else:
#             print(i)


# loopings(fruits)


# TUPLE

# Ordered
# Indexed
# Allows duplicates
# Not changable


# fruits = ('apple', 'orange',(2,5,6),['harry''potter'],'apple',['captan',['tom',['banana',['wkedoku','wehkjbn'],'kiwi'],'apple'],'jerry'],'honest')
# fruits2 = ('kiwi',"grapes")

# fruits[3][0] = 'grapes'
# print(fruits)


# print(fruits.index('apple'))
# print(fruits.count('apple'))

# print(fruits + fruits2)

# numbers = [5,7,8,3,2,4,0,1,9]
# numbers.sort()
# print(numbers)
        
        
# input
#  data = "3e62#c1@-4b0d5a1"

# expected output
# "0a11#c2@-3b4d5e6" - numbers sort
# 0a11#b2@-3c4d5e6 - alphabets sort


# numbers = [5, 7, 8, 3, 2, 4, 0, 1, 9, 6]

# output =[]

# maxNum = 0

# while len(numbers)> 0:
#     for i in numbers:
#         if i > maxNum:
#             maxNum = i

#     output.insert(0, maxNum)
#     numbers.remove(maxNum)
#     maxNum = 0
    

# print(output)


# input [5, 0, 7, 0, 0, 8, 3, 0, 2, 4, 0, 0, 1, 9, 0, 6]
# output [1, 0, 2, 0, 0, 3, 4, 0, 5, 6, 0, 0, 7, 8, 0, 9]



# Lambda Function

# res = lambda a,b : a+b
# print(res(3,5))


# data = [3,5,6,1,4,7,10]

# data = list(map(lambda i: i*2, data))

# print(data)


# Even numbers matum multiple aganum na indha method

# data = [3,5,6,1,4,7,10]

# data = list(map(lambda i: i*2 if i%2==0 else i, data))

# print(data)

# 10 ku mela irundha inoru condition single line 

# data = [3,11,5,6,18,1,4,7,10,23,54,12]
# output = []
# for i in data:
#     if i>10:
#         output.append(i)
# print(output)

# data = list(map(lambda i: i*2 if i%2==0 else i*2 if i>10 else i , data))

# data = list(filter(lambda i: i%2==0 and i>10, data))

# data = list(filter(lambda i: i%2==0 or i>10, data))

# print(data)

# x = 12
# y = 5
# z = 32
# print("x is greater than y and z") if x>y and x>z else print('y is greater than x and z') if y>x and y>z else print('z is greater than x and y')

# if x>y and x>z:
#     print("x is greater than y and z")
# elif y >x and y>z:
#     print('y is greater than x and z')
# else:
#     print('z is greater than x and y')




# people = [
#     {'name':"Alice", "age": 12},
#     {'name':"Bob", "age": 25},
#     {'name':"Charle", "age": 35},
#     {'name':"Diana", "age": 22},
#     {'name':"Eve", "age": 28},
#     {'name':"Frank", "age": 33},
#     {'name':"Grace", "age": 27},
#     {'name':"Hank", "age": 24},
#     {'name':"Ivy", "age": 31},
#     {'name':"Jack", "age": 29},
#     {'name':"Kim", "age": 26},
#     {'name':"Leo", "age": 32},
#     {'name':"Mia", "age": 23},
#     {'name':"Nina", "age": 34}
# ]


# data = list(map(lambda i: i['name'], people))
# data = list(filter(lambda i: i["age"] > 15, people))

# print(data)

# output = []
# for i in people:
#     output.append(i['name'])

# print(output)

# Greater than 15 age matum venum

# data = list(map(lambda i : i ["name"], filter(lambda x : x ['age'] > 15, people)))
# data = list(filter(lambda i: i["name"], people))

# print(data)

# List fulla plus pananum

# data = [3,11,5,12,23,55,60,56,18,20,14]

from functools import reduce

# result = reduce(lambda a,b: a+b, data)
# print(result)

# res = 0

# for i in data:
#     res = res + i
# print(res)


# words = ['Hello', 'world', 'this', "is", 'Python']
# output = "Hello world this is Python"

# output = ''

# for i in words:
#     output += i +" "
# print(output.strip())

# output = reduce(lambda a, output: a +" "+ output, words)
# print(output)

# data = [3,11,5,12,23,55,60,56,18,20,14]
# find the largest number in the list using reduce function

# max = 0
# for i in data:
#     if i>max:
#         max=i
# print(max)

# list_of_lists = [[1,2,3],[4,5],[6,7,8,9]]
# output should be [1,2,3,4,5,6,7,8,9] using reduce function
# output = reduce(lambda i,y:i+y,list_of_lists)
# print(output)

# SET

# Unordered - When we print each time, it will suffle the orders
# UnIndexed - Because of suffle we can't find index number
# Doesn't allows duplicates
# Changable

# fruits = {"apple", "orange","grapes","kiwi"}
# print(fruits)

# Built In Functions:
# Add
# Update
# Union
# Pop
# Remove - Iladha data kudutha error throw panum
# Discard - Iladhe data kudutha error throw panadhu
# Clear

# fruits1 = {"apple", "orange","grapes","kiwi","apple"}
# fruits2 = {"apple", "banana","pineapple","kiwi"}

# fruits.add('banana')
# fruits.update(["banana",'pineapple'])
# fruits = fruits.union(['papaya',"berry"])
# fruits.pop()
# fruits.remove("banana")
# fruits.discard("honest")
# fruits.clear()
# fruits.copy()
# print(fruits1.intersection_update(fruits2))
# print(fruits1.intersection(fruits2))
# fruits1.difference_update(fruits2)
# fruits1.symmetric_difference_update(fruits2)

# print(fruits)


# DICTIONARY

user = {
    "name": "suresh",
    "age" : 12,
    "email" : "suresh@gmail.com",
    "address":{
        "state": "Tamilnadu",
        "district": "Chennai"
    },
    "fruits":["apple","orange",{'name':"suresh"}]
}

# user["phone"] = 90936932
# user['address']["country"] = "India"
# print(user["fruits"].remove("apple"))
# user['fruits'][2]['name']= "Ramesh"
#print(user)


# print(list(user.keys()))
# print(list(user.values()))
# print(list(user.items()))
# user.update({'name': 9093679})
# user.popitem()
# user.pop('name')
# user.clear()
# user.copy()

# print(user.setdefault('phone',90937123))      
# print(user)

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


# for i in range(len(users)):
#      users[i].setdefault('id', i)


# # for i in range(len(users)):
# #     if users[i]['age'] > 18:
# #         print(users[i])

# print(users)

# users = [
#     {
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
#     },
#     {
#         "name": "rekha",
#         "age": 34,
#         "email": "rekha@gmail.com",
#         "phone": 9080778965,
#         "dept": "CSE"
#     },
#     {
#         "name": "santosh",
#         "age": 19,
#         "email": "santosh@gmail.com",
#         "phone": 9080789076,
#         "dept": "ECE"
#     },
#     {
#         "name": "meena",
#         "age": 22,
#         "email": "meena@gmail.com",
#         "phone": 9080790187,
#         "dept": "MECH"
#     },
#     {
#         "name": "vikram",
#         "age": 30,
#         "email": "vikram@gmail.com",
#         "phone": 9080701298,
#         "dept": "EEE"
#     },
#     {
#         "name": "deepa",
#         "age": 26,
#         "email": "deepa@gmail.com",
#         "phone": 9080712309,
#         "dept": "CSE"
#     },
#     {
#         "name": "priya",
#         "age": 31,
#         "email": "priya@gmail.com",
#         "phone": 9080723410,
#         "dept": "ECE"
#     },
#     {
#         "name": "mohan",
#         "age": 28,
#         "email": "mohan@gmail.com",
#         "phone": 9080734521,
#         "dept": "MECH"
#     },
#     {
#         "name": "geeta",
#         "age": 25,
#         "email": "geeta@gmail.com",
#         "phone": 9080745632,
#         "dept": "EEE"
#     },
#     {
#         "name": "arjun",
#         "age": 33,
#         "email": "arjun@gmail.com",
#         "phone": 9080756743,
#         "dept": "CSE"
#     },
#     {
#         "name": "nidhi",
#         "age": 21,
#         "email": "nidhi@gmail.com",
#         "phone": 9080767854,
#         "dept": "ECE"
#     },
#     {
#         "name": "manish",
#         "age": 36,
#         "email": "manish@gmail.com",
#         "phone": 9080778965,
#         "dept": "MECH"
#     },
#     {
#         "name": "sona",
#         "age": 20,
#         "email": "sona@gmail.com",
#         "phone": 9080789076,
#         "dept": "EEE"
#     },
#     {
#         "name": "rahul",
#         "age": 27,
#         "email": "rahul@gmail.com",
#         "phone": 9080790187,
#         "dept": "CSE"
#     },
#     {
#         "name": "tina",
#         "age": 32,
#         "email": "tina@gmail.com",
#         "phone": 9080701298,
#         "dept": "ECE"
#     },
#     {
#         "name": "amit",
#         "age": 28,
#         "email": "amit@gmail.com",
#         "phone": 9080712309,
#         "dept": "MECH"
#     },
#     {
#         "name": "kavita",
#         "age": 24,
#         "email": "kavita@gmail.com",
#         "phone": 9080723410,
#         "dept": "EEE"
#     },
#     {
#         "name": "vijay",
#         "age": 35,
#         "email": "vijay@gmail.com",
#         "phone": 9080734521,
#         "dept": "CSE"
#     },
#     {
#         "name": "ChatGPT",
#         "age": None,
#         "email": "chatgpt@openai.com",
#         "phone": None,
#         "dept": "ECE"
    
#     },
# {
#      "name": "ChatGPT",
#         "age": None,
#         "email": "chatgpt@openai.com",
#         "phone": None,
#         "dept": "IT"
# }
# ]

# dept = dict()

# for i in users:
#    keys= list(dept.keys())
#    filteredData = list(filter(lambda a:a == i ['dept'], keys))
#    if len(filteredData)>0:
#       dept[i['dept']]= dept[i["dept"]]+1
#    else:
#         dept[i['dept']]=1
# print(dept)

# dept = dict()

# for i in users:
#    keys= list(dept.keys())
#    filteredData = list(filter(lambda a:a == i ['dept'], keys))
#    if len(filteredData)>0:
#       dept.update({i['dept']:dept[i["dept"]] +1})
#    else:
#         dept.update({i['dept']:1})
# print(dept)


# dept ={}
# for i in users:
#     dept[i['dept']]= dept.setdefault(i['dept'],0)+1
# print(dept)


# arr = [5,10,9,4,15]
# first = 0
# last = 3

# def getGreaterNumber(lis,firstNum,lastNum):

#     subList = []
#     for i in range(len(lis)):
#         if i>= firstNum and i< lastNum:
#             subList.append(lis[i])
    
#     if len(subList)==3:
#         greaterNum = subList[1] > subList[0] and subList[1] > subList[2]
#         if greaterNum == True:
#             return subList[1]
#         else:
#             return getGreaterNumber(lis,lastNum,lastNum+3)
#     else:
#         return max(subList)
    
# resultNumber = getGreaterNumber(arr,first,last)
# print(resultNumber)

# arr = [4,13,12,23,15]
# first = 0
# last = 3

# output = 0
# while True:
#     subList =[]
#     for i in range(len(arr)):
#         if i >=first and i<last:
#             subList.append(arr[i]) 

#     first = last 
#     last = last+3
#     if len(subList)==3:
#         greaterNum = subList[1]> subList[0] and subList[1]> subList[2]
#         if greaterNum == True:
#             output = subList[1]
#             break
#     else:
#         output = max(subList)
#         break
    
# print(output)
    
# arr = [1,2,3,2,5,6,7,8,2,3]
# sub =[]
# arrset=[]

# for i in range(len(arr)):
#     if len(sub)==0:
#         sub.append(arr[i])
#     elif sub[-1]<arr[i]:
#         sub.append(arr[i])
#         if i == len(arr)-1:
#             arrset.append(sub)
#             sub=[]
#             sub.append(arr[i])
#     else:
#         arrset.append(sub)
#         sub=[]
#         sub.append(arr[i])
# print("arrSets",arrset)

# maxlength = []

# for i in range(len(arrset)):
#     if len(arrset[i])>len(maxlength):
#         maxlength = arrset[i]
# print('max length', maxlength)
        

