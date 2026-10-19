class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)
        for i in range(n - 1, -1, -1):
            temp = digits[i] + carry
            if i == n - 1:
                temp += 1 
            digits[i] = temp % 10
            carry = (temp - digits[i]) // 10
        if carry > 0:
            digits.insert(0, carry)
        return digits