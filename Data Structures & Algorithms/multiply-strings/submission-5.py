class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums_map = { "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0 }
        str_map = { 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0" }
        def conver_int(s):
            num = 0
            n = len(s)
            for i in range(n):
                num += nums_map[s[n - i - 1]] * 10 ** i
            return num
    
        def conver_str(num):
            if num == 0:
                return str_map[num]
            s = []
            while num > 0:
                s.append(str_map[num % 10])
                num = num // 10
            return "".join(s[::-1])
        
        prod = conver_int(num1) * conver_int(num2)
        return conver_str(prod)

        