import timeit

def fun(n):
    if n == 1 or n == 2:
        return 1
    else:
        total = 0
        for i in range(1, n):
            total += fun(i)
        return total


n = int(input())

start_time = timeit.default_timer()#시작시간

fun(n)

terminate_time = timeit.default_timer()#종료시간

print((terminate_time - start_time))
