class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        l = 0
        cnt = 0

        for r in range(n):
            if s[r] == "1":
                cnt += 1

            while cnt == k:
                sub = s[l : r + 1]
                if (
                    not ans
                    or len(sub) < len(ans)
                    or (len(sub) == len(ans) and sub < ans)
                ):
                    ans = sub

                if s[l] == "1":
                    cnt -= 1
                l += 1

        return ans
