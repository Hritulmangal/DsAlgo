class Solution: #By CyFun
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
