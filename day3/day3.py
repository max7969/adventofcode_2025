def compute(content):
    sum = 0
    for element in content:
        digits = [int(c) for c in element.rstrip()]
        max_value = max(digits[:-1])
        max_index = digits.index(max_value)
        max_second = max(digits[max_index + 1:])
        sum += max_value * 10 + max_second

    return sum

def max_value_and_index(digits):
    max_value = max(digits)
    max_index = digits.index(max_value)
    return max_value, max_index

def compute2(content):
    sum = 0
    for element in content:
        digits = [int(c) for c in element.rstrip()]
        result = 0
        for i in range (11, -1, -1):
            max_value, max_index = max_value_and_index(digits[0:(len(digits) - i)])
            result += max_value * 10 ** i
            digits = digits[max_index + 1:]
        sum += result

    return sum