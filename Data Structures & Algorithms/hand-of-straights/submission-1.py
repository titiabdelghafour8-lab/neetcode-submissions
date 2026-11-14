class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        freqs = defaultdict(int)
        for i in range(n):
            freqs[hand[i]] += 1
        hand.sort()
        i = 0
        while i < n:
            if freqs[hand[i]] <= 0:
                i += 1
                continue
            idx = 0
            while idx < groupSize:
                if freqs[hand[i] + idx] <= 0:
                    return False
                freqs[hand[i] + idx] -= 1
                idx += 1
        return True