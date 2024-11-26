#              Dictionary

thisdict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year"  : "1998"
}

print(thisdict)

print(len(thisdict)) #print length

x = thisdict["Model"] # or use get()
print(x)

y = thisdict.keys()
print(y)



# value\

z = thisdict.values()
print(z)

a = thisdict.items()
print(a)

if "Dealer" in thisdict :
    print("Yes")
else :
    print("No")

# add item to dict

# thisdict["Color"] = "Red"
# print(y)

# use of update() , argumesnt must be a dictionary or key : value

thisdict.update({"Color":"Red"})
print(thisdict)

# delete a item

thisdict.pop("Year")
print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict.clear()
print(thisdict)

# copy a dictionary / use dict constructor
car = thisdict.copy()
print(car)

# Nested loop

myfamily = {
    "child1" :
    {
        "Name" : "Niloy",
        "Year" : 2004
    },
    "child2" : {
        "Name" : "Dagi",
        "Year" : 2006
    },
    "child3" :
    {
        "Name" : "Ayeshi",
        "Year" : 2022
    }
}

print(myfamily["child1"]["Name"])


for x , obj in myfamily.items():
    print(x)
    for y in obj :
        print(y + ':',obj[y])

#        if-else

a = 10
b = 10
if a>b :
    print("a is greater")
elif(a == b) :
    print("a is equal to b")
else :
    print("b is greater")

# print("a > b") if a>b else print("b > a")

print("a > b") if a>b else print("=") if a == b else print("b > a")

# i = 0 
# while i < 6 :
#     print(i)
#     i = i+1
#     if(i == 4) :
#         break

i = 0 
while i < 6 :
    i = i+1
    if i == 4 :
        continue
    print(i)

for x in range(2,10,2) :
    print(x)

   
