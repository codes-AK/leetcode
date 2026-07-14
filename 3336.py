class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)

        @lru_cache(None)
        def dp(i: int, x: int, y: int) -> int:
            if i == n:
                return 1 if(x > 0 and x == y) else 0

            skip = dp(i + 1, x, y)

            take1 = dp(i + 1, math.gcd(x, nums[i]), y)

            take2 = dp(i + 1, x, math.gcd(y, nums[i]))

            return (skip + take1 + take2) % MOD

        return dp(0, 0, 0)
        
