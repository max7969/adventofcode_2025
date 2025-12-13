def compute(content):
    sum = 0
    lines = []
    for element in content:
        new_line = []
        values = element.split(' ')
        for value in values:
            value = value.rstrip()
            if value != '':
                new_line.append(value)
        lines.append(new_line)

    columns_len = len(lines[0])
    lines_len = len(lines)
    for i in range(columns_len):
        values = []
        for j in range(lines_len-1):
            values.append(lines[j][i])
        expression = lines[lines_len-1][i].join(values)
        sum += eval(expression)
    return sum


def compute2(content):
    sum = 0
    to_consider = len(content) - 1
    columns = {}
    for i, element in enumerate(content):
        if i < to_consider:
            for j, char in enumerate(element):
                if columns.get(j) is None:
                    columns[j] = char
                else:
                    columns[j] += char
    symbols = []
    for char in content[len(content) - 1]:
        if char == '+' or char == '*':
            symbols.append(char)
    index_char = 0
    expression = []
    for i in range(len(columns)):
        if columns[i].rstrip() == '':
            sum += eval(symbols[index_char].join(expression))
            index_char += 1
            expression = []
        else:
            expression.append(columns[i])

    return sum