class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for a in range(1, len(nums)):
            b = a
            while b > 0 and (nums[b-1] > nums[b]):
                nums[b-1], nums[b] = nums[b], nums[b-1]
                b -= 1
        