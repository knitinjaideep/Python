#LongestPalindromicSubstring.py
# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
# Example 3:

# Input: s = "a"
# Output: "a"
# Example 4:

# Input: s = "ac"
# Output: "a"

#Time: O(n^2) | Space: O(1)
def longestPalindromicSubstring(s):
	longestLen = 0
	output = [0, 0]
	start = end = 0
	for i in range(len(s)):
		l1, left1,right1 = longestPalindromeLen(s, i, i)
		l2, left2, right2 = longestPalindromeLen(s, i, i + 1)
		longestLen = max(l1, l2)
		if longestLen > end - start:
			if l1 > l2:
				start, end = left1, right1
			else:
				start, end = left2, right2
	return s[start:end]

def longestPalindromeLen(s, l, r):
	while l >= 0 and r < len(s) and s[l] == s[r]:
		l -= 1
		r += 1
	return r - l - 1, l+1, r


print(longestPalindromicSubstring("heefffe"))
