class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not str:
            return ""

        prefix = []
        for characters in zip(*strs):
            if len(set(characters)) == 1:
                prefix.append(characters[0])
            else:
                break

        return "".join(prefix)
        
