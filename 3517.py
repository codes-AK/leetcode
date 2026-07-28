class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter

        counts = Counter(s)
        half = []
        mid = ""

        for char in sorted(counts.keys()):
            half.append(char * (counts[char] // 2))
            if counts[char] % 2 == 1:
                mid = char

        first_half = "".join(half)
        return first_half + mid + first_half[::-1]
        
