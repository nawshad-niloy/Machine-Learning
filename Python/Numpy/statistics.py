import numpy as np

data = np.array([[1,2,3],[4,5,6]])
print(data)
print("\n")

print("Minimum : ",np.min(data))
print("\n")

print("Maximum of both row : ",np.max(data,axis=1))

print("Sum of data : ",np.sum(data))

print("\n")

#vertical stack

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

v = np.vstack([v1,v2,v1,v2])
print(v)
print("\n")
#horizontal  stacking 

h1 = np.ones((2,4))
h2 = np.zeros((2,2))

h = np.hstack([h1,h2])
print(h)
print("\n")

# import data from txt file

filedata = np.genfromtxt('data.txt',delimiter=',')
filedata = filedata.astype('int32')
print(filedata)
print("\n")

#boolean masking 
print(filedata > 50)

#indexing 

print(filedata[filedata >= 90])