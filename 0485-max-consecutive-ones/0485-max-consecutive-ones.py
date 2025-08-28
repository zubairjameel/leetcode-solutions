class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                maxi = max(maxi, count)
            else:
                count = 0
        return maxi
