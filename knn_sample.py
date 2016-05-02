from streamsx.topology.topology import Topology
import streamsx.topology.context
from knn import knn_sources
from knn.knn_model import KNNClassifier

def main():
    """
    The 'KNN' model accepts a tuple with these elements: (type, X, y), where:
     'type' can be: 'train', 'data', or an empty string (same as 'data')
     'X' is the data
     'y' is the actual class of the data (only used to train the model)
    """
    training_size = 100

    t = Topology("KNN_Sample")
    trainingStream = t.source(knn_sources.KNNTrainingData(training_size))
    dataStream = t.source(knn_sources.KNNTestData(20, 5))
    combinedStreams = trainingStream.union({dataStream})
    predictionStream = combinedStreams.transform(KNNClassifier(training_size))
    predictionStream.sink(print)


    streamsx.topology.context.submit("STANDALONE", t.graph)


if __name__ == '__main__':
    main()
