from scipy import signal

class Convolve:
    def __init__ (self, ref_signal, mode='full'):
        self.ref_signal = ref_signal
        self.mode = mode
    def __call__ (self, tuple):
        return signal.convolve(tuple, self.ref_signal, self.mode)

class Correlate:
    def __init__ (self, ref_signal, mode='full'):
        self.ref_signal = ref_signal
        self.mode = mode
    def __call__ (self, tuple):
        return signal.correlate(tuple, self.ref_signal, self.mode)

class FFTConvolve:
    def __init__ (self, ref_signal, mode='full'):
        self.ref_signal = ref_signal
        self.mode = mode
    def __call__ (self, tuple):
        return signal.fftconvolve(tuple, self.ref_signal, self.mode)

