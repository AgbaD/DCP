#!/usr/bin/python3
# Author:	@BlankGodd_

def pro(a):
	c = []
	d = [i for i in range(len(a))]
	for i in range(len(a)):
		n = 1
		for j in d:
			if i == j:
				pass
			else:
				n *= a[j]
		c.append(n)
		n = 1
	return c

if __name__ == "__main__":
	l = input("Enter a space seperated list of integers \n:")
	a = l.split(" ")
	a = [int(i) for i in a]
	print(pro(a))
