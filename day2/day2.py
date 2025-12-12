def compute(content):
    couples = content[0].split(',')
    sum = 0
    for couple in couples:
        ids = couple.split('-')
        first = int(ids[0])
        second = int(ids[1])
        
        for element in range(first, second + 1):
            id = str(element)
            mid = len(id) // 2
            first_half = id[:mid]
            second_half = id[mid:]
            if first_half == second_half:
                sum += element
    return sum

def check_id_with_n_parts(id, n):
    part_size = len(id) // n
    split = [id[i:i + part_size] for i in range(0, len(id), part_size)]
    if all(part == split[0] for part in split):
        return True
    else:
        return False

def check_id(id):
    length = len(id)
    result = {}
    for n in range(2, length + 1):
        if length % n == 0:
            if check_id_with_n_parts(id, n):
                return int(id)
    return 0


def compute2(content):
    couples = content[0].split(',')
    sum = 0
    for couple in couples:
        ids = couple.split('-')
        first = int(ids[0])
        second = int(ids[1])
        
        for element in range(first, second + 1):
            sum += check_id(str(element))
    return sum