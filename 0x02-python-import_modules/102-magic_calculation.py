#!/usr/bin/python3
def magic_calculation(a, b):

    from magic_calculation_102 import add, sub
    if a < b:
        magic = add(a, b)
        for i in range(4, 6):
            magic = add(i, magic)
        return magic
    else:
        mag_rev = sub(a, b)
        return mag_rev
