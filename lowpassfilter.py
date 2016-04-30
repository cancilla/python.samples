from streamsx.topology.topology import Topology
import streamsx.topology.context
from sources import signal_generator
from timeseries.filters import butterworth
from standard.TumblingWindow import TumblingWindow

def main():
    filter_order = 4
    cutoffFreq = 100
    sampleRate = 1000

    t = Topology("LowpassFilter_Sample")
    readings = t.source(signal_generator.Readings(50000)).transform(TumblingWindow(2000))
    filterStream = readings.transform(butterworth.Lowpass(filter_order, cutoffFreq, sampleRate))
    filterStream.sink(print)

    streamsx.topology.context.submit("STANDALONE", t.graph)


if __name__ == '__main__':
    main()
