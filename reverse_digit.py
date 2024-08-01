class Solution:
    def reverse(self, x: int) -> int:
        def is_within_int32_range(value):
            return -2**31 <= value <= 2**31 - 1

        
    
        reverse = ""

        if x<0:
            for i in str(x):
                if i != str(x)[0]:
                    reverse = i + reverse 
            reverse = "-"+reverse
        else:
            for i in str(x):
                reverse = i + reverse 

        if not is_within_int32_range(int(reverse)):
            return 0

        return int(reverse)
