class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        if m > n:
            return []

        ex = [0] * (n + 1)
        ex[n] = m
        j = m
        for i in range(n - 1, -1, -1):
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
            ex[i] = j

        used = [0] * (n + 1)
        used[n] = m
        for i in range(n - 1, -1, -1):
            u_next = used[i + 1]
            if u_next > 0 and word1[i] == word2[u_next - 1]:
                cand1 = u_next - 1
            else:
                cand1 = u_next

            e_next = ex[i + 1]
            cand2 = e_next - 1 if e_next > 0 else e_next

            used[i] = min(cand1, cand2)

        e1 = [min(ex[i], used[i]) for i in range(n + 1)]

        result = []
        budget = 1
        i = 0

        for k in range(m):
            found = -1
            while i < n:
                if budget == 1:
                    if word1[i] == word2[k] and e1[i + 1] <= k + 1:
                        found = i
                        break
                    if word1[i] != word2[k] and ex[i + 1] <= k + 1:
                        found = i
                        budget = 0
                        break
                else:
                    if word1[i] == word2[k] and ex[i + 1] <= k + 1:
                        found = i
                        break
                i += 1

            if found == -1:
                return []

            result.append(found)
            i = found + 1

        return result
