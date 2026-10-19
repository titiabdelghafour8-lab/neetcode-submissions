class Solution:
    def twos_complement_to_int(self, bits: list[int]) -> int:
        """Converts a 12-bit two's complement list of 0s and 1s into a signed integer."""
        # Convert the list of bits into an integer value
        val = int("".join(str(b) for b in bits), 2)

        # If the most significant bit (MSB) is 1, it's a negative number in two's complement
        if bits[0] == 1:
            val -= (1 << len(bits))  # Subtract 2^12 (4096)
        
        return val
    def get_digits_sum(self, x):
       
        digs_list = [0 for i in range(13)]
        
        for i in range(13):
            digs_list[12 - i] = x % 2
            x >>= 1

        
        return digs_list



    def getSum(self, a: int, b: int) -> int:
        if a > b:
            a, b = b, a
        a_list = self.get_digits_sum(a)
        b_list = self.get_digits_sum(b)
        sum = [0 for i in range(13)]
        carry = 0
        for i in range(12, -1, -1):
            sum[i] = a_list[i] ^ b_list[i] ^ carry
            carry = (a_list[i] | b_list[i]) & (a_list[i] | carry) & (carry | b_list[i])
        
        sum[0] = 0
        sum_int = self.twos_complement_to_int(sum[1:13])
        return sum_int


            
        