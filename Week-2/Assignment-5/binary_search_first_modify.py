from typing import List


def binary_search_first(numbers: List, target: int) -> int:
    left = 0
    right = len(numbers) - 1
        
    while left <= right:            
        mid = (left + right) // 2   # 向下取整數
        if target <= numbers[mid]:  # target 小於中間值就搜尋左邊 且 不要 target 找到就停，找到時強制再往左搜尋        
            right = mid - 1         # 當 target 找到且 left = right，此時要 left 的 index，故讓 right -1 使得 left < right，break         
        else:                       # target 大就搜尋右邊
            left = mid + 1          # 目標是讓 left 停在 target 或 大於 target 的最小 index
    return left


# test run for binary_search_first
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))  # 1
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))  # 2
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3))  # 2





# more test (sorted random 42 int in list)
# print(binary_search_first([
#                               3, 11, 12, 13, 15, 16, 16, 20, 23, 24, 25, 26, 29,
#                               29, 29, 31, 36, 38, 38, 43, 44, 50, 51, 52, 56, 56,
#                               57, 60, 62, 66, 66, 69, 70, 71, 72, 74, 75, 82, 90,
#                               91, 95, 100
#                            ], 16))  # 5



# print(binary_search_first([
#                               3, 11, 12, 13, 15, 16, 16, 20, 23, 24, 25, 26, 29,
#                               29, 29, 31, 36, 38, 38, 43, 44, 50, 51, 52, 56, 56,
#                               57, 60, 62, 66, 66, 69, 70, 71, 72, 74, 75, 82, 90,
#                               91, 95, 100
#                            ], 92))  # 40

# print(binary_search_first([
#                               3, 11, 12, 13, 15, 16, 16, 20, 23, 24, 25, 26, 29,
#                               29, 29, 31, 36, 38, 38, 43, 44, 50, 51, 52, 56, 56,
#                               57, 60, 62, 66, 66, 69, 70, 71, 72, 74, 75, 82, 90,
#                               91, 95, 100
#                            ], 14))  # 4

# print(binary_search_first([
#                               3, 11, 12, 13, 15, 16, 16, 20, 23, 24, 25, 26, 29,
#                               29, 29, 31, 36, 38, 38, 43, 44, 50, 51, 52, 56, 56,
#                               57, 60, 62, 66, 66, 69, 70, 71, 72, 74, 75, 82, 90,
#                               91, 95, 100
#                            ], 3))  # 0

# print(binary_search_first([
#                               3, 11, 12, 13, 15, 16, 16, 20, 23, 24, 25, 26, 29,
#                               29, 29, 31, 36, 38, 38, 43, 44, 50, 51, 52, 56, 56,
#                               57, 60, 62, 66, 66, 69, 70, 71, 72, 74, 75, 82, 90,
#                               91, 95, 100
#                            ], 100))  # 41

# print(binary_search_first([
#                               3, 11, 12, 13, 15, 16, 16, 20, 23, 24, 25, 26, 29,
#                               29, 29, 31, 36, 38, 38, 43, 44, 50, 51, 52, 56, 56,
#                               57, 60, 62, 66, 66, 69, 70, 71, 72, 74, 75, 82, 90,
#                               91, 95, 100
#                            ], 102))  # 42





