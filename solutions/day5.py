#!/usr/bin/python3
# Author: @AgbaD | @Agba_dr3

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def grace(a, b):
    return tuple([a, b])


def car(pair):
    p = pair(grace)
    return p[0]


def cdr(pair):
    p = pair(grace)
    return p[-1]


if __name__ == "__main__":
    a, b = 3, 4
    print(car(cons(a, b)))
    print(cdr(cons(a, b)))
