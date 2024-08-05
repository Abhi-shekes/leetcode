class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(n):
            res.append(nums[i])
            x = nums[i]
            for j in range(i + 1, n):
                x += nums[j]
                res.append(x)
        res.sort()
        return sum(res[left - 1:right]) % (10 ** 9 + 7)