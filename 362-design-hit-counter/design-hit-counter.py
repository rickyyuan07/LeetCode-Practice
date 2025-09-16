class HitCounter:

    def __init__(self):
        self.log = []

    def hit(self, timestamp: int) -> None:
        while self.log and self.log[0] <= timestamp - 300:
            self.log.pop(0)
        self.log.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.log and self.log[0] <= timestamp - 300:
            self.log.pop(0)
        
        return len(self.log)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)