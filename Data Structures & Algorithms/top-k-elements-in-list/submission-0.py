from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return list(map(lambda x: x[0], cnt.most_common(k)))
        