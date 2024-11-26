# import my_module
import Add_module as Mx
import platform
from my_module import person2
import math
# a = my_module.person1["Age"]
# print(a)

Mx.Calculator(4,8)

print(platform.system())
# print(dir(platform))

print(dir(Mx))

print(person2["Gender"])

#            Math

x = max(10,25,1,1000,11125)
y = min(10,25,2,1000,11125)
print(x,y)

print(pow(x,y))

print(math.sqrt(9))

print(math.ceil(1.4))
print(math.floor(1.4))

username = input("Enter Username ")
print(username)