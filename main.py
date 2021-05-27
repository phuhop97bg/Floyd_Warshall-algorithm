import numpy as np
from math import inf as i


#Nhập ma trận dường đi ( hoặc giá, băng thông..)

A_=[[0,1,3,2,i,2],[1,0,1,i,i,i],[3,i,0,i,i,1],[2,i,i,0,1,3],[i,i,i,i,0,3],[2,i,1,3,3,0]]
#Nhập số đỉnh
n=6
A=np.array(A_)
pi=np.zeros((n,n))

for k in range(0,n):
    for i in range(0,n):
        for j in range(0,n):
            if A[i][j]>A[i][k]+A[k][j]:
                pi[i][j]=k+1
                A[i][j]=A[i][k]+A[k][j]

#Ma trận đường đi ngắn nhất
print(A)
#Ma trận gốc pi
print(pi)
