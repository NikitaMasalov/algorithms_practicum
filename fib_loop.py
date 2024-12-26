import time

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


test_values = [8, 16, 24, 30, 32]
results = []

for n in test_values:
    start_time = time.perf_counter()  
    result = fib(n)
    end_time = time.perf_counter()  

    elapsed_time = (end_time - start_time) * 1000 
    results.append((n, result, elapsed_time))

# Вывод результатов
for n, result, elapsed_time in results:
    print(f"fib({n}) = {result}, время выполнения: {elapsed_time:.3f} мс")

