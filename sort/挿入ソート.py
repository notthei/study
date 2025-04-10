"""挿入ソート
要素を適切な場所へ挿入すること
"""
def insert_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]  # 現在の要素をkeyに保存
        j = i - 1
        
        while j >= 0 and arr[j] > key:  # keyより大きい要素を右にシフト
            arr[j + 1] = arr[j]
            j -= 1
        
      
        arr[j + 1] = key  # keyを適切な位置に挿入


data = [12, 11, 13, 5, 6]
print("ソート前:", data)
insert_sort(data)
print("ソート後:", data)