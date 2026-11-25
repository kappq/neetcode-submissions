class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for k in range(n):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] == -nums[k]:
                    trip = [nums[i], nums[j], nums[k]]
                    if trip not in ans:
                        ans.append(trip)
                if nums[i] + nums[j] < -nums[k]:
                    i += 1
                else:
                    j -= 1
        return ans