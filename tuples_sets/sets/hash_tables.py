ll = [None, None, None, None]


def get_index(value):
    return hash(value) % len(ll)


def add(value):
    index = get_index(value)
    if ll[index] is None:
        ll[index] = []
    ll[index].append(value)


add(1)
print(ll)
add(16)
print(ll)
add(7)
print(ll)
add(4)
print(ll)
add(8)
print(ll)
add(9)
print(ll)
add(1)
print(ll)
add(3)
print(ll)
add(33)
print(ll)
add('Doncho')
print(ll)

print(', '.join(str(hash(x)) for x in range(16)))
print(hash('Doncho'))
print(hash('Minkov'))