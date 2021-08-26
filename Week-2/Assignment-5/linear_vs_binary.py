from typing import List
import random
from memory_profiler import memory_usage
import time


def sorted_random_list(numbers):   
    random_list = []
    
    for i in range(0, numbers):
        n = random.randint(1, numbers)
        random_list.append(n)
    
    sorted_random_list = sorted(random_list)
    return sorted_random_list


def find_position(numbers: List[int], target: int) -> int:
    for i in range(len(numbers)):
        if numbers[i] == target:  # 當找到值
            return i            
    return -1  # 找不到回傳 -1


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


# settings
numbers = 10000000
target = 7648000
sorted_random_list = sorted_random_list(numbers)
# print(sorted_random_list)
print(f'length of data: {numbers}')
print(f'target: {target}\n')


# linear-search
print('using linear search')
print(f'Mem: {memory_usage()} MB')
start_time = time.time() # 使用 time 模組的 time 功能 紀錄當時系統時間 從 start_time 

print(f'found position: {find_position(sorted_random_list, target)}')

end_time = time.time() # 使用 time 模組的 time 功能 紀錄當時系統時間 到 end_time
print(f'elapsed {end_time - start_time} seconds')
print(f'Mem: {memory_usage()} MB\n')


# binary-search
print('using binary search')
print(f'Mem: {memory_usage()} MB')
start_time = time.time() 

print(f'found position: {binary_search_first(sorted_random_list, target)}')

end_time = time.time() 
print(f'elapsed {end_time - start_time} seconds')
print(f'Mem: {memory_usage()} MB')


# test result:

# 沒找到
# length of data: 10000000
# target: 764800

# using linear search
# Mem: [405.40625] MB
# found position: -1
# elapsed 1.8355958461761475 seconds
# Mem: [405.41796875] MB

# using binary search
# Mem: [405.41796875] MB
# found position: 764581
# elapsed 0.0 seconds
# Mem: [405.41796875] MB


# 資料在前面
# length of data: 10000000
# target: 764800

# using linear search
# Mem: [406.28515625] MB
# found position: 763548
# elapsed 0.15361952781677246 seconds
# Mem: [406.296875] MB

# using binary search
# Mem: [406.296875] MB
# found position: 763548
# elapsed 0.0 seconds
# Mem: [406.296875] MB


# 資料在後面
# length of data: 10000000
# target: 7648000

# using linear search
# Mem: [406.43359375] MB
# found position: 7646238
# elapsed 1.447573184967041 seconds
# Mem: [406.4453125] MB

# using binary search
# Mem: [406.4453125] MB
# found position: 7646238
# elapsed 0.0 seconds
# Mem: [406.4453125] MB


# 老師建議
# 以後可以用 ms 記錄時間，會更明顯 (milli-second)
# time.time()*1000 ms



