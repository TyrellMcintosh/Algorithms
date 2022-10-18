class Solution(object):
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        if isinstance(target, int) == False:
            print("Target value not a valid input")
            return
        if len(nums) < 2:
            print("Not enough elements in list")
            return
        for x in nums:
            if isinstance(x,int) == False:
                print("List contains invalid input")
                return

        new = target - nums[0]
        
        rlist = []
        start = 0
        stop = len(nums)-1

        while rlist != None:
            for i in range(start,stop):
                if nums[i+1] == new:
                    rlist.append(nums.index(nums[start]))
                    rlist.append(nums.index(nums[i+1],start+1)) #index finds first satisfy
                    return rlist

            start += 1
            new = target - nums[start]

            if start == stop:
                break

class Program:
    num1 = [2, 7, 11, 15]
    num2 = [3, 2, 4]
    num3 = [3, 3]
    num4 = [7, 3, 8, 2, 1, 4]
    num5 = [7, 9, 9]
    num6 = [-3, -5, 3]
    num7 = []
    num8 = ['hello', 1, 3, 5]

    target1 = 9
    target2 = 6
    target3 = 6
    target4 = 12
    target5 = 18
    target6 = 0
    target7 = 2
    target8 = 14
    
    numbers = Solution()

    ans1 = numbers.twoSum(num1, target1)
    ans2 = numbers.twoSum(num2, target2)
    ans3 = numbers.twoSum(num3, target3)
    ans4 = numbers.twoSum(num4, target4)
    ans5 = numbers.twoSum(num5, target5)
    ans6 = numbers.twoSum(num6, target6)
    ans7 = numbers.twoSum(num7, target7)
    ans8 = numbers.twoSum(num8, target8)

    print(f"Case 1: {ans1}\nCase 2: {ans2}\nCase 3: {ans3}\nCase 4: {ans4}\nCase 5: {ans5}")
    print(f"Case 6: {ans6}\nCase 7: {ans7}\nCase 8: {ans8}")
