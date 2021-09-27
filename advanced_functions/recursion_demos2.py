def loop(index, max_index):
    print(f' -- starting loop({index},{max_index} ) -- ')
    if index == max_index:
        print(f' -- ending loop({index},{max_index} ) -- ')
        return  # base case, exit condition

    print(index)
    loop(index=index + 1, max_index=max_index)  # recursive call

    print(f' -- ending loop({index},{max_index} ) -- ')


loop(0, 1024)


def loop3():
    return


def loop2():
    print(2)
    loop3()


def loop1():
    print(1)
    loop2()


def loop0():
    print(0)
    loop1()


loop0()
