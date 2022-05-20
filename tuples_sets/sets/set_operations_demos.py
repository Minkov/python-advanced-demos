s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {1, 3, 4, 5}

print(f's1 = {s1}')
print(f's2 = {s2}')
print(f's3 = {s3}')

print(f'{s1} | {s2} = {s1 | s2}')
print(f'{s1}.union({s2}) = {s1.union(s2)}')
print(f'{s1} & {s2} = {s1 & s2}')
print(f'{s1}.intersection({s2}) = {s1.intersection(s2)}')

print(f'{s2}.issubset({s3}) = {s2.issubset(s3)}')
print(f'{s3}.issubset({s3}) = {s3.issubset(s3)}')
