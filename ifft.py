from streamsx.topology.topology import Topology
import streamsx.topology.context
from sources import signal_generator
from scipy import fftpack
from standard.TumblingWindow import TumblingWindow

def main():
    t = Topology("IFFT_Sample")
    readings = t.source(signal_generator.Readings(50)).transform(TumblingWindow(10))
    fftStream = readings.transform(fftpack.fft)
    ifftStream = fftStream.transform(fftpack.ifft)
    ifftStream.sink(print)

    streamsx.topology.context.submit("STANDALONE", t.graph)


if __name__ == '__main__':
    main()
