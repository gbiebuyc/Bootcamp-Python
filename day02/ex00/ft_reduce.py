#!/usr/bin/env python3

def ft_reduce(function_to_apply, list_of_inputs):
	ret = list_of_inputs[0]
	for i in range(1, len(list_of_inputs)):
		ret = function_to_apply(ret, list_of_inputs[i])
	return ret


l = [1, 2, 3, 4, 5]
print(l)
l = ft_reduce(lambda x, y: x+y, l)
print(l)
