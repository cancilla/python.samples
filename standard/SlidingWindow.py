class SlidingWindow:
    def __init__ (self, length, triggerCount=1):
        self.length = length
        self.window = []
        self.triggerCount = triggerCount
        self.count = 0
    def __call__ (self, tuple):
        self.window.append(tuple)
        if(len(self.window) > self.length):
            self.window.pop(0)    

        if(++self.count == self.triggerCount):
            self.count = 0
            return self.window
