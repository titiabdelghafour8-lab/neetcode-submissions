class Solution:
    def hammingWeight(self, n: int) -> int:
        length = n.bit_length()
        ones_count = 0
        for i in range(length):
            ones_count += (n & (1 << i)) >> i
        return ones_count
        