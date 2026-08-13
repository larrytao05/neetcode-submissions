class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1,nums2 = nums2,nums1
        l = 0
        r = len(nums1)-1
        total = len(nums1) + len(nums2)
        half = total // 2
        while True:
            m1 = l+(r-l)//2
            m2 = (half - m1 - 2)
            Aleft = nums1[m1] if m1 >= 0 else float('-inf')
            Aright = nums1[m1+1] if m1+1 < len(nums1) else float('inf')
            Bleft= nums2[m2] if m2 >= 0 else float('-inf')
            Bright = nums2[m2+1] if m2+1 < len(nums2) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (min(Aright,Bright) + max(Bleft,Aleft)) / 2.0
            elif Aleft > Bright:
                r = m1 - 1
            else:
                l = m1 + 1