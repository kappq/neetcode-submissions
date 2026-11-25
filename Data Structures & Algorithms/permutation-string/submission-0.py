from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        d1, d2 = defaultdict(int), defaultdict(int)
        for c in s1:
            d1[c] += 1
        for c in s2[:k]:
            d2[c] += 1
        if d1 == d2:
            return True
        for i in range(k, len(s2)):
            d2[s2[i - k]] -= 1
            if d2[s2[i - k]] == 0:
                del d2[s2[i - k]]
            d2[s2[i]] += 1
            if d1 == d2:
                return True
        return False
