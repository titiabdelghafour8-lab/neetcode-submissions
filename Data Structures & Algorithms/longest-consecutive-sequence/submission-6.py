class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        nums_set = { x: False for x in nums }
        sequence_lengths = [0] * n
        sequence_index = 0
        for num in nums_set:
            sequence_lengths[sequence_index] = 1
            if nums_set[num]:
                continue
            nums_set[num] = True
            while num + 1 in nums_set:
                num = num + 1
                nums_set[num] = True
                sequence_lengths[sequence_index] += 1
            sequence_index += 1 
        return max(sequence_lengths) 
