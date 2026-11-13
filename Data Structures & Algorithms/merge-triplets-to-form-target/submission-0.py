class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #eligibility is a triplet of booleans that represent eligiblity for each target parts to be chosen from that triplet
        #we hit the target if and only if eligibility we can have eligibility (True, True, True) after going throught the whole list of candidates with at least one True eligibility
        def eligible(triplet):
            eligibility = [False, False, False]
            if triplet[0] == target[0]:
                if triplet[1] <= target[1] and triplet[2] <= target[2]:
                    eligibility[0] = True
            if triplet[1] == target[1]:
                if triplet[0] <= target[0] and triplet[2] <= target[2]:
                    eligibility[1] = True
            if triplet[2] == target[2]:
                if triplet[1] <= target[1] and triplet[0] <= target[0]:
                    eligibility[2] = True
            return eligibility


        def and_triplets_op(triplet1, triplet2):
            triplet1[0] = triplet1[0] or triplet2[0]
            triplet1[1] = triplet1[1] or triplet2[1]
            triplet1[2] = triplet1[2] or triplet2[2]


        n = len(triplets)
        eligibility = [False, False, False]
        for i in range(n):
            and_triplets_op(eligibility, eligible(triplets[i]))
        
        return (eligibility[0] and eligibility[1] and eligibility[2])
               
            