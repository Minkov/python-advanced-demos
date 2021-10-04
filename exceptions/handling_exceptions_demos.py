def raise_exception():
    # raise TypeError
    # x = {}['asd']
    x = [1][1]

    pass


try:
    raise_exception()
    print('No exception')
# except IndexError as err:
#     print(f'Index Exception handled: {err}')
# except KeyError:
#     print('Key Exception handled')
except (IndexError, KeyError) as err:
    print(f'Index/Key Exception handled: {err}')
except LookupError as err:
    print(f'Lookup Exception handled: {err}')
except Exception:
    print('General Exception handled')

print('End')

try:
    raise_exception()
except Exception as err:
    if isinstance(err, KeyError) or \
            isinstance(err, IndexError):
        print(f'Index/Key Exception handled: {err}')
    elif isinstance(err, LookupError):
        print(f'Lookup Exception handled: {err}')
    else:
        print('General Exception handled')
