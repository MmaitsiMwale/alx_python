def fibonacci_sequence(n):
    fib = [0, 1]
    for el in range(2, n):
        fib.append(fib[el - 1] + fib[el - 2])
    return fib
