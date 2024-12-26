import math

def fib(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2  
    psi = (1 - sqrt_5) / 2 

    fib_n = (phi**n - psi**n) / sqrt_5
    return round(fib_n)

test_values = [10, 20, 32, 50, 64]
results = []

for n in test_values:  
    result = fib(n)
    results.append((n, result, round(3)))

for n, result, elapsed_time in results:
    print(f"fib({n}) = {result}")


