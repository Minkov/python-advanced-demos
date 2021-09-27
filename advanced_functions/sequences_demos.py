# Factorial
# f(n) = f(n-1) * n
# f(1) = 1
# f(0) = 1

def factorial(n):
    print(f'Calculating f({n})')
    if n == 0 or n == 1:
        return 1

    result = n * factorial(n - 1)
    print(f'f({n})={result}')

    return result


def factorial2(n):
    print(f'Calculating f({n})')
    if n > 1:
        result = n * factorial(n - 1)
        print(f'f({n})={result}')

        return result
    return 1


factorial(10)
factorial2(10)

# Fibonacci
# f(n) = f(n-1)+f(n-2)
# f(0) = 0
# f(1) = 1

counts = {
    'x': 0
}


# memoization?
def fibonacci(n):
    counts['x'] += 1
    if n == 0:
        return 0
    if n == 1:
        return 1

    result = fibonacci(n - 1) + fibonacci(n - 2)
    return result


print(fibonacci(15))
print(counts)
# print(fibonacci(15))
