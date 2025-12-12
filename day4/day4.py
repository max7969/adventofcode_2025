def compute(content):
    sum = 0
    positions = {}
    for i, element in enumerate(content):
        element = element.rstrip()
        for j, char in enumerate(element):
            if char == '@':
                positions[i, j] = 1
    for position in positions:
        if get_sum_neighbors(position, positions) <= 4:
            sum += 1
    return sum

def get_sum_neighbors(position, positions):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (position[0] + i, position[1] + j) in positions:
                sum += 1
    return sum

def treat_positions(positions):
    to_remove = []
    sum = 0
    for position in positions:
        if get_sum_neighbors(position, positions) <= 4:
            to_remove.append(position)
            sum += 1
    for position in to_remove:
        positions.pop(position)
    return sum, positions

def compute2(content):
    sum = 0
    positions = {}
    for i, element in enumerate(content):
        element = element.rstrip()
        for j, char in enumerate(element):
            if char == '@':
                positions[i, j] = 1
    while(1):
        size = len(positions)
        result, positions = treat_positions(positions)
        sum += result
        if size == len(positions):
            break
    return sum