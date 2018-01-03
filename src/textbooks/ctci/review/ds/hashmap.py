"""

Basically the searching takes O(1) time.
But the collisions happen it takes O(n) time for searching.


Collisions



"""

class HashMap(object):

    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def add(self, key, value):
        hash_key = self._get_hash(key)
        hash_value = [key, value]

        if self.map[hash_key] is None:
            self.map[hash_key] = list([hash_value])
            return True
        else:
            for h_key, h_value in self.map[hash_key]:
                if h_key == key:
                    h_value = value
                    return True
            self.map[hash_key].append(hash_value)
            return True

    def get(self, key):
        hash_key = self._get_hash(key)

        if self.map[hash_key] is not None:
            for h_key, h_value in self.map[hash_key]:
                if h_key == key:
                    return h_value
        return None

    def delete(self, key):
        hash_key = self._get_hash(key)

        if self.map[hash_key] is None:
            return False

        for i, hash_pair in enumerate(self.map[hash_key]):
            if hash_pair[0] == key:
                self.map[hash_key].pop(i)
                return True

    def _get_hash(self, key):
        hash_key = 0
        for char in str(key):
            hash_key += ord(char)
        return hash_key % self.size

    def describe(self):
        print("\n-------------------------------------------\n")
        for pair in self.map:
            print(pair)

        print("\n")
        print("You have {} slots of hashmap".format(len(self.map)))
        print("-----------------------------------------\n")






if __name__ == '__main__':
    hashmap = HashMap()
    hashmap.add("Tsukamoto", "01")
    hashmap.add("Tanaka", "02")
    hashmap.add("Tsuchida", "03")
    hashmap.add("Takenaka", "04")
    hashmap.add("Honma", "05")
    hashmap.add("Yamada", "06")

    hashmap.describe()

    print(hashmap.get("Tsukamoto"))
    print(hashmap.get("Honma"))

    hashmap.delete("Tanaka")
    hashmap.delete("Takenaka")
    hashmap.delete("Yamada")

    hashmap.describe()
