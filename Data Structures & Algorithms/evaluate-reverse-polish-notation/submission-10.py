import operator

def div(a, b):
    return int(a / b)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": div}
        st = []
        for token in tokens:
            if token in ops.keys():
                rand2, rand1 = st.pop(), st.pop()
                st.append(ops[token](rand1, rand2))
            else:
                st.append(int(token))
        return st.pop()
