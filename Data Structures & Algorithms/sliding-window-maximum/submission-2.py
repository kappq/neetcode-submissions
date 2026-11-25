from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        dq = deque()
        for num in nums[:k]:
            while len(dq) != 0 and dq[-1] < num:
                dq.pop()
            dq.append(num)
        ans.append(dq[0])
        for i in range(k, n):
            if dq[0] == nums[i - k]:
                dq.popleft()
            while len(dq) != 0 and dq[-1] < nums[i]:
                dq.pop()
            dq.append(nums[i])
            ans.append(dq[0])
        return ans
