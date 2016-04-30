from scipy import signal

class Lowpass:
    def __init__ (self, order, cutoffFreq, sampleRate):
        Wn = cutoffFreq / (0.5 * sampleRate)
        self.b, self.a = signal.butter(order, Wn, btype='lowpass')
    def __call__ (self, tuple):
        return signal.lfilter(self.b, self.a, tuple)


