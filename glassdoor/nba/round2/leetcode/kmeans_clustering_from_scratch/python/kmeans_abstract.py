from abc import ABC, abstractmethod

class KMeansAbstract(ABC):
    def __init__(self, k=3, max_iterations=100):
        pass

    @abstractmethod
    def fit(self, X):
        pass
    
    @abstractmethod
    def _assign_labels(self):
        pass

    @abstractmethod
    def _update_centroids(self, labels):
        pass
    
    @abstractmethod
    def predict(self, X):
        pass
