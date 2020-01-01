class queue:
    def __init__(self):
        self.store = []
        self.length = 0
    def enqueue(self,x):
        self.store = self.store + [x]
        self.length = self.length + 1
        return True
    def dequeue(self):
        if self.length == 0:
            return [False,0]
        else:
            save = (self.store)[0]
            self.store = (self.store)[1:]
            self.length = self.length - 1
            return [True,save]
