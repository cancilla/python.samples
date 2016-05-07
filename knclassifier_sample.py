from streamsx.topology.topology import Topology
import streamsx.topology.context
from sources import sklearn_sources
from estimator.estimator_model import Estimator
from sklearn.neighbors import KNeighborsClassifier

def main():
    """
    The 'Estimator' model accepts a tuple with these elements: (type, X, y), where:
       'type':  't' (for training), 'd' (for data), '' (empty string, same as 'd')
       'X':     is the data
       'y':     is the actual class of the data (only used to train the model)
    """
    training_size = 100
    num_centers = 2
    num_features = 2

    t = Topology("Estimator_Sample")
    trainingStream = t.source(sklearn_sources.Blobs(iterations=training_size, isTraining=True, centers=num_centers, n_features=num_features))
    dataStream = t.source(sklearn_sources.Blobs(centers=num_centers, n_features=num_features))
    combinedStreams = trainingStream.union({dataStream})
    predictionStream = combinedStreams.transform(Estimator(training_size, KNeighborsClassifier()))
    predictionStream.sink(print)

    streamsx.topology.context.submit("STANDALONE", t.graph)


if __name__ == '__main__':
    main()
