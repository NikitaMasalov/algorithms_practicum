def fib_eo(n):
    if n <= 0:
        raise ValueError("n должно быть больше или равно 1.")
    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10

    return "чётное" if b % 2 == 0 else "нечётное"

n = 43798398
result = fib_eo(n)
print(f"Число {n}-е число Фибоначчи {result}.")
