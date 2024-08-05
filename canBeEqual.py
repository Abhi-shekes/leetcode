class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for ele in arr:
            if ele not in target:
                return False
            else:
                target.remove(ele)
        
        return True