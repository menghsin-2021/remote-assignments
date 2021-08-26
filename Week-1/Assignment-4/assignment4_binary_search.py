from typing import List


def binary_search_position(numbers: List, target: int) -> int:
	index = -1  # 都找不到就回傳 -1
	min_index = 0
	max_index = len(numbers) - 1
		
	while max_index >= min_index:
		middle_index = (max_index + min_index) // 2  # 向下取整數
		if target == numbers[middle_index]:  
			index = middle_index  # 找到就將 index 設為當前位置
			break
		elif target < numbers[middle_index]:  # target 小就搜尋左邊
			max_index = middle_index - 1
			continue
		else:  # target 大就搜尋右邊
			min_index = middle_index + 1
			continue

	return index  # 都找不到就回傳 -1



# function test
print(binary_search_position([1, 2, 5, 6, 7], 1))  # 0
print(binary_search_position([1, 2, 5, 6, 7], 6))  # 3




# Test

# print(binary_search_position([
# 								3, 11, 12, 13, 15, 16, 16, 20, 23, 24, 25, 26, 29,
# 								29, 29, 31, 36, 38, 38, 43, 44, 50, 51, 52, 56, 56,
# 								57, 60, 62, 66, 66, 69, 70, 71, 72, 74, 75, 82, 90,
# 								91, 95, 100
# 							 ], 3))  # 0


# print([
# 								3, 11, 12, 13, 15, 16, 16, 20, 23, 24, 25, 26, 29,
# 								29, 29, 31, 36, 38, 38, 43, 44, 50, 51, 52, 56, 56,
# 								57, 60, 62, 66, 66, 69, 70, 71, 72, 74, 75, 82, 90,
# 								91, 95, 100
# 							 ].index(3))  # 0

# print(binary_search_position([
# 								3, 11, 12, 13, 15, 16, 16, 20, 23, 24, 25, 26, 29,
# 								29, 29, 31, 36, 38, 38, 43, 44, 50, 51, 52, 56, 56,
# 								57, 60, 62, 66, 66, 69, 70, 71, 72, 74, 75, 82, 90,
# 								91, 95, 100
# 							 ], 92))  # -1


# 1. Let min = 1, and max = n
# 2. Guess the average of max and min, rounded down so that it is an integer.
# 3. If you guessed the number, stop. You found it!
# 4. If the guess was too low, set min to be one larger than the guess.
# 5. If the guess was too high, set max to be one smaller than the guess.
# 6. Go back to step two.


