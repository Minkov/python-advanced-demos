def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    if not isinstance(length, int) \
            or not isinstance(width, int):
        return 'Enter valid values!'

    return f'''Rectangle area: {area()}
Rectangle perimeter: {perimeter()}'''


print(rectangle(2, 10))
print(rectangle('2', 10))
