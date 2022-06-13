def read_until_command(command, map_func=None):
    result = []
    while True:
        line = input()
        if line == command:
            break
        result.append(line)

    if map_func is None:
        return result

    return [map_func(x) for x in result]
