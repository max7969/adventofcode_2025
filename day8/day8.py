def compute(content, size=10):
    sum = 0

    boxes = []
    for element in content:
        element = element.rstrip()
        values = element.split(',')
        boxes.append((int(values[0]), int(values[1]), int(values[2])))
    distances = {}
    for i, box in enumerate(boxes):
        for j, box2 in enumerate(boxes):
            if i != j:
                if (j, i) not in distances:
                    distances[(i, j)] = ((box[0] - box2[0]) ** 2 + (box[1] - box2[1]) ** 2 + (box[2] - box2[2]) ** 2) ** 0.5
    
    sorted_distances = dict(sorted(distances.items(), key=lambda x: x[1]))

    circuits = [[i] for i, box in enumerate(boxes)]
    count = 0
    for (i, j), dist in sorted_distances.items():
        if count >= size:
            break
        new_circuit = []
        to_remove = []
        for l, circuit in enumerate(circuits):
            if i in circuit:
                new_circuit.extend(circuit)
                to_remove.append(l)
            if j in circuit:
                new_circuit.extend(circuit)
                to_remove.append(l)

        to_remove = list(set(to_remove))
        for index in sorted(to_remove, reverse=True):
            circuits.pop(index)
        circuits.append(list(set(new_circuit)))

        count += 1

    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])


def compute2(content):
    sum = 0

    boxes = []
    for element in content:
        element = element.rstrip()
        values = element.split(',')
        boxes.append((int(values[0]), int(values[1]), int(values[2])))
    distances = {}
    for i, box in enumerate(boxes):
        for j, box2 in enumerate(boxes):
            if i != j:
                if (j, i) not in distances:
                    distances[(i, j)] = ((box[0] - box2[0]) ** 2 + (box[1] - box2[1]) ** 2 + (box[2] - box2[2]) ** 2) ** 0.5
    
    sorted_distances = dict(sorted(distances.items(), key=lambda x: x[1]))

    circuits = [[i] for i, box in enumerate(boxes)]
    for (i, j), dist in sorted_distances.items():

        new_circuit = []
        to_remove = []
        for l, circuit in enumerate(circuits):
            if i in circuit:
                new_circuit.extend(circuit)
                to_remove.append(l)
            if j in circuit:
                new_circuit.extend(circuit)
                to_remove.append(l)

        to_remove = list(set(to_remove))
        for index in sorted(to_remove, reverse=True):
            circuits.pop(index)
        circuits.append(list(set(new_circuit)))
        if len(circuits) == 1:
            return boxes[i][0] * boxes[j][0]
    return 0
