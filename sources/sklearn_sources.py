from sklearn.datasets.samples_generator import make_blobs
import time

class Src:
    def __init__(self, isTraining, iterations=-1, initDelay=0):
        self.isTraining = isTraining
        self.iterations = iterations
        self.initDelay = initDelay
        self.data = []
    def createData(self):
        """
        Default implementation assumes the generator will return X,y values. Subclass should 
        override if this is not the case.
        """
        X,y = self.generateData()
        for x,y_actual in zip(X,y):
            if self.isTraining:
                self.data.append(('t', x, y_actual))
            else:
                self.data.append(('d', x))
    def getData(self):
        """ Default implementation. May need to be overriden for different types of generators."""
        if len(self.data) == 0:
            self.createData()
        return self.data.pop()
    def generateData(self):
        raise NotImplementedError("Subclass must implement this function")
    def __call__(self):
        ## initial delay
        if self.initDelay > 0:
            time.sleep(self.initDelay)
        count = 0 
        while True:
            ## iterations
            if self.iterations > -1: 
                if count < self.iterations:
                    count += 1
                else:
                    break;

            ## return data 
            yield self.getData()

class Blobs(Src):
    def __init__(self, centers, n_features, random_state=0, isTraining=False, iterations=-1, initDelay=0):
        super(Blobs, self).__init__(isTraining, iterations, initDelay)
        self.n_samples = iterations if iterations >= 0 else 1000
        self.centers = centers
        self.n_features = n_features
        self.random_state = random_state
    def generateData(self):
        return make_blobs(n_samples=self.n_samples, centers=self.centers, n_features=self.n_features, random_state=self.random_state)


