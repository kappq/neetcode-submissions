import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        for c in string.ascii_uppercase:
            cnt = 0
            l = 0
            for r in range(len(s)):
                if s[r] != c:
                    cnt += 1
                while cnt > k:
                    if s[l] != c:
                        cnt -= 1
                    l += 1
                ans = max(ans, r - l + 1)
        return ans