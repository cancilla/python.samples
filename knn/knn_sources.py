from sklearn.datasets.samples_generator import make_blobs
import time

class KNNTrainingData:
    def __init__(self, training_size):
        self.X, self.y = make_blobs(n_samples=training_size, centers=3, n_features=2, random_state=13)
    def __call__(self):
        for x, y_actual in zip(self.X, self.y):
            yield ('t', x, y_actual)

class KNNTestData:
    def __init__(self, iterations=-1, initDelay=0):
        self.iterations = iterations
        self.initDelay = initDelay
        self.num_samples = 10000
        self.testData = []
    def _createTestData(self):
        X,y = make_blobs(n_samples=self.num_samples, centers=3, n_features=2)
        for x in X:
            self.testData.append(('d',x))
    def __call__(self):
        if self.initDelay > 0:
            time.sleep(self.initDelay)
        count = 0
        while True:
            ## handle iterations
            if self.iterations > -1:
                if count < self.iterations:
                    count += 1
                else:
                    break;
                
            ## return data
            if len(self.testData) == 0:
                self._createTestData();

            yield self.testData.pop()
        
