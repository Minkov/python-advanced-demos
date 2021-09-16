# ss = set()
# ll = []
# ss.add(1)
# ss.add(2)
# ss.add(1)
# ss.add(3)
# print(ss)
#
# for _ in range(10):
#     ss.add(1)
#     ll.append(1)
# print(ss)
# print(ll)


s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1)
print(s2)
print(s1 | s2)
print(s1 & s2)
print(s1 < s2)
print(s1 < s1)
print(s1 <= s1)
print(s1 - s2)
print(s2 - s1)
print(s1 ^ s2)
# same as
print((s1 | s2) - (s1 & s2))

print(
    {x % 5 for x in range(15)}
)

print({})
print(dict())
print(set())
print({1, 2, 3, })
