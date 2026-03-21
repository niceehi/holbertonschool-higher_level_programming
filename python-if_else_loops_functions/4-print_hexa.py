#!/usr/bin/python3

for i in range(99):
    k = i % 16

    if k == 10:
        c = 'a'
    elif k == 11:
        c = 'b'
    elif k == 12:
        c = 'c'
    elif k == 13:
        c = 'd'
    elif k == 14:
        c = 'e'
    elif k == 15:
        c = 'f'
    else:
        c = k

    print(i, " = 0x{}".format(c))
