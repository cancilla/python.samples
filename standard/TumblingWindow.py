class TumblingWindow:
    def __init__ (self, length):
        self.length = length
        self.window = []
    def __call__ (self, tuple):
        self.window.append(tuple)
        if(len(self.window) == self.length):
             temp = self.window
             self.window = []
             return temp

