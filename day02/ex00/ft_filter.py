#!/usr/bin/env python3

def ft_filter(function_to_apply, list_of_inputs):
	ret = []
	for elem in list_of_inputs:
		if function_to_apply(elem):
			ret.append(elem)
	return ret

l = [1, 2, 3, 4, 5]
print(l)
l = ft_filter(lambda x: x%2 == 0, l)
print(l)
