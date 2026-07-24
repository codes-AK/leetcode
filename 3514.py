class Solution:
    def countUniqueXORTriplets(self, nums: list[int]) -> int:
        S = list(set(nums))
        
        P = set()
        for i in range(len(S)):
            for j in range(i, len(S)):
                P.add(S[i] ^ S[j])
                
        U = set()
        for p in P:
            for x in S:
                U.add(p ^ x)
                
        return len(U)
