class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = [0] * n
        high_temp = temperatures[n-1]
        high_temp_index = n-1
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if stk[j] == 0:
                    j = n
                    break
                j += stk[j]

            if j < n:
                stk[i] = j - i
        return stk   
        