def fibonacci_sequence(n):
    fib = [0,1]
    if n < 2:
        return fib[:n]
    else:
        for el in range(2, n):
            fib.append(fib[el - 1] + fib[el - 2])
    return fib
