class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = list(range(len(nums)))
        idxs.sort(key=lambda idx: nums[idx])
        l, r = 0, len(nums) - 1
        while l < r:
            i, j = idxs[l], idxs[r]
            if nums[i] + nums[j] == target:
                return [i, j] if i < j else [j, i]
            if nums[i] + nums[j] < target:
                l += 1
            else:
                r -= 1
