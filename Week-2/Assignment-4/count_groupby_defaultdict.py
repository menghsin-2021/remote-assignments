from typing import List, Dict
from collections import defaultdict


def count(input: List[str]) -> Dict[str, int]:
    counted_dict = defaultdict(int)

    for alphabet in input1:
        counted_dict[alphabet] += 1

    return counted_dict

# test run for count
input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # defaultdict(<class 'int'>, {'a': 3, 'b': 1, 'c': 2, 'x': 1})

def group_by_key(input: List[Dict]) -> Dict[str, int]:
    grouped_words_counts = defaultdict(int)

    for words_dict in input2:
        word = words_dict['key']
        count = words_dict['value']
        grouped_words_counts[word] += count

    return grouped_words_counts

# test run for group_by_key
input2 = [
    {'key': 'a', 'value': 3},
    {'key': 'b', 'value': 1},
    {'key': 'c', 'value': 2},
    {'key': 'a', 'value': 3},
    {'key': 'c', 'value': 5},
]

print(group_by_key(input2))  # defaultdict(<class 'int'>, {'a': 6, 'b': 1, 'c': 7})