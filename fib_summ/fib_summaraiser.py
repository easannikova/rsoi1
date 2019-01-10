import random

fib = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584)

def sum_fibonachi(n):
    i = 0
    sum = 0
    while i <= n:
        sum += fib[i]
        i+=1
    return sum

def fibonachi():
    n = random.randint(0, 15)
    res = 'Summary of first ' + str(n+1) + ' numbers of fibonacci series is ' + str(sum_fibonachi(n))
    return res

if __name__ == "__main__":
    print(fibonachi())