#Two sum
#O(n) time and O(n) space

#Tips to remember 2 sum:
#For O(n) time and O(n) space use dictionary/set and keep storing every character in dictionary
#For O(nlogn) time and O(1) space sort the array and have 2 pointers, one from start and other from end and have them move towards eachother

#TwoSum With one solution
def TwoSum(arr, target):
	d = {}
	for i in range(len(arr)):
		if target - arr[i] in d:
			return [arr[i], target - arr[i]]
		d[arr[i]] = True
	return []

#O(nlogn) time and O(1) space
def TwoSum1(arr, target):
	arr.sort()
	i, j = 0, len(arr) - 1
	while i < j:
		if arr[i] + arr[j] == target:
			return [arr[i], arr[j]]
		elif arr[i] + arr[j] > target:
			j -= 1
		else:
			i += 1
	return []

#O(nlogn) time and O(n) space
#This will give all the paits
def TwoSum2(arr, target):
	d = {}
	output = []
	for i in range(len(arr)):
		if target - arr[i] in d and sorted([arr[i], target - arr[i]]) not in output:
			output.append(sorted([arr[i], target - arr[i]])) 
		d[arr[i]] = True
	return output

print(TwoSum([1,4,6,3,-2], 1))
print(TwoSum1([1,4,6,3,-2], 1))
print(TwoSum2([1,4,6,3,-2,7,4], 10))

