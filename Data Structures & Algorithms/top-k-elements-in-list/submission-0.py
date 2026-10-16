class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range(len(nums) + 1)]

        count = {}
        for i in range(0, len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1

        for j in count:
            amt = count[j]
            frequency[amt].append(j)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                res.append(j)
                if len(res) == k:
                    return res

