values = ['Pesho', 'Doncho', 'Gosho']

print(
    [-ord(x) for x in 'Doncho']
)

print(
    sorted(
        values,
        key=lambda x: [-ord(c) for c in x],
    )
)
