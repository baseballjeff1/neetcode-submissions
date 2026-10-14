class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_car = {}
        t_car = {}

        for i in s:
            if i in s_car:
                s_car[i] += 1
            else:
                s_car[i] = 1

        for j in t:
            if j in t_car:
                t_car[j] += 1
            else:
                t_car[j] = 1

        if s_car == t_car:
            return True
        else:
            return False