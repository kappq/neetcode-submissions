import string
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = None
        ds, dt = defaultdict(int), defaultdict(int)
        for c in t:
            dt[c] += 1
        l = 0
        for r in range(len(s)):
            ds[s[r]] += 1
            if self.includes(ds, dt):
                while ds[s[l]] - 1 >= dt[s[l]]:
                    ds[s[l]] -= 1
                    l += 1
                if ans is None or r - l + 1 < len(ans):
                    ans = s[l:r + 1]
        return ans if ans is not None else ""

    def includes(self, ds: Dict[str, int], dt: Dict[str, int]) -> bool:
        for c in string.ascii_letters:
            if ds[c] < dt[c]:
                return False
        return True
