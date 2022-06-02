class ValueTooSmallException(Exception):
    pass


# Value should only contain '1' and '0'
str_value = input()

for x in str_value:
    if x not in ['0', '1']:
        raise ValueError('The input should contain only \'0\'s and \'1\'s')

value = int(str_value)

if value < 10:
    raise ValueTooSmallException(
        f'{value} should be equal or greater than 10')
