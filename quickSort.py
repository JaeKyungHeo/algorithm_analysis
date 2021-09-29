#1.
import random
import matplotlib.pyplot as plt
            
def partition(s,low,high):
    pivotitem = s[low]
    j = low
    for i in range(low+1,high+1):
        global count
        count += 1
        if s[i] < pivotitem:
            j += 1
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
    pivotpoint = j
    temp = s[low]
    s[low] = s[pivotpoint]
    s[pivotpoint] = temp
    return pivotpoint

def quickSort(s,low, high):
    if high>low:
        pivotpoint = partition(s,low,high)
        quickSort(s,low, pivotpoint-1)
        quickSort(s,pivotpoint+1, high)




#비교할 데이터의 개수 n
#n=8,16,24,32,40에 대하서 각 20개의 데이터를 생성하여 빠른 정렬실행
#실행된 빠른정렬에 대해 비교 횟수를 그래프로 나타내기
N=[8,16,24,32,40]
x=[]
y=[]
for n in N:
    total = 0
    for i in range(20):
        s = [random.randint(0, n) for _ in range(n+1)]
        #print(s)
        count = 0
        quickSort(s,0,n)
        total += count
        #print(count)
    print(total//20)
        #print(s)
    x.append(n)
    y.append(total//20)
#print(x)
#print(y)
plt.plot(x,y)
plt.show()




#2.
from numpy import *
def strassen (n, A, B, C):
    threshold = 2
    A11 = array([[A[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2))])
    A12=array([[A[rows][cols] for cols in range(int(n/2),int(n))]for rows in range(int(n/2))])
    A21=array([[A[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2),int(n))])
    A22=array([[A[rows][cols] for cols in range(int(n/2),int(n))]for rows in range(int(n/2),int(n))])
    B11=array([[B[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2))])
    B12=array([[B[rows][cols] for cols in range(int(n/2),int(n))]for rows in range(int(n/2))])
    B21=array([[B[rows][cols] for cols in range(int(n/2))]for rows in range(int(n/2),int(n))])
    B22=array([[B[rows][cols] for cols in range(int(n/2),int(n))]for rows in range(int(n/2),int(n))])
    # print(A11, A12, A21, A22, B11, B12, B21, B22)
    if (n <= threshold):
        C = array(A) @ array(B)
    else:
        M1 = M2 = M3 = M4 = M5 = M6 = M7 = array([])
        M1=strassen(int(n/2), (A11 + A22) , (B11 + B22), M1)
        M2=strassen(int(n/2),(A21+A22),B11,M2)
        M3=strassen(int(n/2),A11,(B12-B22),M3)
        M4=strassen(int(n/2),A22,(B21-B11),M4)
        M5=strassen(int(n/2),(A11+A12),B22,M5)
        M6=strassen(int(n/2),(A21-A11),(B11+B12),M6)
        M7=strassen(int(n/2),(A12-A22),(B21+B22),M7)
        C = vstack([ hstack([M1+M4 -M5 + M7, M3 + M5]), hstack([M2 + M4, M1 + M3 - M2 + M6]) ])
    return C
n = 4
#A = [[1 for cols in range(n)]for rows in range(n)]
#B = [[2 for cols in range(n)]for rows in range(n)]
A=[ [1,2,0,2], [3,1,0,0], [0,1,1,2],[2,0,2,0]]
B=[ [0,3,0,2], [1,1,4,0], [1,1,0,2],[0,5,2,0]]
C = array(A)@array(B)
D = [[0 for cols in range(n)]for rows in range(n)]
print(C)
D=strassen(n, A, B, D)
print(D)
