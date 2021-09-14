import timeit

def fun(n):
    a = [0]*(n+2)
    a[1] = 1
    a[2] = 1
    sum = 2
    for i in range(3,n+2):
        a[i] = sum
        sum += a[i]
    return a[n]


n = int(input())

start_time = timeit.default_timer()#시작시간


fun(n)


terminate_time = timeit.default_timer()#종료시간

print((terminate_time - start_time))
