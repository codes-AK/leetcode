class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        # Pair values with original indices and sort by value
        sorted_pairs = sorted((nums[i], i) for i in range(n))
        
        result = [0] * n
        i = 0
        
        while i < n:
            j = i
            # Group elements where difference between adjacent values <= limit
            while j + 1 < n and sorted_pairs[j + 1][0] - sorted_pairs[j][0] <= limit:
                j += 1
            
            # Extract original indices and values for the current component
            indices = [sorted_pairs[k][1] for k in range(i, j + 1)]
            values = [sorted_pairs[k][0] for k in range(i, j + 1)]
            
            # Sort indices to place values in leftmost original positions
            indices.sort()
            
            # Place values back into the result array
            for idx, val in zip(indices, values):
                result[idx] = val
                
            i = j + 1
            
        return result
