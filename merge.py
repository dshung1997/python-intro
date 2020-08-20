def merge(intervals):
    if len(intervals) == 0:
        return []

    sorted_intervals = sorted(intervals, key=lambda i: i[1])

    result = []

    start, end = sorted_intervals[0]

    for i in sorted_intervals:
        if i[0] <= end:
            end = max(end, i[1])
            start = min(start, i[0])
        else:
            result.append([start, end])
            start, end = i

    result.append([start, end])
    return result


print(merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
