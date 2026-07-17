class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)
        counts = Counter(nums)

        cnt_g = [0] * (max_num + 1)

        for i in range (max_num, 0, -1):
            total_multiples = 0
            for j in range(i, max_num + 1, i):
                total_multiples += counts[j]

            pairs = total_multiples * (total_multiples - 1) // 2

            for j in range(2 * i, max_num + 1, i):
                pairs -= cnt_g[j]

            cnt_g[i] = pairs

        prefix_sums = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            prefix_sums[i] = prefix_sums[i - 1] + cnt_g[i]

        ans = []
        for q in queries:
            idx = bisect_right(prefix_sums, q)
            ans.append(idx)

        return ans

        
