def twoSum(nums, target):
    hash_table = {}  # O(1)
    for i, num in enumerate(nums): # O(n * 2) 
        if target - num in hash_table:
            return ([hash_table[target - num], i])  
            break
        # 到第2個相同數字才判斷避免相減後數字剛好一樣
        hash_table[num] = i    # O(1)
    return []  # O(1)  


# test
print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(twoSum([3, 3], 6))  # [0, 1]
print(twoSum([7, 3, 3, 8, 9], 5))  # []


# time complexity
# 假設每一行程式碼運行時間T(n)固定
# 演算法的時間複雜度，用來度量演算法的執行時間，記作: T(n) = O(f(n))
# 時間複雜度 O(n*2+3) 當 n 很大並去除常數 =>  O(n)

# test
