def fib(n):
    '''Fibonacci Sequence'''
    x = [0]*n
    for i in range(n):
        if i == 0:
            x[i] = 0
        elif i == 1:
            x[i] = 1
        else:
            x[i] = x[i-2] + x[i-1]
    return x
