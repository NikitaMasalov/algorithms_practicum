import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


test_values = [2, 6, 13, 19, 24]
results = []

for n in test_values:
    start_time = time.time()  
    result = fib(n)
    end_time = time.time() 

    elapsed_time = (end_time - start_time) * 1000  
    results.append((n, result, elapsed_time))

for n, result, elapsed_time in results:
    print(f"fib({n}) = {result}, время выполнения: {elapsed_time:.3f} мс")
