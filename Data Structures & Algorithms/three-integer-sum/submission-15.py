class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for k in range(n):
            if k < n - 1 and nums[k] == nums[k + 1]:
                continue
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] == -nums[k]:
                    ans.append([nums[i], nums[j], nums[k]])
                    i += 1
                    while i < k and nums[i] == nums[i - 1]:
                        i += 1
                    j -= 1
                    while j >= 0 and nums[j] == nums[j + 1]:
                        j -= 1
                    continue
                if nums[i] + nums[j] < -nums[k]:
                    i += 1
                else:
                    j -= 1
        return ans