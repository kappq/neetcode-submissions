class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        l, r = 0, n - 1
        pref, suff = 0, 0
        while l <= r:
            if pref < suff:
                ans += max(min(pref, suff) - height[l], 0)
                pref = max(pref, height[l])
                l += 1
            else:
                ans += max(min(pref, suff) - height[r], 0)
                suff = max(suff, height[r])
                r -= 1
        return ans