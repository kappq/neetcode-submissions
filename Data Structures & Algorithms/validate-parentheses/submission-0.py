class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"(": ")", "[": "]", "{": "}"}
        st = []
        for c in s:
            print(c, st)
            if c in parens.keys():
                st.append(c)
            else:
                if len(st) == 0 or parens[st[-1]] != c:
                    return False
                st.pop()
        return len(st) == 0
