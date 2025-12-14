from collections import deque, defaultdict
import heapq
import z3

from math import gcd


def find_shortest(start, end, possibilities):
    if start == end:
        return 0
    
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        pos, distance = queue.popleft()
        
        for possibility in possibilities:
            new_pos = tuple((a + b) % 2 for a, b in zip(pos, possibility))
            
            if new_pos == end:
                return distance + 1
            
            if new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos, distance + 1))
    return float('inf')


def compute(content):
    sum = 0

    machines = {}
    for i, element in enumerate(content):
        element = element.rstrip()
        line = element.split(' ')
        first_key = line[0].replace('[', '').replace(']', '').replace('.', '0').replace('#', '1')
        key = tuple([int(char) for char in first_key])
        machines[i] = []
        machines[i].append(key)
        possibilities = []
        for j in range(1, len(line) - 1):
            number = [0] * len(key)
            indexes = line[j].replace('(', '').replace(')', '').split(',')
            for index in indexes:
                number[int(index)] = 1
            possibilities.append(number)
        machines[i].append(possibilities)

    for machine in machines:
        sum += find_shortest(tuple([0] * len(machines[machine][0])), machines[machine][0], machines[machine][1])

    return sum

def solve_buttons(buttons, joltages):
    solver = z3.Optimize()
    button_presses = z3.IntVector("button_presses", len(buttons))

    button_indices = defaultdict(list)
    for i, btn in enumerate(buttons):
        solver.add(button_presses[i] >= 0)
        for j in btn:
            button_indices[int(j)].append(i)

    for j, indices in button_indices.items():
        solver.add(joltages[j] == sum(button_presses[i] for i in indices))

    presses = z3.Sum(button_presses)
    solver.minimize(presses)
    solver.check()
    
    return solver.model().eval(presses).as_long()

def compute2(content):
    sum = 0

    machines = {}
    for i, element in enumerate(content):
        element = element.rstrip()
        line = element.split(' ')
        first_key = line[len(line) - 1].replace('{', '').replace('}', '')
        key = tuple([int(char) for char in first_key.split(',')])
        machines[i] = []
        machines[i].append(key)
        possibilities = []
        for j in range(1, len(line) - 1):
            number = [0] * len(key)
            indexes = [int(e) for e in line[j].replace('(', '').replace(')', '').split(',')]
            possibilities.append(tuple(indexes))
        machines[i].append(possibilities)

    for machine in machines:
        sum += solve_buttons(machines[machine][1], machines[machine][0])
    return sum
