#!/usr/bin/python3
# Author:	@BlankGodd_

import re

class Node:
	def __init__(self, var, left=None, right=None):
	self.left = left
	self.var = var
	self.right = right

def serialize(a):
	return "f{a}"

def deserialize(a):
	# if it gets pattern for 'Node('
	# deserialize value after ( before ,(if any)
	# if not, Node.var = value
	# if ), current Node done
