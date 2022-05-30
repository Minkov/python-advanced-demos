# ll1 = [1, 2, 3, 4]
#
# k, l, *r = ll1
# print(k, l, r)
#
# ll2 = [-1, *ll1, -2]
# print(ll2)
# print(ll2[4])
#
# dd1 = {
#     'x': 1,
#     'y': 2
# }
#
# dd2 = {
#     'z': 3,
#     **dd1,
# }
#
# print(dd2)

def f(*args, **kwargs):
    print(f'args={args}, kwargs={kwargs}')


def shame_doncho(Doncho, **kwargs):
    print(f'Doncho has {Doncho}. He is stupid!')


def congrat_maria(Maria, **kwargs):
    print(f'Maria has {Maria}. She is smart!')


numbers = [1, 2, 3, 4, 5]
grades_dict = {
    'Doncho': 3,
    'Ivan': 4,
    'Maria': 6,
    'Pesho': 4.5,
}

shame_doncho(**grades_dict)
shame_doncho(Doncho=3, Ivan=4, Maria=6, Pesho=4.5)
congrat_maria(**grades_dict)

f(*numbers)
f(numbers)
f(**grades_dict)
f(grades_dict)
f(*numbers, **grades_dict)
f(numbers, grades_dict)
