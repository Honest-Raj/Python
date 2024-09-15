try:
    name = "suresh"
    
    print(name.index("u"))

except ValueError as error:
    print("Something unexpected happend",error)

print("dqhqhwdhq-------------")

def add(a,b):
    pass

try:
    add(2,3)
except ValueError as error:
    print("This is Value Error")
except TypeError as error:
    print("Something unexpected happend:",error)
except Exception as error:
    print("this is Exception:",error)
else:
    print("this is else")
finally:
    print("This is finally")

print('Jjjj')



try:
    print("Hestdgqg")
except NameError as error:
    print(error)
finally:
    print("This is finnally--------")


