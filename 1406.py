class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            max_score = float('-inf')
            take_sum = 0
            for X in range(1, 4):
                if i + X - 1 < n:
                    take_sum += stoneValue[i + X - 1]
                    max_score = max(max_score, take_sum - dp[i + X])
            dp[i] = max_score
            
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
