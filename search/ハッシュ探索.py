
""" ハッシュ探索
GPTパワーをお借りしました。
ターゲットデータのハッシュ値を用いてデータ本体の代わりに比較に用いる
"""
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # 各インデックスにリストを持つ

    def _hash(self, key):
        """キーをハッシュ化してインデックスを取得する"""
        return hash(key) % self.size

    def insert(self, key, value):
        """ハッシュテーブルにキーと値を挿入する"""
        index = self._hash(key)
        # 既存のキーがあれば更新
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # 新しいキーを追加
        self.table[index].append((key, value))

    def search(self, key):
        """キーに対応する値を検索する"""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # キーが見つからない場合

    def delete(self, key):
        """キーとその値を削除する"""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False  # キーが見つからない場合

# 使用例
if __name__ == "__main__":
    ht = HashTable()
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("orange", 3)

    print(ht.search("banana"))  # 出力: 2
    print(ht.search("grape"))   # 出力: None

    ht.delete("banana")
    print(ht.search("banana"))  # 出力: None