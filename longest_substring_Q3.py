# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
#
# leetcode, algorithm question #3


class Solution(object):

	## Naive Solution, beats 38.30% of submissions, Runtime: 124 ms
	'''
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_string = ''
        if len(s) > 0:
	        curString = s[0]
	        for i in range(1, len(s)):
	        	if s[i] not in curString:
	        		curString = curString + s[i]
	        	else:
	        		if len(curString) > len(max_string):
	        			max_string = curString
	        		curString = curString.split(s[i])[1] + s[i]
	        	i = i + 1

	        if len(curString) > len(max_string):
	        	max_string = curString
	        # print max_string
        return len(max_string)
    '''

	## KMP Algorithm Version
	## Beats 98.34% of submissions: Runtime: 88 ms
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		lastRepeating = -1
		longestSubstring = 0
		positions = {}
		for i in range(0, len(s)):
			if s[i] in positions and lastRepeating<positions[s[i]]:
				lastRepeating = positions[s[i]]
			if i-lastRepeating > longestSubstring:
				longestSubstring = i-lastRepeating
			positions [s[i]]=i
		print positions
		return longestSubstring



sol = Solution()
s = "abcdeabcbb"
longest_substring_len = sol.lengthOfLongestSubstring(s)
print "The length of the longest non-repeative substring for ", s, " is ", longest_substring_len

s = "bbbbbbb"
longest_substring_len = sol.lengthOfLongestSubstring(s)
print "The length of the longest non-repeative substring for ", s, " is ", longest_substring_len

s = "awkweq"
longest_substring_len = sol.lengthOfLongestSubstring(s)
print "The length of the longest non-repeative substring for ", s, " is ", longest_substring_len

s = "c"
longest_substring_len = sol.lengthOfLongestSubstring(s)
print "The length of the longest non-repeative substring for ", s, " is ", longest_substring_len

s = "au"
longest_substring_len = sol.lengthOfLongestSubstring(s)
print "The length of the longest non-repeative substring for ", s, " is ", longest_substring_len

s = ""
longest_substring_len = sol.lengthOfLongestSubstring(s)
print "The length of the longest non-repeative substring for ", s, " is ", longest_substring_len

s = "dvdf"
longest_substring_len = sol.lengthOfLongestSubstring(s)
print "The length of the longest non-repeative substring for ", s, " is ", longest_substring_len