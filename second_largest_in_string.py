class Solution(object):
    def secondHighest(self, s):
     

        nums = []
        int_nums = []

        for i in s:
            if i.isnumeric():
                nums.append(i)
        second_largest = -1
        if nums:
            for item in nums:
                if int(item) not in int_nums:
                    int_nums.append(int(item))
            
            int_nums = sorted(int_nums)
            
            if len(int_nums) >=2:
                second_largest= int_nums[-2]
        
        return second_largest