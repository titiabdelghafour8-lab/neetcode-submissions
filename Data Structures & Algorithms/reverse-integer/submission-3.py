class Solution:
    def reverse(self, x: int) -> int:
        rev_x = str(x)
        sign = ""
        if rev_x[0] == "-":
            sign = "-"
            rev_x = rev_x[1::]
        reversed_int = int(rev_x[::-1]) if sign == "" else -int(rev_x[::-1])
        if reversed_int > 2 ** 31 - 1 or reversed_int < -2 ** 31:
            return 0
        return reversed_int