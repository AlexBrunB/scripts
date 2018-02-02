#!/usr/bin/env python

import sys
import random

def generate_list(n):
	list = []
	for x in range(n):
		list.append(random.randint(0,100))
	return list


def split_list(list):
	list_1 = []
	list_2 = []
	list_3 = []
	for x in list:
		if sum(list_1) > sum(list_2):
			if sum(list_2) > sum(list_3):
				list_3.append(x);
			else:
				list_2.append(x);
		elif sum(list_2) > sum(list_3):
			list_3.append(x);
		elif sum(list_3)> sum(list_1):
			list_1.append(x);
		else :
			list_1.append(x);
	return list_1, list_2, list_3




if __name__ == "__main__":
	sys.argv[1]
	list = generate_list( int(sys.argv[1])); 
	print list;
	l1, l2, l3 = split_list(list);
	print sum(l1), sum(l2), sum(l3)
	
