class Solution:
    def distinctAverages(self, nums):
        nums = sorted(nums)
        distinct = []
        left = 0
        right = len(nums)-1
        
        while(left<right):
            
            average = (nums[left] + nums[right]) /2
            if average not in distinct:
                distinct.append(average)
                
            left +=1
            right -=1
        return len(distinct)

        
