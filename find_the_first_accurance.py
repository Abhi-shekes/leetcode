class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_of_needle = len(needle)
        if needle in haystack:
            for i in range(len(haystack) - len_of_needle + 1):
                if haystack[i:i+len_of_needle] == needle:
                    return i
                
        else:
            return -1