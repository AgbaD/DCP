#!/usr/bin/python3
# Author: @AgbaD | @Agba_dr3

class Node:
	def __init__(self, var, left=None, right=None):
		self.left = left
		self.var = var
		self.right = right

	@classmethod
	def from_str(cls, string):
		a = string.split(',')
		for i in range(len(a)):
			if a[i] == "Node":
				a[i+1] = ''.join(['(', a[i+1]])
		print(a)


if __name__ == "__main__":
	node = "Node('root', Node('left', Node('left.left')), Node('right'))"
	Node.from_str(node)
