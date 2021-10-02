arr = [0]*17
count = [0]*17
arr2 = [0]*17
count2 = [0]*17
def merge(h,m,u,v,s):
    i = j = k = 0
    while i<h and j<m:
        if u[i]<v[j]:
            s[k] = u[i]
            i += 1
        else:
            s[k] = v[j]
            j += 1
        k += 1
    if i >= h:
        for t in range(j,m):
            s[k] = v[t]
            k += 1
    else:
        for t in range(i,h):
            s[k] = u[t]
            k += 1
           

def mergeSort(n, s):
    h = n // 2
    m = n - h
    u = s[:h]
    arr[len(u)] += 1
    if arr[len(u)]>count[len(u)]:
            count[len(u)] = arr[len(u)]
    v = s[h:]
    arr[len(v)] += 1
    if arr[len(v)]>count[len(v)]:
        count[len(v)] = arr[len(v)]
    
    if n>1:
        arr[len(u)] -= 1
        mergeSort(h, u)
        arr[len(v)] -= 1
        mergeSort(m, v)
        #print(h,'+',m, u,v)
        merge(h,m,u,v,s)
    else:
        arr[len(u)] -= 1
        arr[len(v)] -= 1


def merge2(s,low, mid, high):
    u = [0]*(high-low+1)
    arr2[mid-low+1] += 1
    if arr2[mid-low+1]>count2[mid-low+1]:
            count2[mid-low+1] = arr2[mid-low+1]
    i = low
    j = mid + 1
    k = 0
    while i <= mid and j<= high:
        if s[i] < s[j]:
            u[k] = s[i]
            i += 1
        else:
            u[k] = s[j]
            j += 1
        k += 1
    if i > mid:
        for t in range(j,high+1):
            u[k] = s[t]
            k +=1
    else:
        for t in range(i,mid+1):
            u[k] = s[t]
            k += 1
    for t in range(low, high+1):
        s[t] = u[t-low]
    arr2[mid-low+1] -= 1


def mergeSort2(s,low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort2(s,low,mid)
        mergeSort2(s,mid+1,high)
        merge2(s,low,mid,high)


print("합병정렬")
s = [11,5,2,16,12,1,8,15,6,14,9,3,10,7,13,4]
print("정렬전 -",s)
mergeSort(len(s),s)
#print("추가 공간")
total = 0
#print("(크기x공간수)")
for i in range(1,len(count)-1):
    if count[i] > 0:
        print(i,'x',count[i])
        total += (i*count[i])
print("총 추가 공간:",total)
print("정렬후 -",s)
print()


print("합병정렬2")
s = [11,5,2,16,12,1,8,15,6,14,9,3,10,7,13,4]
print("정렬전 -",s)
mergeSort2(s,0,len(s)-1)
total2 = 0
for i in range(1,len(count2)-1):
    if count2[i] > 0:
        print(i,'x',count2[i])
        total2 += (i*count2[i])
print("총 추가 공간:",total2)
print("정렬후 -",s)
