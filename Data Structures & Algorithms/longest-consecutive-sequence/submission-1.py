class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = list(set(nums))
        nums.sort()
        ans = 0
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 1
        ans = max(ans, cur)
        return ans
