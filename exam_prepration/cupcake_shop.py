'''
https://judge.softuni.org/Contests/Practice/Index/2812#2
'''

def stock_availability(inventory, command, *args):
    if command == 'delivery':
        return inventory + list(args)

    if not args or isinstance(args[0], int):
    # if not args or str(args[0]).isdigit(): Don't do this
        count = args[0] if args else 1
        return inventory[count:]

    sold_items = set(args)

    return [item for item in inventory if item not in sold_items]


print(stock_availability(['choco', 'vanilla', 'banana'], 'delivery', 'caramel', 'berry'))
print(stock_availability(['chocolate', 'vanilla', 'banana'], 'delivery', 'cookie', 'banana'))
print(stock_availability(['chocolate', 'vanilla', 'banana'], 'sell'))
print(stock_availability(['chocolate', 'vanilla', 'banana'], 'sell', 3))
print(stock_availability(['chocolate', 'vanilla', 'banana'], 'sell', 2))
print(stock_availability(['chocolate', 'chocolate', 'banana'], 'sell', 'chocolate'))
print(stock_availability(['cookie', 'chocolate', 'banana'], 'sell', 'chocolate'))
print(stock_availability(['cookie', 'chocolate', 'banana'], 'sell', 'chocolate', 'banana'))
print(stock_availability(['chocolate', 'vanilla', 'banana'], 'sell', 'cookie'))
print(stock_availability(['chocolate', 'vanilla', 'banana'], 'sell', 'cookie', 'banana'))
