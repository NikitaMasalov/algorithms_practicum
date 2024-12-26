def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    fib_sequence = [0, 1]  
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence


test_values = [35]
results = []

for n in test_values:
    
    fib_sequence = fib(n)
    results.append((n, fib_sequence))


for n, fib_sequence,  in results:
    print(f"fib({n}) = {fib_sequence}")