class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1),len(nums2)
        
        A = nums1 if n < m else nums2
        B = nums1 if n >= m else nums2
        half = (n+m)//2
        l,r = 0,len(A)-1
        while True:
            mid = (l+r)//2
            otherMid = (half) - mid - 2
            Aleft = A[mid] if mid >= 0 else float("-infinity")
            Aright = A[mid+1] if mid+1 < len(A) else float("infinity")
            Bleft = B[otherMid] if otherMid >= 0 else float("-infinity")
            Bright = B[otherMid+1] if otherMid+1 < len(B) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright:
                if (n+m)%2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = mid-1
            else:
                l = mid+1