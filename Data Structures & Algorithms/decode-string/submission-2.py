class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        res = ''
        for c in s:
            temp = ''
            if c == ']':
                while stk[-1] != '[':
                    temp = stk.pop() + temp
                stk.pop()
                num = ''
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(temp * int(num))
            else:
                stk.append(c)


        return res.join(stk)