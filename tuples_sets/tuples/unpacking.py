tt = (1, 2, 3)

x, y, z = tt
# equivalent to:
x = tt[0]
y = tt[1]
z = tt[2]

print(x)
print(y)
print(z)

ll = list(range(5, 16))

# Here, `index, value` is unpacking of tuple
for index, value in enumerate(ll):
    print(f'll[{index}]={value}')
# equivalent to:
for index in range(len(ll)):
    value = ll[index]
    print(f'll[{index}]={value}')

dd = {
    'one': 1,
    'two': 2,
    'three': 3,
}

# Here, `key, value` is unpacking of tuple
for key, value in dd.items():
    print(f'd[{key}]={value}')

print(dd.items())
print(dd.items())
print(dd.items())
print(dd.items())
print(dd.items())
print(dd.items())
print(dd.items())
print(dd.items())
print(dd.items())
print(dd.items())

# Unpacking works for lists too
ll = ['one', 'two', 'three', 'four']

a, b, c, d = ll
print(a)
print(b)
print(c)
print(d)
