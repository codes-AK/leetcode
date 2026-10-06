class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0   # unmatched '(' so far
        add = 0           # '(' we must insert for unmatched ')'

        for ch in s:
            if ch == '(':
                open_needed += 1
            else:  # ch == ')'
                if open_needed > 0:
                    open_needed -= 1
                else:
                    add += 1

        return add + open_needed
