class Solution(object):
    def merge(self, intervals):

        if len(intervals) == 1:
            return intervals

        intervals.sort()
        i = 1
        end = len(intervals)

        while i != end:
            if intervals[i][0] <= intervals[i-1][1] and intervals[i][1] >= intervals[i-1][1]:
                intervals[i-1][1] = intervals[i][1]
                intervals.remove(intervals[i])
                i -= 1
                end -= 1
            elif intervals[i][1] < intervals[i-1][1] and intervals[i][0] <= intervals[i-1][1]:
                intervals.remove(intervals[i])
                i -= 1
                end -= 1

            i += 1

        return intervals

class Test:
    interval1 = [[1,3], [2,6], [8,10], [15,18]]
    interval2 = [[1,4], [4,5]]
    interval3 = [[1,4], [2,3]]
    
    test = Solution()

    print("Example 1: ", test.merge(interval1))
    print("Example 2: ", test.merge(interval2))
    print("Example 3: ", test.merge(interval3))
    