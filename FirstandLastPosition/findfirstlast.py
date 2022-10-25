class Solution(object):
    def searchRange(self, nums, target):

        n = len(nums)

        if n == 0 or target not in nums:
            return [-1,-1]
        
        if n == 1:
            return [0,0]

        first = nums.index(target)
        
        for i in range(first, n):
            if nums[i] != target:
                last = i - 1
                return [first, last]
    
        return [first, i]

class Test:
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    nums2 = [1,1]
    target2 = 1
    nums3 = [6]
    target3 = 6

    test = Solution()

    print("Example 1: ", test.searchRange(nums1,target1))
    print("Example 2: ", test.searchRange(nums2,target2))
    print("Example 3: ", test.searchRange(nums3,target3))
