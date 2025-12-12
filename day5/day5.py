def compute(content):
    sum = 0
    intervals = []
    values = []
    for element in content:
        element = element.rstrip()
        if '-' in element:
            intervals.append((int(element.split('-')[0]), int(element.split('-')[1])))
        else:
            if element != '':
                values.append(int(element))

    for value in values:
        for interval in intervals:
            if value >= interval[0] and value <= interval[1]:
                sum += 1
                break
    return sum

def join_intervals(intervals):
    to_remove = []
    to_add = []
    for i, interval in enumerate(intervals):
        for j, other_interval in enumerate(intervals):
            if i != j and interval[0] <= other_interval[1] and interval[0] >= other_interval[0]:
                to_remove.append(i)
                to_remove.append(j)
                to_add.append((min(interval[0], other_interval[0]), max(interval[1], other_interval[1])))
                break
            elif i != j and interval[1] >= other_interval[0] and interval[1] <= other_interval[1]:
                to_remove.append(i)
                to_remove.append(j)
                to_add.append((min(interval[0], other_interval[0]), max(interval[1], other_interval[1])))
                break
        if len(to_remove) > 0:
            for index in sorted(to_remove, reverse=True):
                intervals.pop(index)
            intervals.extend(to_add)
            break
    return intervals


def compute2(content):
    sum = 0
    intervals = []
    for element in content:
        element = element.rstrip()
        if '-' in element:
            intervals.append((int(element.split('-')[0]), int(element.split('-')[1])))
    
    while(1):
        size = len(intervals)
        intervals = join_intervals(intervals)
        if size == len(intervals):
            break
    
    for interval in intervals:
        sum += (interval[1] - interval[0]) + 1
    return sum