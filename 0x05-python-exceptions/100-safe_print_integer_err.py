#!/usr/bin/python3

def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))

    except (ValueError, TypeError) as err:
        import sys
        print("Exception: {}".format(err), file=sys.sderr)
        return False

    else:
        return True
