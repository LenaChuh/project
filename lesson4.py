# Задача1
import itertools
from sys import argv
from itertools import cycle
import functools

name, v, s, p = argv


def zp(v, s, p):
    return int(v) * int(s) + int(p)


print('расчитанная зарплата:  ', zp(v, s, p))

# Задача2

ll = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

ll1 = [ll[x + 1] for x in range(0, len(ll) - 1) if ll[x + 1] > ll[x]]

# Задача3

h = [x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0]

# Задача4
k = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
f = [x for x in k if k.count(x) == 1]

# Задача5

lis = [x for x in range(100, 1000, 2)]

print("The product of the list elements is : ")
print(functools.reduce(lambda a, b: a * b, lis))

# Задача6
g = itertools.count(start=2, step=1)

for e in g:
    if e < 28:
        print(next(g))
    else:
        break


c = 0
for el in cycle("A T N".split()):
    if c > 10:
        break
    print(el)
    c += 1


# Задача7

def fact(n):
    mist = range(1, n + 1)
    p = 1
    for i in mist:
        p *= i
        yield p


for x in fact(6):
    print(x)
