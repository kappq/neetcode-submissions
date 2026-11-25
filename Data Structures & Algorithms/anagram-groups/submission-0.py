class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        eq: Dict[str, List[str]] = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in eq:
                eq[key] = []
            eq[key].append(s)
        return list(eq.values())