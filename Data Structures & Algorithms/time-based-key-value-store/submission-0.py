class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append([timestamp, value])   
    def get(self, key: str, timestamp: int) -> str:
        valueToReturn = ""
        if(key not in self.store):
            return valueToReturn
        else:
            print("Getting", self.store[key])
            for val in self.store[key]:
                if(val[0] <= timestamp):
                    valueToReturn = val[1]

        return valueToReturn
