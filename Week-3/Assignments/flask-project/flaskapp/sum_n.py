# 遞迴
def sum_n_recu(num):
    if num == 1:
        return 1
    return num + sum_n_recu(num-1)

# 當用遞迴方法，且 N 太大 => stack overflow（堆疊溢位，使用過多記憶體導致溢出）
# RecursionError: maximum recursion depth exceeded
# 解決這個問題有兩個辦法：#
# 1. 重新寫遞迴的演算法（優化）
# 2. 設定遞迴深度限制（雖然不推薦，但這個方法比較快，可以在衡量自己的設備後選擇）

# 迴圈
def sum_n_loop(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

# 公式
def sum_f(num):
    return int((1 + num) * num / 2)

