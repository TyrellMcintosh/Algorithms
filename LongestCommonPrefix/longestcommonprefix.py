class Solution(object):
    def __init__(self):
        pass
    
    def longestCommonPrefix(self, strs):
        if len(strs) < 1 or len(strs) > 200:    # Constraint: 1 <= len(strs) <= 200
            print("There are either too few or too many strings in the list.")
            return

        for x in strs:
            if len(x) > 200:    # Constraint: 0 <= len(x) <= 200
                print("One of the strings in the list exceed the maximum.")
                return

            if x.isalpha() == False and x != "":    # Constraint: English letters only
                print("Strings can only contain English letters")
                return

            x = x.lower()   # Constraint: Should only be lowercase letters

        if len(strs) == 1:
            return strs[0]

        minimum = min(strs, key=len)
        strs.remove(minimum)
        strs.append(minimum)

        x = 0   # List of strings counter

        for count in range(x,len(strs)-1):
            count = 0
            while (count < len(minimum) and strs[x][count] == minimum[count]):
                count += 1
            
            if count == 0:
                return ""
            
            minimum = minimum[0:count]

            x += 1

        return minimum

class Test:
    strs1 = ["flight","flower", "flow"]
    strs2 = ["dog", "racecar", "car"]
    strs3 = ["drag", "dry", "draw"]
    strs4 = ["hello", "water", "wet"]
    strs5 = ["apple", "app", "donkey"]
    strs6 = ["hi", "horse", "hose"]

    strs = Solution()

    print("Case 1:", strs.longestCommonPrefix(strs1))

    print("Case 2:", strs.longestCommonPrefix(strs2))

    print("Case 3:", strs.longestCommonPrefix(strs3))

    print("Case 4:", strs.longestCommonPrefix(strs4))

    print("Case 5:", strs.longestCommonPrefix(strs5))

    print("Case 6:", strs.longestCommonPrefix(strs6))
