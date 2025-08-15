class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[mid + 1]:  # still climbing
                left = mid + 1
            else:  # we are in the descending part
                right = mid
        
        return left  # or right, both are same here
