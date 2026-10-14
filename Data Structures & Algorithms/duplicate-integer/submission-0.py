class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for i in nums:
            result.add(i)

        if len(result) != len(nums):
            return True
        else:
            return False
            