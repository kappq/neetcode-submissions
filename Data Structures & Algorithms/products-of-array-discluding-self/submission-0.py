class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros = nums.count(0)
        if zeros >= 2:
            return [0] * n
        prod = 1
        for num in nums:
            if num == 0:
                continue
            prod *= num
        ans = []
        for num in nums:
            if zeros == 1:
                ans.append(prod if num == 0 else 0)
            else:
                ans.append(prod // num)
        return ans