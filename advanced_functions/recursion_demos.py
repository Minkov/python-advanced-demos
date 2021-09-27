n = 3

for i in range(n):
    print(i)

index = 0
while True:
    if index == n:
        break  # base case, exit condition

    print(index)
    index += 1


def loop(index, max_index):
    if index == max_index:
        return  # base case, exit condition

    print(index)
    loop(index=index + 1, max_index=max_index)  # recursive call


loop(index=0, max_index=n)
