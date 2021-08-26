from typing import List, Dict


def count(input: List[str]) -> Dict[str, int]:
    words_counts = {}

    for word in input1:
        if word in words_counts:
            words_counts[word] += 1
        else:
            words_counts[word] = 1

    return words_counts

# test run for count
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input: List[Dict]) -> Dict[str, int]:
    grouped_words_counts = {}

    for words_dict in input2:
        word = words_dict['key']
        count = words_dict['value']
        if word in grouped_words_counts:
            grouped_words_counts[word] += count
        else:
            grouped_words_counts[word] = count
            
    return grouped_words_counts


# test run for group_by_key
input2 = [
    {'key': 'a', 'value': 3},
    {'key': 'b', 'value': 1},
    {'key': 'c', 'value': 2},
    {'key': 'a', 'value': 3},
    {'key': 'c', 'value': 5},
]

print(group_by_key(input2))  # {'a': 6, 'b': 1, 'c': 7}
















