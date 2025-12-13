from shapely.geometry import Polygon, box

def compute(content):
    sum = 0

    tiles = []
    for element in content:
        element = element.rstrip()
        values = element.split(',')
        tiles.append((int(values[0]), int(values[1])))
    areas = {}
    for i, tile in enumerate(tiles):
        for j, tile2 in enumerate(tiles):
            if i != j:
                if (j, i) not in areas:
                    areas[(i, j)] = (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
    
    sorted_areas = dict(sorted(areas.items(), key=lambda x: x[1], reverse=True))

    (i, j), area = list(sorted_areas.items())[0]

    return area


def compute2(content):
    sum = 0

    tiles = []
    for element in content:
        element = element.rstrip()
        values = element.split(',')
        tiles.append((int(values[0]), int(values[1])))
    areas = {}

    polygon = Polygon(tiles)
    for i, tile in enumerate(tiles):
        for j, tile2 in enumerate(tiles):
            if i != j:
                if (j, i) not in areas:
                    rectangle = box(min(tiles[i][0], tiles[j][0]), min(tiles[i][1], tiles[j][1]), max(tiles[i][0], tiles[j][0]), max(tiles[i][1], tiles[j][1]))
                    if polygon.contains(rectangle):
                        areas[(i, j)] = (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
    
    sorted_areas = dict(sorted(areas.items(), key=lambda x: x[1], reverse=True))

    (i, j), area = list(sorted_areas.items())[0]

    return area
