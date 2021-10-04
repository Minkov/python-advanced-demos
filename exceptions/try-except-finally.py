def raise_exception():
    int('asdsad')
    pass


def f1():
    try:
        raise_exception()
        return 1
    except ValueError as err:
        return 2
    finally:
        print('Finally from func')


x = f1()
print(x)

try:
    print(' -- Try: start')
    raise_exception()
    print(' -- Try: end')
except TypeError:
    print(' -- Except')
finally:
    print(' -- Finally')

# try:
#     pass
# finally:
#     pass

# try-except
# try-finally
# try-except-finally
