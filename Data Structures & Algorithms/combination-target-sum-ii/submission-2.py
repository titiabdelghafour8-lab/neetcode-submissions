class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def combine(i, sum_yet):

            if sum_yet == target:
                res.append(path[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                if sum_yet + candidates[j] > target:
                    return
                
                path.append(candidates[j])
                combine(j + 1, sum_yet + candidates[j])
                path.pop()

        combine(0, 0)
        return res

            