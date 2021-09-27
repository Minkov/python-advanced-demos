'''
ab (n=2)
=>
ab
ba

abc (n=3)
=>
a bc
a cb
b ac
b ca
c ab
c ba

abcd (n=4)
abcd

=>
a bcd
a bdc
a cbd
a cdb
a dbc
a dcb

b acd
b adc
b cad
b cda
b dac
b dca
'''


# Example here: https://media.geeksforgeeks.org/wp-content/cdn-uploads/NewPermutation.gif
def permute(index, values):
    if index == len(values):
        print(''.join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permute(index + 1, values)
        values[i], values[index] = values[index], values[i]


permute(0, list('abc'))