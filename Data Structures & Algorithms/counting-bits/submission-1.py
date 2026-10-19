class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0 for i in range(n + 1)]
        for i in range(n + 1):
            i_length = i.bit_length()
            for j in range(i_length):
                counts[i] += (i & (1 << j)) >> j 
            
        return counts

        