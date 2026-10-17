class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        l = 0
        sub = set() # holder for characters for substring
        result = 1 # current longest substring in loop

        sub.add(s[l]) #adding first character
        for r in range(1, len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1

            sub.add(s[r])
            result = max(result, len(sub))

        return result
