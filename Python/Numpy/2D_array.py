import numpy as np


a = np.array([1,3,5])
# print(a)

b = np.array([2,5,10])

print(a*b)
print("\n")

c = np.array([[2,3,5,7],[5,4,7,10]],dtype='int16')
print(c)

print(a.ndim) # get dimension

# get  shape (row,column)
print(c.shape)

#get data type and size
print(c.dtype)
print(c.size)

print(c.itemsize) #get item byte size

#get total size of array in bytes
print(c.nbytes)

#get a specific element
print(c[0,2])

#get a specific row
print(c[0, :]) 
print("\n")

#get a specific column
print(c[ :,2])
print("\n")

print(c[0,1:4]) #get a row range
print("\n")

d = np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11]])

print(d)
print("\n")

print(d[1:3,1])
print("\n")

#sub array
sub_matrix = d[1:3,1:3]
print(sub_matrix)
print("\n")



