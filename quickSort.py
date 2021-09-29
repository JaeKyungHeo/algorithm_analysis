#1.
import random
import matplotlib.pyplot as plt

def exchange(i, j):
    temp = i
    i = j
    j = temp
            
def partition(s,low,high):
    pivotitem = s[low]
    j = low
    for i in range(low+1,high+1):
        if s[i] < pivotitem:
            global count
            count += 1
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
