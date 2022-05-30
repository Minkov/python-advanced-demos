# n! = n * (n-1)!
# 1! = 1
# 0! = 1

def fact(n):
    if n in (0, 1):
        return 1

    n_1_fact = fact(n - 1)
    return n * n_1_fact


# [print(fact(x)) for x in range(5)]
print(fact(5))
