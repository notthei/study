
""" 二分探索
データ列の中央の値と大小比較をし、目的とするデータがどちらにあるかを判断する
"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # 中間インデックスを計算
        
        if arr[mid] == target:  #中間値と一致する場合
            return mid
       
        elif arr[mid] > target: #中間値より小さい場合
            right = mid - 1
        
        else:                   #中間値より大きい場合
            left = mid + 1

   
    return -1    # みつからなかった場合


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(numbers, target)

if result != -1:
    print(f" {target} は {result} にあります。")
else:
    print(f" {target} は存在しません。")