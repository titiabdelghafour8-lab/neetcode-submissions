class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        nums_set = set(nums)
        max_seq_length = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                current_seq_length = 1
                while num + 1 in nums_set:
                    current_seq_length += 1 
                    num += 1
                max_seq_length = max(current_seq_length, max_seq_length)
        return max_seq_length


