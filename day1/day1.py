def compute(content):
    sum = 0
    total = 50
    for element in content:
        element = int(element.rstrip().replace('L', '-').replace('R', ''))
        element = element % 100
        total += element
        if total % 100 == 0:
            sum += 1
    return sum

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.count = 0
        self.left = left
        self.right = right

def compute2(content):

    nodes = []
    for i in range(100):
        nodes.append(Node(i))
    for node in nodes:
        node.left = nodes[(node.value - 1) % 100]
        node.right = nodes[(node.value + 1) % 100]
    
    current_node = nodes[50]

    for element in content:
        element = int(element.rstrip().replace('L', '-').replace('R', ''))
        if element > 0:
            for i in range(element):
                current_node = current_node.right
                current_node.count += 1
        else:
            for i in range(abs(element)):
                current_node = current_node.left
                current_node.count += 1
    return nodes[0].count