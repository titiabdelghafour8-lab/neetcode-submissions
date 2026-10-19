class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        if n < 0:
            return self.myPow(1 / x, -n)
        pow_half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return pow_half * pow_half
        if n % 2 == 1:
            return pow_half * pow_half * x