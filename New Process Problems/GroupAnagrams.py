#GroupAnagrams.py
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

#Time: O(nk) - where n is the total number of words and k is the total length of each word
import collections
def groupAnagrams(strs):
	ans = collections.defaultdict(list)
	for s in strs:
		count = [0] * 26
		for c in s:
			count[ord(c) - ord('a')] += 1

		ans[tuple(count)].append(s)
	return ans.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
