import time

ll = list(range(1024*32))
ss = set(ll)

result = False
start = time.time()
for v in ss:
    result = v in ss
end = time.time()
print(f'Set: {end - start} s')

result = False
start = time.time()
for v in ll:
    result = v in ll
end = time.time()
print(f'List: {end - start} s')


#
# for v in ll:
#     result = v in ll
#
# for v in ll:
#     for v2 in ll:
#         if v == v2: # 32000 * 32000 = 1 024 000 000
#             return True
#     return False