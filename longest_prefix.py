class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        
        first_word = strs[0]
        
        for i in range(len(first_word)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != first_word[i]:
                    return first_word[:i]
        
        return first_word