import termcolor

import pyfiglet

print(
    termcolor.colored('It works!', 'red', )
)

print(
    termcolor.colored('It works!', 'red', attrs=['underline'])
)

print(
    termcolor.colored('It works!', 'red', attrs=['bold'])
)

print(
    termcolor.colored('It works!', 'red', attrs=['bold', 'underline'])
)

print(
    pyfiglet.figlet_format('It, works!', font='isometric1')
)
