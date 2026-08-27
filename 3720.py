from collections import Counter

class Solution:
    def lexicographicallySmallestPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        
        matched_length = 0
        for ch in target:
            if count[ch] > 0:
                count[ch] -= 1
                matched_length += 1
            else:
                break
                
        for i in range(matched_length, -1, -1):
            if i < n:
                t_char = target[i]
                for c_code in range(ord(t_char) + 1, ord('z') + 1):
                    c = chr(c_code)
                    if count[c] > 0:
                        res = [target[:i], c]
                        count[c] -= 1
                        for char_code in range(ord('a'), ord('z') + 1):
                            ch_key = chr(char_code)
                            if count[ch_key] > 0:
                                res.append(ch_key * count[ch_key])
                        return "".join(res)
            
            if i > 0:
                count[target[i - 1]] += 1
                
        return ""
