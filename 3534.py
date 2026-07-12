class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        p = sorted(range(n), key=lambda x: nums[x])

        LOG = 18
        fa = [[0]* LOG for _ in range(n)]

        j = 0
        for i in range(n):
            while nums[p[i]] - nums[p[j]] > maxDiff:
                j += 1
                fa[i][0] = j
                for  k in range(1, LOG):
                    fa[i][k] = fa[fa[i][k - 1]][k - 1]

        mp = [0] * n
        for i, original_idx in enumerate(p):
            mp[original_idx] = i

        ans = []
        for u, v in queries:
            a, b = mp[u], mp[v]
            if a == b:
                ans.append(0)
                continue

            if a < b:
                a, b = b, a 

            steps = 0

            for k in range(LOG - 1, -1, -1):
                if fa[a][k]  != -1 and fa[a][k] > b:
                    a = fa[a][k]
                    steps |= (1 << k)


            if fa[a][0] == -1 or fa[a][0] > b:
                ans.append(-1)
            else:
                ans.append(steps + 1)
        return ans
