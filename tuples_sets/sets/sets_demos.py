'''
Sets:

- Search, add, remove is very, very, very fast
- Contains only unique values
    - *unique values
- Unordered (with hash tables)
- Ordered (with tree)
'''

ss = {1, 2, 3, 4, 5}
[ss.add(6) for _ in range(1024)]
print(ss)

# add
ss.add(8)
print(ss)

# remove
ss.remove(4)
print(ss)
# ss.remove(4) # raises exception
# print(ss)

# check if value is in set
print(4 in ss)
print(5 in ss)
ss.add(4)
print(4 in ss)
ss.remove(4)
print(len(ss))
# This is an empty dict, not a set
ddd = {}
# This is an empty set
sss = set()
