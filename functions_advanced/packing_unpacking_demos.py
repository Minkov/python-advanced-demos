ll = [1, 2, 3, 4]
# tt = (1, 2, 3, 4)

x, y, z, a = ll

print(x)
print(y)
print(z)
print(a)

k, l, *r = ll

print(k)
print(l)
print(r)

k, *l, r = ll
(k, *l, r) = ll

print(k)
print(l)
print(r)

k, *_, r = ll

print(k)
print(r)


