def compute(content):
    sum = 0
    map = {}
    to_evaluate = []
    for i, element in enumerate(content):
        element = element.rstrip()
        for j, char in enumerate(element):
            if char == 'S':
                to_evaluate.append((i, j))
            map[(i, j)] = char
    count_split = 0
    for i in range(len(content) - 1):
        new_to_evaluate = []
        for position in to_evaluate:
            if map[(position[0] + 1, position[1])] == '.':
                new_to_evaluate.append((position[0] + 1, position[1]))
            elif map[(position[0] + 1, position[1])] == '^':
                count_split += 1
                new_to_evaluate.append((position[0] + 1, position[1] - 1))
                new_to_evaluate.append((position[0] + 1, position[1] + 1))
        to_evaluate = list(set(new_to_evaluate)).copy()
    return count_split


def compute2(content):
    sum = 0
    map = {}
    to_evaluate = []

    new_content = []
    for element in content:
        element = element.rstrip()
        if 'S' in element or '^' in element:
            new_content.append(element)

    for i, element in enumerate(new_content):
        element = element.rstrip()
        for j, char in enumerate(element):
            if char == 'S':
                to_evaluate.append((i, j))
            map[(i, j)] = char
    count_split = 0

    evaluations = {}
    evaluations[to_evaluate[0]] = 1
    for i in range(len(new_content) - 1):
        new_to_evaluate = []
        for position in to_evaluate:
            if map[(position[0] + 1, position[1])] == '.':
                new_to_evaluate.append((position[0] + 1, position[1]))
                if evaluations.get((position[0] + 1, position[1])) is None:
                    evaluations[(position[0] + 1, position[1])] = 1 * evaluations[position]
                else:
                    evaluations[(position[0] + 1, position[1])] += 1 * evaluations[position]
            elif map[(position[0] + 1, position[1])] == '^':
                new_to_evaluate.append((position[0] + 1, position[1] - 1))
                if evaluations.get((position[0] + 1, position[1] - 1)) is None:
                    evaluations[(position[0] + 1, position[1] - 1)] = 1 * evaluations[position]
                else:
                    evaluations[(position[0] + 1, position[1] - 1)] += 1 * evaluations[position]
                new_to_evaluate.append((position[0] + 1, position[1] + 1))
                if evaluations.get((position[0] + 1, position[1] + 1)) is None:
                    evaluations[(position[0] + 1, position[1] + 1)] = 1 * evaluations[position]
                else:
                    evaluations[(position[0] + 1, position[1] + 1)] += 1 * evaluations[position]            
        to_evaluate = list(set(new_to_evaluate)).copy()
    for position in to_evaluate:
        sum += evaluations[position]
    return sum
