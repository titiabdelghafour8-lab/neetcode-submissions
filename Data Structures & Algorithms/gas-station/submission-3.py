class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        max_remainder = 0
        starts = []
        for i in range(n):
            remainder = (gas[i] - cost[i])
            remainder = remainder + gas[(i + 1) % n] if remainder >= 0 else remainder
            if remainder > max_remainder:
                max_remainder = remainder
                starts.append(i)
        flag = True
        res = -1
        for start in starts:
            remainder = gas[start]
            idx = start
            for i in range(n):
                if (remainder - cost[idx]) < 0:
                    break
                remainder = (remainder - cost[idx]) + gas[(idx + 1) % n]
                idx = (idx + 1) % n
                if idx == start:
                    res = start
                    break
            if res >= 0:
                break
        return res
            