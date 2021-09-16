tt = (1, 2, 3)
x = tt[0]
y = tt[1]
z = tt[2]
print(x, y, z)

# destructuring assignments in JS
a, b, c = tt
print(a, b, c)

i, *j = tt
print(i, j)

dd = {
    'name': 'Gosho',
    'age': 17,
}

print(dd.items())
for key, value in dd.items():
    print(key, value)

x1, y1 = (5, 6)
x1, y1 = (y1, x1)
print(x1, y1)
