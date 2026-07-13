class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        result = []

        for length in range(2, 10):
            for start in range(10 - length):
                substring = sample[start:start + length]
                num = int(substring)

                if low <= num <= high:
                    result.append(num)


                elif num > high:
                    break

        return sorted(result)
