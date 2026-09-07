class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        last = [0] * 26
        total = 0
        
        for c in s:
            idx = ord(c) - ord('a')
            new_added = (total + 1 - last[idx]) % MOD
            total = (total + new_added) % MOD
            last[idx] = (last[idx] + new_added) % MOD
            
        return total
