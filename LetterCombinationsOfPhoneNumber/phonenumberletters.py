class Solution(object):
    def letterCombinations(self, digits):

        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        length = len(digits)

        if length > 4:     # Constraint: 0 <= len(digits) <= 4
            print("Too many digits inputted.")
            return

        for x in digits:
            if int(x) < 2:  # Constraint: digits[i] must be in range ['2', '9']
                print("Digits are out of range.")
                return
        x = 0
        rlist = []

        if length == 0:         # REMEMBER to account for spaces AND DUPLICATES
            return []

        elif length == 1:
            match digits[0]:
                case "2":
                    return phone["2"]
                case "3":
                    return phone["3"]
                case "4":
                    return phone["4"]
                case "5": 
                    return phone["5"]
                case "6":
                    return phone["6"]
                case "7":
                    return phone["7"]
                case "8":
                    return phone["8"]
                case "9":
                    return phone["9"]

        elif length == 2:
            for x in phone[digits[0]]:
                for y in phone[digits[1]]:
                    rlist.append(x+y)
            return rlist
        
        elif length == 3:
            for x in phone[digits[0]]:
                for y in phone[digits[1]]:
                    for z in phone[digits[2]]:
                        rlist.append(x+y+z)

            return rlist
        else:
            for x in phone[digits[0]]:
                for y in phone[digits[1]]:
                    for z in phone[digits[2]]:
                        for w in phone[digits[3]]:
                            rlist.append(x+y+z+w)
            
            return rlist

class Test:
    strs1 = "23"
    strs2 = ""
    strs3 = "7"
    strs4 = "234"
    strs5 = "102"

    strs = Solution()
    
    print("Case 1:", strs.letterCombinations(strs1))
    print("Case 2:", strs.letterCombinations(strs2))
    print("Case 3:", strs.letterCombinations(strs3))
    print("Case 4:", strs.letterCombinations(strs4))
    print("Case 5:", strs.letterCombinations(strs5))
