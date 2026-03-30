class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        '''
        '+': Record a new score that is the sum of the previous two scores.
        'D': Record a new score that is the double of the previous score.
        'C': Invalidate the previous score, removing it from the record. 
        '''

        for i in range(len(operations)):
            temp = 0
            if operations[i] == '+':
                temp = stack[-1] + stack[-2]
                stack.append(temp)
            elif operations[i] == 'D':
                temp = stack[-1] * 2
                stack.append(temp)
            elif operations[i] == 'C':
                stack.pop()
            else:
                stack.append(int(operations[i]))
        
        res = sum(stack)
        return res