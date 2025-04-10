
""" 線形探索
配列に格納されたデータの先頭から順番に、ターゲットデータと一致するか比較していく
"""

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # 値が存在した場合、そのインデックスを返す
    return -1  # 値が存在しない場合は-1を返す


numbers = [5, 3, 8, 4, 2]
target = 4

result = linear_search(numbers, target)

if result != -1:
    print(f"{target} は {result} に存在します")
else:
    print(f"{target} は存在しません")
