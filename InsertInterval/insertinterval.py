class Solution(object):
    def insert(self, intervals, newInterval):

        start = 0
        stop = len(intervals) - 1

        if stop == -1:
            return [newInterval]

        for i in range(start, stop):
            if newInterval[0] >= intervals[i][0]:
                if newInterval[0] <= intervals[i][1]:
                    if newInterval[1] <= intervals[i][1]:
                        return intervals    # between interval
                    elif newInterval[1] < intervals[i+1][0]:
                        intervals[i][1] = newInterval[1]
                        return intervals    # overlap 1 interval
                    else:
                        while i != stop:
                            if intervals[i+1][0] > newInterval[1]:
                                if intervals[i][1] > newInterval[0]:
                                    intervals[i][1] = newInterval[1]
                                    return intervals
                                if intervals[i][1] < newInterval[1]:
                                    intervals[i] = newInterval
                                    return intervals
                            elif intervals[i+1][1] >= newInterval[1]:
                                intervals[i][1] = intervals[i+1][1]
                                intervals.remove(intervals[i+1])
                                return intervals    # Overlap multiple
                            else:
                                intervals.remove(intervals[i+1])
                                stop -= 1

                        intervals[i][1] = newInterval[1]
                        return intervals   # overlap mutliple insert last

            elif newInterval[0] > intervals[i][1] and newInterval[1] < intervals[i+1][0]:
                intervals.insert(i+1, newInterval)
                return intervals    # no overlap and between intervals

            elif newInterval[0] < intervals[i][0]:
                if newInterval[1] < intervals[i][0]:
                    intervals.insert(i, newInterval)
                    return intervals    # no overlap at beginning
                elif newInterval[1] <= intervals[i][1]:
                    intervals[i][0] = newInterval[0]
                    return intervals    # overlap at beginning
                else:
                    while i != stop:
                        if intervals[i+1][0] > newInterval[1]:
                            if intervals[i][1] > newInterval[0] and intervals[i][0] < newInterval[0]:
                                intervals[i][1] = newInterval[1]
                                return intervals
                            if intervals[i][1] < newInterval[1]:
                                intervals[i] = newInterval
                                return intervals
                        elif intervals[i+1][1] >= newInterval[1]:
                            intervals[i+1][0] = newInterval[0]
                            intervals.remove(intervals[i])
                            return intervals    # Overlap multiple
                        else:
                            intervals.remove(intervals[i])
                            stop -= 1
                    
                    intervals[i] = newInterval
                    return intervals

        if newInterval[0] >= intervals[stop][0]:
                if newInterval[1] <= intervals[stop][1]:
                    return intervals    # between the interval
                elif newInterval[0] > intervals[stop][1]:
                    intervals.append(newInterval)
                    return intervals    # insert at end
                elif newInterval[1] >= intervals[stop][1]:
                    intervals[stop][1] = newInterval[1]
                    return intervals    # merged

        elif newInterval[0] < intervals[stop][0] and newInterval[1] < intervals[stop][0]:
            intervals.insert(stop, newInterval)
            return intervals

        elif newInterval[0] < intervals[stop][0]:
            if newInterval[1] < intervals[stop][0]:
                intervals.insert(0, newInterval)
                return intervals    # insert at first

            elif newInterval[1] > intervals[stop][1]:
                intervals[stop] = newInterval
                return intervals   # interval is wider

            elif newInterval[1] <= intervals[stop][1]:
                intervals[stop][0] = newInterval[0]
                return intervals    # merge

        return intervals

class Test:
    interval1 = [[5,9], [12,13]]
    new1 = [10,11]
    interval2 = [[1,2], [3,5], [6,7], [8,10], [12,16]]
    new2 = [4,8]
    interval3 = [[1,3], [6,9]]
    new3 = [2,10]
    interval4 = [[1,2], [3,5], [6,7]]
    new4 = [4,6]

    test = Solution()

    print("Example 1: ", test.insert(interval1,new1))
    print("Example 2: ", test.insert(interval2,new2))
    print("Example 3: ", test.insert(interval3,new3))
    print("Example 4: ", test.insert(interval4,new4))
