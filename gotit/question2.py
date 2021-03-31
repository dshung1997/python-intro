import ast

def get_original_labels(lines):
    n = 0
    labels = []

    for i, line in enumerate(lines.splitlines()):
        if i == 0:
            n = int(line)
        elif i == 1:
            labels = ast.literal_eval(line)
            labels = map(lambda x: int(x), labels)
        else:
            return None

    correct_labels = [x for x in range(1, n + 1)]
    original_labels = [0]
    
    for i, x in enumerate(labels):
        original_labels.append(original_labels[i] + x)

    value_to_add = 1 - min(original_labels)
    
    original_labels = [(x + value_to_add) for x in original_labels]
    sorted_labels = sorted(original_labels)

    for i, l in enumerate(sorted_labels):
        if l != correct_labels[i]:
            return None

    return original_labels

# s = """5
# [2, 2, -3, 2]
# """
# print(get_original_labels(s))

# s = """5
# [1, 2, -3, 2]
# """
# print(get_original_labels(s))