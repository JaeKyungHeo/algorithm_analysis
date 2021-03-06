import utility

def order(p,i,j):
    if i == j:
        print('A', i, end = '')
    else:
        k = p[i][j]
        print('(', end = '')
        order(p,i,k)
        order(p,k+1,j)
        print(')', end = '')      


d=[5,2,3,4,6,7,8]
n=len(d)-1
m=[[0 for j in range(1,n+2)] for i in range(1,n+2)]
p=[[0 for j in range(1,n+2)] for i in range(1,n+2)]

for i in range(1,n+1):
    m[i][i] = 0
for diagonal in range(1,n):
    for i in range(1,n-diagonal + 1):
        j = i + diagonal
        m[i][j] = m[i][i] + m[i+1][j] + d[i-1]*d[i]*d[j]
        p[i][j] = i
        for k in range(i+1,j):
            if m[i][j] > m[i][k] + m[k+1][j] + d[i-1]*d[k]*d[j]:
                m[i][j] = m[i][k] + m[k+1][j] + d[i-1]*d[k]*d[j]
                p[i][j] = k


utility.printMatrix(m)
print()
utility.printMatrix(p)
order(p,1,6)
