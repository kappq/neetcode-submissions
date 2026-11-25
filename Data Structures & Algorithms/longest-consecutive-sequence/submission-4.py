import sys

sys.setrecursionlimit(100000)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        dp = {}
        def solve(num):
            if num not in s:
                return 0
            if num not in dp:
                dp[num] = solve(num + 1) + 1
            return dp[num]
        for num in nums:
            solve(num)
        return max(dp.values(), default=0)