class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0
        start = 0
        char_index_map = {}

        for end in range(n):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1
            
            char_index_map[s[end]] = end
            max_len = max(max_len, end - start + 1)
        
        return max_len
