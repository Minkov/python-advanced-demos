generated_sequence = []


def create_sequence(n):
    while generated_sequence:
        generated_sequence.pop()

    generated_sequence.append(0)
    generated_sequence.append(1)

    for _ in range(n - 2):
        generated_sequence.append(
            generated_sequence[-1] + generated_sequence[-2]
        )
    return generated_sequence


def locate(x):
    if x in generated_sequence:
        return generated_sequence.index(x)

    return None
