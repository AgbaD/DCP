#!usr/bin/python
# author:   @AgbaD | @agba_dr3


from math import sqrt
s = 0


def steps(n):
    global s
    if is_prime(n):
        n -= 1
        s += 1
    else:
        sqt = round(sqrt(n))
        while n % sqt != 0:
            sqt -= 1
        n = n/sqt
        s += 1
    if n != 1:
        steps(n)


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n < 1:
        return False
    return True


if __name__ == "__main__":
    steps(100)
    print(s)

