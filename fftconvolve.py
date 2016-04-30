from streamsx.topology.topology import Topology
import streamsx.topology.context
from sources import signal_generator
from standard.TumblingWindow import TumblingWindow
from timeseries import signal_functions
from scipy import signal

def main():
    ref_signal = signal.hann(10)

    t = Topology("FFTConvolve_Sample")
    readings = t.source(signal_generator.Readings(10000)).transform(TumblingWindow(1000))
    convolveStream = readings.transform(signal_functions.FFTConvolve(ref_signal))
    convolveStream.sink(print)

    streamsx.topology.context.submit("STANDALONE", t.graph)


if __name__ == '__main__':
    main()
