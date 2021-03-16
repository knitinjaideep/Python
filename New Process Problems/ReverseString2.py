#ReverseString2.py
# Given an input string , reverse the string word by word. 

# Example:

# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Note: 

# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.

# Follow up: Could you do it in-place without allocating extra space?

#Time: O(N) | Space: O(1)

def reverseWords(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    reverse(s, 0, len(s) - 1)
    return reverseEachWord(s)
    
def reverse(s, left, right):
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

def reverseEachWord(s):
    n = len(s)
    start = end = 0
    
    while start < n:
        while end < n and s[end] != ' ':
            end += 1
        reverse(s, start, end-1)
        start = end + 1
        end += 1
    return s

print(reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))

