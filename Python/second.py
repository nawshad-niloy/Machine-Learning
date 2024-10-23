#                              list


myList = ["Eat","sleep","Repeat"]
print(myList)
print(len(myList))
# range

List = ["Math","Statistics","Java","OS","MAP"]
print(List[0:2])
#   negative range
print(List[-4:-1])
#     check list
# if "Eat" in myList:
#     print("Yes")
# #update list
# myList[1] = "Study"
# print(myList)
# #  insert method
#  # myList.insert(0,"Wake Up")
#  # print(myList)
#  # #remove item method
#  # myList.remove("Study")
#  # print(myList)
#  # #remove index method
#  # List.pop(1)
#  # print(List)
#  # #to delete the entire list
#  # #del List
#  # print(List) #willcause an error as List was deleted
#  # #  clear list
#  # myList.clear() #list stays but empty
#  # print(myList)
#  #loop list
#  # for x in myList :
#  #     print(x)
#  # for i in range(len(myList)) :
#  #     print(myList[i])
#  # #while loop
#  # i = 0
#  # while i < len(myList) :
#  #     print(myList[i])
#  #     i = i+1
#  # #list comprehension
#  # fruits = ["Apple","Banana","Orange"]
#  # newList = []
#  # for x in fruits :
#  #         newList.append(x)
#  # print(newList)
#  #shorting
#  # newList = [x for x in fruits]
#  # print(newList)
#  #sort
#  # myList.sort()
#  # print(myList)
#  # listNum = [10,9,8,6,25,30]
#  # listNum.sort(reverse=True)
#  # print(listNum) #reverse/descending
#  # orderList = ["#53","#7","#27","#3325","#58714"]
#  # sorted_list = sorted(orderList);
#  # print("Sorted Order List : ",sorted_list)
#  #by length
#  # sorted_by_length = sorted(orderList,key=len)
#  #print("Sorted Order List : ",sorted_by_length)
#  #custom function
#  # def mypref(string):
#  #     return int(string[1:])
#  # Sorted_by_value = sorted(orderList,key=mypref)
#  # print(Sorted_by_value)
#  #reverse list regardless of alphabet or numerical order
#  # name = ["Sojib","Jim","Gay"]
#  # name.reverse()
#  # print(name)
#  #num = [2,3,8,4,963,1000]
#  #num.reverse()
#  #print(num)

#            copy list
students = ["Joy","Topu","Badhon"]
dendikhor = students.copy()
dendikhor = list(students)
print(dendikhor)
#  slicing a part

dendikhor = students[0:1]
print(dendikhor)

#         join

list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)
#or use append

for x in list2 :
    list1.append(x)
print(list1)

list1.extend(list2)
print(list1)

#                                        tuples

fol = ("Apple","Cherry","Grape","Apple","Cherry","Grape")
print(fol)
myTuple = ("Apple",)
print(type(myTuple))
myTuple = ("Apple")
print(type(myTuple))

# update tuple : make the tuple into list , change it
# then again convert it to tuple

x = ("Niloy","A","B")
y = list(x)
print(y)
y[1]="C"
print(y)

y.append("c")
print(y)

y.insert(3,"C")
print(y)


x = tuple(y)
print(x)

# remove
x = ("Niloy","A","B")
y = list(x)
print(y)

y.remove("B")
x = tuple(y)
print(x)

# del x
# print(x)


#add tuple to tuple
fruits = ("Grape","Watermelon","Mango","Bean")
vegetable = ("Tomato",)
fruits += vegetable
print(fruits)

#unpack
cars = ("Audi","Lambo","RR","Pagani")

car1,car2,car3,car4=cars
print(car1)
print(car2)
print(car3)
print(car4)

car1,car2,*car3=cars
print(car1)
print(car2)
print(car3)

#Loop

for x in cars :
     print(x)


#      indexing
for i in range(len(cars)) :
    print(cars[i])
while i < len(cars) :
    print(cars[i])
    i=i+1
    
    # join tuple
car = ("Tomtom","CNG","Auto")
a = (1,2,3)
newTuple = car + a
print(newTuple)

nums = (2,4,9,10,15,10) #multiplying contents
muls = nums*2
print(muls)
a = nums.count(10) #returns the number of times a value appear
print(a)
b = nums.index(10) #returns the index of first cameo hqhq
print(b)



#                           Set

myset = {"Nesha","Nari","Tash"}
print(myset)

thisSet = {"Cars","Bars",True,1,5} # 1 and true is considered same
print(thisSet)
#accessing item 
for x in myset :
    print(x)

# find a item
if "Nesha" in myset :
    print("Yes")

print("Nesha" in myset)

print("Gaja" not in myset)

#add items
myset.add("Glutonny")
print(myset)

#to update a set from another set or even another list/
myset.update(thisSet)
print(myset)

thisSet.update(myList)
print(thisSet)

myset.remove("Cars")
print(myset)

# or use discard that won't show error if item is not in set
myset.discard("Bus")
print(myset)

#remove random item
myset.pop()
print(myset)

myset.clear()
print(myset)

# join 

set1 = {'a','b','c'}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)
