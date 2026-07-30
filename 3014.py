class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)

        if n <= 8:
            return n * 1
        elif n <= 16:
            return 8 * 1 + (n - 8) * 2
        elif n <= 24:
            return 8 * 1 + 8 * 2 + (n - 16) * 3
        else:
            return 8 * 1 + 8 * 2 + 8 * 3 + (n - 24) * 4
