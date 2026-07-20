class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n

        flat = []
        for row in grid:
            flat.extend(row)


        k = k % total_elements

        shifted_flat = flat[-k:] + flat[:-k]

        result = []
        for i in range(0, total_elements, n):
            result.append(shifted_flat[i : i + n])

        return result
        
