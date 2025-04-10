# 選択ソート
"""
配列の要素を順番に見ていき、要素を最大値と入れ替えていく
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):# 未ソート部分を走査
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # 最小値を現在の位置と交換
    return arr


list = [64, 25, 12, 22, 11]
print(selection_sort(list))