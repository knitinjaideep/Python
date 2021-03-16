# AdjPalindrome.py
# Given a string, what is the minimum number of adjacent swaps required to convert a string into a palindrome. If not possible, return -1.

# Example 1:

# Input: "mamad"
# Output: 3
# Example 2:

# Input: "asflkj"
# Output: -1
# Example 3:

# Input: "aabb"
# Output: 2
# Example 4:

# Input: "ntiin"
# Output: 1
# Explanation: swap 't' with 'i' => "nitin"

def adjPalin(s):
	if len(s) > 0:
		totalCount = 0
	if isShuffledPalindrome(s):
		p1, p2 = 0, len(s) - 1
	else:
		return -1
	s = [i for i in s]
	while p1 < p2:

		if s[p1] != s[p2]:
			runner = p2
			print(p1,p2,runner)
			while runner >= p1 and s[runner] != s[p1]:
				runner -= 1

				if runner == p1:
					print('here1')
					print(p1,p2,runner)
					s[p1], s[p1 + 1] = s[p1 + 1], s[p1]
					totalCount += 1
				else:
					while runner < p2:
						s[runner], s[runner + 1] = s[runner + 1], s[runner]
						totalCount += 1
						runner += 1
					p1 += 1
					p2 -= 1
		else:
			p1 += 1
			p2 -= 1
	return totalCount
def isShuffledPalindrome(s):
	occurance = [0] * 26
	oddCount = 0
	for i in s:
		occurance[ord(i) - ord('a')] += 1
	for i in occurance:
		if i % 2 != 0:
			oddCount += 1
	return oddCount <= 1


print(adjPalin('mamad'))
print(adjPalin('aabb'))
print(adjPalin('ntiin'))