from streamsx.topology.topology import Topology
import streamsx.topology.context
from sources import signal_generator
from standard.TumblingWindow import TumblingWindow
from scipy import fftpack

def main():
    t = Topology("FFT_Sample")
    readings = t.source(signal_generator.Readings(50)).transform(TumblingWindow(10))
    fftStream = readings.transform(fftpack.fft)
    fftStream.sink(print)

    streamsx.topology.context.submit("STANDALONE", t.graph)


if __name__ == '__main__':
    main()
