class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = prices[0]
        for cur in prices[1:]:
            ans = max(ans, cur - mn)
            mn = min(mn, cur)
        return ans