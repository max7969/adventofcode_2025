def compute(content):
    total = 0
    forms = {}
    for i in range(0, 30, 5):
        key = int(content[i].rstrip().split(':')[0])
        size  = content[i+1].count('#')
        size += content[i+2].count('#')
        size += content[i+3].count('#')
        forms[key] = size

    for i in range(30, len(content)):
        element = content[i].rstrip().split(': ')
        forms_size = [int(nb) for nb in element[1].split(' ')]
        for i, size in enumerate(forms_size):
            forms_size[i] = size * forms[i]
        if eval(element[0].replace('x', '*')) >= sum(forms_size):
            total += 1
    return total




def compute2(content):
    return 0
