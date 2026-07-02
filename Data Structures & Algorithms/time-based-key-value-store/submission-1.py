class TimeMap:

    def __init__(self):
        self.store= defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value,timestamp))
        #self.store[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        result=""

        for value ,ts in self.store[key]:
            if ts <= timestamp:

                result=value
            
                
                
            
        return result
        
        
        
