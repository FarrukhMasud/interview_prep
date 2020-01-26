class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return None
        arr = self.store[key]
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = int((l + r) / 2)
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            if arr[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if r < 0:
            return ""
        return arr[r][1]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("love", "high", 10)
obj.set("love", "low", 20)
print(obj.get("love", 1))

# ["TimeMap","set","set","get","get","get","get","get"]
# [["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
