class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A): # a is smaller array
            A, B = B, A
        
        total = len(B) + len(A)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2 # A
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2 == 1:
                    return min(Aright, Bright)
                
                
                return (max(Aleft,Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        
