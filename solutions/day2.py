#!/usr/bin/python3
# Author: @AgbaD | @Agba_dr3

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
	l = input("Enter a space separated list of integers \n:")
	a = l.split(" ")
	a = [int(i) for i in a]
	print(pro(a))
