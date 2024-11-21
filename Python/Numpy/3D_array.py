import numpy as np

a = np.arange(45).reshape(3,3,5)
print(a)
print("\n")

print(a[0])
print("\n")

print(a[0][1])
print("\n")

#get first row of last matrix
print(a[1:,0])
print("\n")

#get sub matrix fro, last 2 matrix
print(a[1:,0:2,1:4])

#zero matrics
b = np.zeros(5)
print(b)
print("\n")

#2d
c = np.zeros((3,4))
print(c)
print("\n")

#3d
d = np.zeros((3,3,4))
print(d)
print("\n")

e = np.full([2,2],50,dtype= int)
print(e)
print("\n")

f = np.random.rand(3,2)
print(f)
print("\n")

g = np.random.randint(2,11,(3,4))
print(g)
print("\n")

#identity matrix
print(np.identity(3))
print("\n")

#repeat element 
x = np.array([[1,2],[3,4]])
print(np.repeat(x,2,axis=1))
print("\n")
print(np.repeat(x,2,axis=0))
print("\n")
print(np.repeat(x,[2,3],axis=0))
print("\n")

#making a custom matrix using methods
y = np.ones((5,5))
print(y)
print("\n")

z = np.zeros((3,3))
z[1,1] = 9
print(z)
print("\n")

y[1:4,1:4] = z
print(y)
print("\n")

#copying array   
a = np.array([1,2,3,4,5])
b= a.copy()

b[0] = 100
print(a)
print(b)

#arithmatic operation

m = np.array([2,3,4,8])
# a = a + 2
# print(a)

# a = a - 2
# print(a)

#power

m = m ** 2
print(m)

n = np.array([np.pi/6,np.pi/4,np.pi/3,np.pi/2])
print(np.sin(n))