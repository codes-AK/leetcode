from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Precalculate suffix minimums
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
            
        # Step 2: Iterate forward to find the first stable index
        prefix_max = float('-inf')
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            instability_score = prefix_max - suffix_min[i]
            
            if instability_score <= k:
                return i
                
        return -1
