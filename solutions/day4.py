#!/usr/bin/python3
# Author:	@BlankGodd_

def missing(arr):
    a = sorted(arr)
    x = max(a)
    for i in range(1, x):
        if i not in a:
            return i
    return x+1


if __name__ == "__main__":
    arr1 = [3, 4, -1, 1]
    arr2 = [1, 2, 0]
    print(missing(arr1))
    print(missing(arr2))

