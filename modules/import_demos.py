# custom modules
import os  # 1

# built-in or third-party modules
from os import listdir  # 2
from os import listdir as ls  # 2.2

from os import *  # 3, not a good way.

# ZoP -> better explicit, than implicit

print(
    os.listdir('./')  # 1
)

print(
    listdir('./')  # 2
)

print(
    ls('./')  # 2.2
)

print(
    listdir('./')  # 3
)
print(
    linesep  # 3
)
