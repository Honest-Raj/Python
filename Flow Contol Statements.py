
# FLOW CONTROL STATEMENTS


# If else elif
# Loopings
# Break
# Continue
# Pass

# x = 11
# if x>10:
#     print("x is grater than 10")
# elif x==10:
#     print("x is equal to 10")
# elif x ==11:
#     print("x is equal to 11")
# else:
#     print("X is not greater than 10")

# x = 20
# if x<10:
#     print("x is lesser than 10")
#     print ("we have a value until 9")
# elif x==10:
#     print("x is equal to 10")
#     print("there is a value more than 10")
# elif x<=20:
#     print("x is equal to 20")
# elif x>=20:
#     print("x is greater than 20")


# name = "softlogic"
# if name.find('o') !=-1:
#     print("the string has o")
# else:
#     print("the string has no o")


# LOOPINGS
# For Loop - We must give start and end range.
# While Loop - Only starting point is enough, it will loop infinite times.

# For Loop

insname = "Softlogic"
out = ""

for data in insname:
    out +=data
    print(out)

# print("-----end-----")

#for data in range(10):
#     print(data)

# insname = "dqwdkwdgkqjwdg"    
# length = len(insname)

# for data in range(length):
#      print(data,insname[data])

# insname = "dqwdkwdgkqjwdg"    
# length = len(insname)
# num = 0
# for data in range(length):
#     print("first print>>",num)
#     num += 1
#     print("second print>>",num)

# insname = "Softlogic institution"    
# length = len(insname)
# num = 2

# for data in range(length):
#     if data ==num:
#         print(insname[data])
#         num = num + 3


# name1 = "santhosh"
# # output = s_a_n_t_h_o_s_h
# output = ""
# for i in range(len(name1)):
#     if (i == len(name1)-1):
#         output += (name1[i])
#     else:
#         output += ( name1[i] + "_")

#     print(output)

# for i in name1:
#     output += i + "_"
# output = output[:-1]
# print(output)


# name = "HonestRaj"
# len = len(name)
# for data in range(len):
#     print(data,name[data])

# name = 'Honestraj'
# name1 = 'Harishkumar'
# output = 'common letters'
# name2 =''
# for data in name:
#     print(data,data)
#     for beta in name1:
#         print(beta,beta)
#         if data==beta:
#             name2+=data
# print("common",name2)
# final =''
# for value in name2:
#     if value not in final:
#         final+=value
# print("duplicate removed", final)


# Break - To break the overall loop
# Continue - To skip the current iteration
# Pass - Reserved Keyword


# text = "suresh"
# i = "s"
# print(text.find(i)!=-1)

# input = "softlogic"
# output = "s1o2f1t1l1o2g1i1c1"

# name = "softlogic"
# output = ""
# for i in name:
#     val = name.count(i)
#     output += i + str(val)
# print(output)

# PASS

# name = "suftalogic"
# vowels = "aeiou"
# output = ""
# for i in name:
#     if i in vowels:
        
#         pass
#     else:
#         output+=i

# print(output)



# Task 1
# input = "hello world"
# output = "olleh dlrow"
# out= ""
# output=""
# split = input[0:6]
# split1 = split[::-1]
# split2 = input[-5:]
# split2 = split2[::-1]
# formater = "{0} {1}".format(split1,split2)
# print(split1,split2)
# print(formater)

#for data in input:
#     out = input[0:6]
#     out = out[::-1]
#     output =input[-5:]
#     output = output[::-1]
    
# print(out,output)


# Task 2
# input = "Hello World"
# output = "hELLO wORLD"
# print(input.swapcase())


#Task 3
# input = "hello world"
# len = len(input)
# num = 0
    

# #output = "hlowrd"
# for i in range(len):
#     if i ==num:
#         num = num + 2
#         print(input[i])

        


# Task 4 
# input = "I have 245 apples and 367 bananas"
# Output = "I have two apples and three bananas"
# one = ""

# one = input.replace("0","zero")
# one = one.replace("1","one")
# one = one.replace("2","two ")
# one = one.replace("3","three ")
# one = one.replace("4","four")
# one = one.replace("5"," five")
# one = one.replace("6","six ")
# one = one.replace("7","seven")
# one = one.replace("8","Eight")
# one = one.replace("9","Nine")


# print(one)

# Input = " I have 23 apples"
# Output = " I have two three apples"

# Task 5
# Input = "hello"
# helo = ""
# # Output = "hheelllloo"
# for i in Input:
#     helo += (i*2)
# print(helo)


# CONTINUE

# input = "hello world this is fun"
# output = ""
# count = 0
# for i in range(len(input)):
#     if input[i] ==" ":
#         output+=str(count)
#         count=0
#         continue
#     count+=1
#     if i==(len(input)-1):
#         output+=str(count)
# print(output)

# splited = input.split(' ')
# print(splited)
# output = ""

# for i in splited:
#     output+=str(len(i))
# print(output)


# name = "gfgftglvhgvghvglvgv"
# #output = "soft l ogic"
# split = name[0:4]
# split2 = name[-4:]
# formater = f"{split}{split2}"
# formater = split + " l " + split2
# print(formater)


# name = name.replace("l"," l ")
# name = name.find("l")
# formater = name.replace(name," l ")
# print(formater)


# name = "dwedcbwrbfwkbkjbbr"
# letter = "r"
# indexnum = name.find(letter)

# output = name[:indexnum] + " " + name[indexnum] + name[indexnum+1:]
# output = "{}{}{}".format(name[:indexnum], name[indexnum], name[indexnum+1:])
# output = f"{name[:indexnum]} {name[indexnum]} {name[indexnum+1:]}"
# output = "%s %s %s" % (name[:indexnum], name[indexnum], name[indexnum+1:])
# print(output)



# name = "soft"
# #output = soofffttt
# out = ""
# for i in range(len(name)):
#     out = out + name[i]*(i+1)
#     print(out)



# data = "hello world this is for testing sss"
# vowels = 'aeiou'
# # output - '2 1 1 1 1 2 1'

# output = ''
# count = 0
# for i in range(len(data)):
#     if data[i] != " ":
#         if i != (len(data) -1) and vowels.find(data[i]) != -1:
#             count += 1
#         elif i == (len(data) -1):
#             print("else if", data[i])
#             if vowels.find(data[i]) != -1:
#                 count += 1
#             output += str(count)
#             count = 0    
#     else:
#         output += str(count)
#         count = 0

# print(output)

# While Loop

# name = "this is testing"
# count =0
# while True:
#     if count == 40:
#         break
#     elif count %2 !=0:
#         continue
#     print("this is testing")

    