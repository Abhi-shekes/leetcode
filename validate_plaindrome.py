class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s:
            s = s.lower()
            left = 0
            right = len(s) - 1
            while right >= left:
                if not (97 <= ord(s[left]) <= 122) and not (48 <= ord(s[left]) <= 57):
                    left += 1
                elif not (97 <= ord(s[right]) <= 122) and not (48 <= ord(s[right]) <= 57):
                    right -= 1
                else:
                    if s[right] != s[left]:
                        return False
                    right -= 1
                    left += 1
        return True


