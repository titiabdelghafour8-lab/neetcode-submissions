class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        n = len(digits)
        res = []
        string = []
        def backtrack(i):
            if i == n:
                res.append("".join(string[:]))
                return 
            for el in phone_map[int(digits[i])]:
                string.append(el)
                backtrack(i + 1)
                string.pop()
        backtrack(0)
        return res