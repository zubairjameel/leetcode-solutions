class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        multi = (nums[-1]-1)*(nums[-2]-1)
        return multi
        