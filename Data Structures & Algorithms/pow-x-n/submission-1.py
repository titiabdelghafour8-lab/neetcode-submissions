class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        if n < 0:
            return pow(1 / x, -n)
        elif n % 2 == 0:
            return pow(x, n // 2) * pow(x, n // 2)
        elif n % 2 == 1:
            return pow(x, n - 1) * x