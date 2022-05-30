def get_info(name, town, age):
    return f'This is {name} from {town} and he is {age} years old'


info1 = {
    'name': 'Pesho',
    'town': 'Burgas',
    'age': 18,
}

info2 = {
    'name': 'Gosho',
    'town': 'Stara Zagora',
    'age': 48,
}

print(f(**info1))
print(f(**info2))
