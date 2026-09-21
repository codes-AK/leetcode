class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        cnt = [0] * k  # cnt[r] = subarrays ending at previous index with product % k == r

        for a in nums:
            m = a % k
            new = [0] * k
            new[m] += 1  # subarray starting and ending at this element
            for r in range(k):
                if cnt[r]:
                    new[(r * m) % k] += cnt[r]  # extend earlier subarrays
            for r in range(k):
                res[r] += new[r]
            cnt = new

        return res
