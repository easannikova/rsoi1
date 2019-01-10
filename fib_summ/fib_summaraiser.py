import random

fib = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584)

def sum_fibonachi(n):
    i = 0
    sum = 0
    while i <= n:
        sum += fib[i]
        i+=1
    return sum

if __name__ == "__main__":
    n = random.randint(0, 15)
    print('Summary of first', n+1, 'numbers of fibonacci series is', sum_fibonachi(n))