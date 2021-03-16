#ValidPalindrome.py
#s = 'A man, a plan, a canal: Pamana'
#Output = True
#Explanation: "amanaplanacanalpamana" is a palindrome
#Time Complexity: O(n) | space: O(1)
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    left = 0
    right = len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True


print(isPalindrome('A man, a plan, a canal: Pamana'))