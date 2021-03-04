#ThreeSum
#Tips to remember 3sum
#Sort, 2 loops

#O(n^2) time and O(n) space
def ThreeSum(array, target):
	array.sort()
	triplets = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			curr_sum = array[i] + array[left] + array[right]
			if curr_sum == target:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif curr_sum < target:
				left += 1
			elif curr_sum > target:
				right -= 1
	return triplets


print(ThreeSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
print(ThreeSum([8, 10, -2, 49, 14], 57))
#Walkthrough:
#8, 10, -2, 49, 14

#1st					|   curr_sum = -2 + 8 + 49 = 55
#  i  l            r    |	so curr_sum is < target, and  
# -2  8  10  14  49		|	left += 1 will get executed

#2nd					|   curr_sum = -2 + 10 + 49 = 57
#  i      l       r     |   MATCH! Triplets will add them
# -2  8  10  14  49		|   l and r will + and - respectively and exit out of while loop

#3rd					|   curr_sum = 8 + 10 + 49 = 67
#     i   l       r     |   Curr_sum > target, and
# -2  8  10  14  49		|   r -= 1 will be executed

#4th					|   curr_sum = 8 + 10 + 14 = 32
#     i   l   r     	|   Curr_sum > target, and
# -2  8  10  14  49		|   l will + and exit out of while loop

#5th					|   curr_sum = 10 + 14 + 49 = 73
#         i   l   r  	|   Curr_sum > target, and
# -2  8  10  14  49		|   r will - and exit out of while loop

#Finally i will increment and l and r will be equal so the for loop also will exit and Triplets will be returned


