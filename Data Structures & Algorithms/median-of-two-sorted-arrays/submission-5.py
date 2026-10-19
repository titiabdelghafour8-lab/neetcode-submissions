class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        concat = [0 for i in range(n1 + n2)]
        k = 0
        i = 0
        j = 0
        while i < n1 and j < n2:
            if nums1[i] > nums2[j]:
                concat[k] = nums2[j] 
                j += 1
            else:
                concat[k] = nums1[i]
                i += 1
            k += 1
        while i < n1:
            concat[k] = nums1[i]
            i += 1
            k += 1
        while j < n2:
            concat[k] = nums2[j]
            j += 1
            k += 1
        
        if (n1 + n2) % 2 == 1:
            return concat[(n1 + n2) // 2]
        else:
            return (concat[(n1 + n2) // 2] + concat[(n1 + n2) // 2 - 1]) / 2