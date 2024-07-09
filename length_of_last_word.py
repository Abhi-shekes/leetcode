class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        right = len(s) - 1
 

        while right != -1:
            if s[right] == " " and counter == 0:
                right = right - 1
            elif s[right]!= " ":
                counter = counter + 1
                right = right - 1
            elif (s[right] == " " or s[right]==s[0]) and counter !=0:
                break
        
        return counter