import numpy as np

a = np.ones((2,3))
# print(a)

b = np.full((3,4),2,dtype=int)
# print(b)

c = np.matmul(a,b)
print(c)
print("\n")

#determinant 
x = np.identity(3)
print(np.linalg.det(x))

print(np.trace(x))

y = np.arange(16).reshape(4,4)
print(y)
print(np.trace(y))

