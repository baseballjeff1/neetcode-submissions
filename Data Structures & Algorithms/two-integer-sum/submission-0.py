class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        log = {}

        i = 0
        while i < len(nums):
            difference = target - nums[i]
            if difference in log:
                return sorted([i, log[difference]])

            log[nums[i]] = i
            i += 1