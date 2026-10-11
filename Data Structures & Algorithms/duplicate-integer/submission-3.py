class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = set()
     
        for i in range (len(nums)):
            if nums[i] in appeared:
                return True
            appeared.add(nums[i])
        return False
        