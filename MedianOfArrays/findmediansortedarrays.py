import math

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        if (m + n) < 1:
            print("Both lists cannot be empty.")
            return

        if m + n == 1:  # only 1 element combined
            if n == 0:
                return nums1[0] / 1
            else:
                return nums2[0] / 1

        if m >= n:  # Check which list is bigger to add to
            nums1.extend(nums2) 
            nums1.sort()
            m = len(nums1)
            if m % 2 != 0:     # Odd
                 ans = m / 2
                 ans = math.ceil(ans) - 1
                 return nums1[ans] / 1
            else:   # Even
                ans = m // 2
                return (nums1[ans-1] + nums1[ans]) / 2

        else:
            nums2.extend(nums1)
            nums2.sort()
            n = len(nums2)
            if n % 2 != 0:     # Odd
                 ans = n / 2
                 ans = math.ceil(ans) - 1
                 return nums2[ans] / 1
            else:
                ans = n // 2
                return (nums2[ans-1] + nums2[ans]) / 2
           
class Test:
    nums1, nums2 = [1,3], [2]
    nums3, nums4 = [1,2], [3,4]
    nums5, nums6 = [3,9,12], [8,11,17]
    nums7, nums8 = [], [6]
    nums9, nums0 = [], [3,5,8,9,12]
    
    strs = Solution()

    print("Case 1:", strs.findMedianSortedArrays(nums1, nums2))
    print("Case 2:", strs.findMedianSortedArrays(nums3, nums4))
    print("Case 3:", strs.findMedianSortedArrays(nums5, nums6))
    print("Case 4:", strs.findMedianSortedArrays(nums7, nums8))
    print("Case 5:", strs.findMedianSortedArrays(nums9, nums0))
