class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        k = len(tasks)
        reps = {}
        current_max = 0
        current_max_char = None
        first_appeared = {}
        for i in range(k) :
            if tasks[i] in reps:
                reps[tasks[i]] += 1
            else:
                reps[tasks[i]] = 1
                first_appeared[tasks[i]] = i
            
            # Update max frequency and character tracker for every item
            if reps[tasks[i]] >= current_max:
                current_max = reps[tasks[i]]
                current_max_char = tasks[i]

        # Fix: Count how many characters share this same max frequency
        max_count = sum(1 for char, count in reps.items() if count == current_max)

        # Fix: Use the correct block-scheduling math (n + 1 slots per chunk) plus the max_count tie-breaker
        cycles = max((current_max - 1) * (n + 1) + max_count, k)
        
        print("max = ", cycles, current_max)
        return cycles
        
        return cycles

