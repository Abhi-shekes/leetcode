class Solution(object):
    def romanToInt(self, s):

        roman_to_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        sums = 0
        last_value = 0
        for alpha in s[::-1]:
            if roman_to_value[alpha] >= last_value:
                sums = sums + roman_to_value[alpha]
            else:
                sums = sums - roman_to_value[alpha]
                
            last_value =  roman_to_value[alpha]

        return sums