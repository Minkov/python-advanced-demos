# ll = []
#
# # Push, add, append
# ll.append(1) - correct
# ll.insert(0, 1) - very wrong
#
# # Pop, remove
# ll.pop() - correct
# ll.pop(0) - very wrong
#
# # Peek
# print(ll[-1]) - correct
# print(ll[0]) - very wrong
#
# # Len, count, size
# print(len(ll))


# Stack implemented with list, resizing array
# (other) Stack implemented as linked list
s = []  # This is a stack

# Pushes
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
s.append(7)
s.append(8)
print(s)

# Peek
print(s[-1])  # s[len(s) -1]
print(s)

# s.insert(2, 15) # This is not a stack operation

# Pop
s.pop()
print(s)

# Push
s.append(9)
print(s)

# Not stack operations
# s.insert()
# s.reverse()
# s.count()
# s.sort()
# s.pop(0)
# s[0]
