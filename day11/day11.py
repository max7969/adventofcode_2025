from functools import cache

class Node:
    def __init__(self, key, childs):
        self.key = key
        self.childs = childs

def compute(content):
    sum = 0
    nodes = {}
    nodes['out'] = Node('out', [])
    for element in content:
        element = element.rstrip()
        key, childs = element.split(': ')
        childs = childs.split(' ')
        node = Node(key, childs)
        nodes[key] = node
    you_array = ['you']
    outs = []
    while(1):
        new_elements = []
        for element in you_array:
            if element != 'out':
                new_elements.extend(nodes[element].childs)
            elif element == 'out':
                outs.append(element)
        if len(new_elements) == 0:
            break
        you_array = new_elements
    return len(outs)




def compute2(content):
    nodes = {}
    nodes['out'] = []
    special = {'fft', 'dac'}  # Noeuds à tracker
    
    @cache
    def count_paths(node, visited_special):
        if node == 'out':
            return 1 if 'fft' in visited_special and 'dac' in visited_special else 0
        
        if node not in nodes:
            return 0
        
        # Mettre à jour les noeuds spéciaux visités
        if node in special:
            visited_special = tuple(sorted(set(visited_special) | {node}))
        
        return sum(count_paths(child, visited_special) for child in nodes[node])

    for element in content:
        element = element.rstrip()
        key, childs = element.split(': ')
        nodes[key] = childs.split(' ')

    return count_paths('svr', ())
