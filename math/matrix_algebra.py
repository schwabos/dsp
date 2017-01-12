# Matrix Algebra
import numpy as N 
from numpy import matrix
from numpy import linalg


a = 6
A = N.matrix('1 2 3; 2 7 4')
B = N.matrix('1 -1; 0 1')
C = N.matrix('5 -1; 9 1; 6 0')
D = N.matrix('3 -2 -1; 1 2 3')
u = N.matrix('6 2 -3 5')
v = N.matrix('3 5 -1 4')
w = N.matrix('1; 8; 0; 5')

# 1. Dimensions
print(N.shape(A))
print(N.shape(B))
print(N.shape(C))
print(N.shape(D))
print(N.shape(u))
print(N.shape(w))

# 2. Vectory Operations
print(u+v)
print(u-v)
print(a*u)
print(N.inner(u,v))
print(linalg.norm(u))

# 3. Matrix Operations
# print(A+C) NOT DEFINED
print(A-C.T)
print(C.T+3*D)
print(B*A)
# print(B*A.T) NOT DEFINED

# Optional
# print(B*C) NOT DEFINED
print(C*B)
print(B*B*B*B)
print(A*A.T)
print(D.T*D)
