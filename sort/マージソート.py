""" マージソート
1, 配列を２つに分割する
2, 各々をソートする
3, 二つのソートされた配列をマージする
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2# 配列を2つの半分に分割
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half) # 左半分をソート
        merge_sort(right_half) # 右半分

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):# 左右の配列をマージ
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half): # 左側の残りの要素を追加
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half): # 右側の残りの要素を追加
            arr[k] = right_half[j]
            j += 1
            k += 1


data = [38, 27, 43, 3, 9, 82, 10]
print("ソート前:", data)
merge_sort(data)
print("ソート後:", data)