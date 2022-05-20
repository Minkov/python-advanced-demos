ll = []

print(ll)  # immutable operation

ll.append(1)  # mutable operation

ll.insert(0, -1)  # mutable operation
print(ll[0])  # immutable operation

print(ll)  # immutable operation
ll.pop()  # mutable operation
print(ll)  # immutable operation
ll[0] = -111  # mutable operation
print(ll)  # immutable operation

tt = (1, 2, 3, 4)
tt2 = 1, 2, 3, 4
print(tt)
print(tt[0])
# tt[2] = -3

tt = (1, 2, 3)  # overwrites the value of tt

# single element list/tuple

print([1])
print((1,))
print(())

n = 15

print(list(range(n)))
print(tuple(range(n)))
print(tuple(ll))  # extremely rare case
