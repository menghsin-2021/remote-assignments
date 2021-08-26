from typing import List


def find_max(numbers: List[int]) -> int:
	max_number = numbers[0]  # 將第一個數設為最大
	for number in numbers: 	# 一個一個比較	
		if max_number <= number:
			max_number = number
	return max_number


def find_position(numbers: List[int], target: int) -> int:
	for i in range(len(numbers)):
		if numbers[i] == target:  # 當找到值
			return i			
	return -1  # 找不到回傳 -1



# function test
print(find_max([1, 2, 4, 5]))  # 5
print(find_max([5, 2, 7, 1, 6]))  # 7

print(find_position([5, 2, 7, 1, 6], 5))  # 0
print(find_position([5, 2, 7, 1, 6], 7))  # 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))  # 2
print(find_position([5, 2, 7, 1, 6], 8))  # -1






# def find_position_enumerate(numbers: List[int], target: int) -> int:
# 	for i, number in enumerate(numbers):
# 		if target == number:
# 				return i
# 	return -1

# print(find_position_enumerate([5, 2, 7, 1, 6], 5))
# print(find_position_enumerate([5, 2, 7, 1, 6], 7))
# print(find_position_enumerate([5, 2, 7, 7, 7, 1, 6], 7))
# print(find_position_enumerate([5, 2, 7, 1, 6], 8))