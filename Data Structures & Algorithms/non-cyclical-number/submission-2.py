class Solution:
    def digits_square(self, n):
        digits = []
        while n > 0:
            digits.append((n % 10) ** 2)
            n = n // 10
        return digits


    def isHappy(self, n: int) -> bool:
        square_already = set()
        while True:
            n = sum(self.digits_square(n))
            if n == 1:
                return True
            elif n in square_already:
                return False
            square_already.add(n)

