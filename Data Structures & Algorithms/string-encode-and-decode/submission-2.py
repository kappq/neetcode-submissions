class Solution:
    def encode(self, strs: List[str]) -> str:
        lens = list(map(str, map(len, strs)))
        return str(len(lens)) + "," + ",".join(lens) + "," + "".join(strs)
    
    def parseString(self, s: str, cur: int) -> Tuple[str, int]:
        ss = ""
        while cur < len(s) and s[cur] != ",":
            ss += s[cur]
            cur += 1
        cur += 1
        return (ss, cur)

    def decode(self, s: str) -> List[str]:
        cur = 0
        n, cur = self.parseString(s, cur)
        n = int(n)
        lens = []
        for _ in range(n):
            len_, cur = self.parseString(s, cur)
            lens.append(int(len_))
        ans = []
        for i in range(n):
            ans.append(s[cur:cur + lens[i]])
            cur += lens[i]
        return ans
