try:
    raise ValueError
# except ValueError:
#     print('Value exception')
# except Exception:
#     print('Base Exception')
except:
    print('Exception')


def read_until_int():
    while True:
        try:
            return int(input())
        except ValueError:
            print('Not an integer. Try again!')


print(
    read_until_int()
)
