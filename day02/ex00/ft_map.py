#!/usr/bin/env python3

def ft_map(function_to_apply, list_of_inputs):
	ret = [None] * len(list_of_inputs)
	for i in range(len(list_of_inputs)):
		ret[i] = function_to_apply(list_of_inputs[i])
	return ret

l = [1, 2, 3, 4, 5]
print(l)
l = ft_map(lambda x: x+1, l)
print(l)
