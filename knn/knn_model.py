from sklearn.neighbors import KNeighborsClassifier

class KNNClassifier:
    def __init__ (self, training_size):
        self.training_size = training_size
        self.X_train = []
        self.y_train = []
        self.isTraining = True
        self.estimator = KNeighborsClassifier()
    def __call__ (self, tuple):
        if(tuple[0] == 't'): ## training tuple
            print(tuple)
            if self.isTraining:
                self.X_train.append(tuple[1])
                self.y_train.append(tuple[2])
                if len(self.X_train) == self.training_size:
                    ## all training data received, train classifier 
                    ## and begin analyzing data
                    self.estimator.fit(self.X_train, self.y_train)
                    self.isTraining = False                    
        elif tuple[0] == 'd' or tuple[0] == '': ## data tuple
            if not self.isTraining:
                return (tuple[1], self.estimator.predict(tuple[1].reshape(1,-1))[0])
                
                
