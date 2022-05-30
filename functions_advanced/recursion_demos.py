def reverse_loop(n):
    if n < 0:  # exit case (base) case
        return  # same as `break` in `while` loop

    print(n)
    reverse_loop(n - 1)  # recursive call


def loop(n):
    if n < 0:  # exit case (base) case
        return

    loop(n - 1)  # recursive call
    print(n)


def loop_0():
    # if n < 0: return
    print(0)


def loop_1():
    loop_0()
    print(1)


def loop_2():
    loop_1()
    print(2)


def loop_3():
    loop_2()
    print(3)


def loop_4():
    loop_3()
    print(4)


def loop_5():
    loop_4()
    print(5)


print(' --- Reverse loop ---')
reverse_loop(5)

print(' --- Forward loop ---')
loop(5)
loop_5()
