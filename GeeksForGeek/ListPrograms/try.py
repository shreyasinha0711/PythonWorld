
def fib_fn(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_fn(n-1) + fib_fn(n-2)

for i in range(10):
    print(fib_fn(i))

