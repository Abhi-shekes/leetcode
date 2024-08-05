class Solution:
    def kthDistinct(self, arr, k):
        distinct = []
        for index, i in enumerate(arr):
            if i not in arr[0:index] and i not in arr[index+1:]:
                distinct.append(i)
                
        if len(distinct) < k:
            return ""
        return distinct[k-1]