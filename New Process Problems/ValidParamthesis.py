#ValidParamthesis.py

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

#Time: O(n) | space: O(n)
#O(n) time: Becasue we navigate through the entire string once
#O(n) space because if the string is all open brackets ((([[..., then we end up appending all the characters to the string

def validParanthesis(s):
	lookup = {'(':')', '{':'}', '[':']'}
	stck = []
	for char in s:	
		if char in lookup:
			stck.append(char)
		elif char not in lookup and lookup[stck.pop()] != char:
			return False
	return not stck


s = "()"
s1 = "()[]{}"
s2 = "(]"
s3 = "([)]"
print(validParanthesis(s))
print(validParanthesis(s1))
print(validParanthesis(s2))
print(validParanthesis(s3))