def fib(n):
    old, new = 2, 1
    for _ in range(n):
        old, new = new, old + new
    return old