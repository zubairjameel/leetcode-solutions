class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = set(nums)
        if len(arr) == len(nums):
            return False
        return True
        