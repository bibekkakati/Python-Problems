"""
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.
"""
arr = [2, 4, 6, 8, 10, 2, 6, 10]

res = []

for i in arr:
	num = arr.count(i)
	if(num == 1):
		res.append(i)


print(set(res))