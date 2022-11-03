class Solution(object):    
    def fullJustify(self, words, maxWidth):
        def calculate(row,count,numofspaces):
            new = 0     # holds the amount of spaces
            numofspaces -= 1
            temp = ""

            if (len(row) != 1):
                count = count / 1.0
                if ((maxWidth - count) / (len(row) - 1)).is_integer():
                    new = (maxWidth - count) / (len(row) - 1)
                else:
                    new = (maxWidth - count) // (len(row) - 1)
                    
                    for j in range(0, len(row) - 1):
                        row[j] += ' ' * int(new)
                        count += int(new)
                    
                    j = 0
                    
                    while (count != maxWidth):
                        row[j] += ' '
                        count += 1
                        j += 1
                    
                    for x in row:
                        temp += x
                    
                    return temp
            else:
                new = maxWidth - count
                temp += row[0] + ' ' * int(new)
                return temp
                
            for j in range(0, len(row) - 1):
                temp += row[j] + ' ' * int(new)  # add spaces between
            temp += row[j+1]   # add the last word

            return temp

        stop = len(words)
        line = []   # line of words
        rlist = []  # list to be returned
        hold = 0    # holds the num of characters
        numofspaces = 0
        i = 0
        
        while i != stop:
            if hold + numofspaces + len(words[i]) <= maxWidth:
                line.append(words[i])
                hold += len(words[i])
                numofspaces += 1
                i += 1
                
                if i == stop:
                    temp = ""
                    if len(line) == 1:
                        temp += line[0] + ' ' * (maxWidth - hold)
                        rlist.append(temp)
                        return rlist

                    for k in range(0, len(line) - 1):
                        temp += line[k] + ' '
                    temp += line[k+1] + ' ' * ((maxWidth - hold) - len(line) + 1)
                    rlist.append(temp)
                    return rlist

            else:
                rlist.append(calculate(line,hold,numofspaces))
                line = []
                hold = 0
                numofspaces = 0
                
        return rlist

class Test:
    words1 = ["This", "is", "an","example", "of", "text", "justification."]
    words2 = ["What","must","be","acknowledgment","shall","be"]
    words3 = ["Science","is","what","we","understand","well","enough","to",
    "explain","to","a","computer.","Art","is","everything","else","we","do"]
    words4 = ["ask","not","what","your","country","can","do","for","you",
    "ask","what","you","can","do","for","your","country"]

    width1 = 16
    width3 = 20

    test = Solution()
    
    print("Example 1:")
    example1 = test.fullJustify(words1,width1)
    for lines in example1:
        print(lines)

    example2 = test.fullJustify(words2,width1)
    print("\nExample 2:")
    for lines in example2:
        print(lines)

    example3 = test.fullJustify(words3,width3)
    print("\nExample 3:")
    for lines in example3:
        print(lines)

    example4 = test.fullJustify(words4,width1)
    print("\nExample 4:")
    for lines in example4:
        print(lines)
