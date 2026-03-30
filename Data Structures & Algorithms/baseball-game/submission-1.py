class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for c in operations:
            if c in ('+','D','C'):
                if c == '+':
                    stk.append(stk[-1] + stk[-2])
                if c == 'C':
                    stk.pop()
                if c == 'D':
                    stk.append(stk[-1]*2)

            else:
                stk.append(int(c))

        return sum(stk)      