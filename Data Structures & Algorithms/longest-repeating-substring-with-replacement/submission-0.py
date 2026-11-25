from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        cnt = Counter()
        l = 0
        for r in range(len(s)):
            cnt[s[r]] += 1
            while r - l + 1 - cnt.most_common(1)[0][1] > k:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans