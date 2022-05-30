def f1(x):
    def inner_f1(y):
        return x + y

    return inner_f1


func1 = f1(5)
print(func1)
print(func1(6))
print(func1(5))
print(func1(4))

func2 = f1(-5)
print(func2)
print(func2(6))
print(func2(5))
print(func2(4))
