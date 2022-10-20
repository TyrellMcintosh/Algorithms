class Solution(object):
    def permute(self, nums):
        size = len(nums)


        if size == 0 or size > 6:     # Constraint: 1 <= len(nums) <= 6
            return

        if len(set(nums)) != size:     # Constraint: All items must be unique
            return
        
        for x in nums:
            if isinstance(x,int) == False:
                return
            if x < -10 or x > 10:   # -10 <= nums[i] <= 10
                return

        rlist = []
        x = 0

        if size == 1:
            return [nums]

        elif size == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]

        else:
            for x in range(len(nums)):
                temp = nums.pop(x)
                n = self.permute(nums)
                rlist.extend(n)
                nums.insert(x, temp)
                
                for count in range(len(n)):
                    rlist[len(rlist)-1-count].insert(0,temp)
                
            return rlist

class Test:
    nums1 = [1, 2, 3]
    nums2 = [0, 1]
    nums3 = [1]

    test = Solution()

    print("Example 1: ", test.permute(nums1))
    print("Example 2: ", test.permute(nums2))
    print("Example 3: ", test.permute(nums3))
  
