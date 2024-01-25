#importing Libraries 
import numpy as np 
import math
from numpy import random
class DBSCAN:
    def __init__(self, eps=0.5, min_samples=5):
        """
        Parameters 
        ----------
        eps: float 
            The radius of a neighborhood
        min_samples: int
            The minimum number of samples in a neighborhood for a point to be considered as a core point

        Attributes
        ----------
        cluster_id: int
            The id of the current cluster 
        visited: set
            A set of visited points
        cluster: dict 
            A dictionary of clusters with cluster_id as key and list of points as values 
        
        noise: set 
            A set of noise points
        data: ndarray
            The dataset 
        distance_matrix: ndarray 
            The distance matrix of the dataset 
        """
        self.eps = eps
        self.min_samples = min_samples
        self.cluster_id = 0
        self.visited = set()
        self.cluster = {} 
        self.noise = set() 
        self.data = None 
        self.distance_matrix = None
    
    def fit(self,data):
        """
        Parameters
        ----------
        data: ndarray
            The dataset to be clustered
        """
        self.data = data 
        self.distance_matrix = self.get_distance_matrix(data)
        for i in range(len(data)):
            if i not in self.visited:
                self.visited.add(i)
                neighbors = self.get_neighbors(i)
                if len(neighbors) < self.min_samples:
                    self.noise.add(i)
                else:
                    self.cluster_id += 1
                    self.cluster[self.cluster_id] = []
                    self.expand_cluster(i, neighbors)
        return self.cluster, self.noise

    def get_distance_matrix(self, data):
        """
        Parameters
        ----------
        data: ndarray
            The dataset to be clustered
        """
        distance_matrix = np.zeros((len(data), len(data)))
        for i in range(len(data)):
            for j in range(len(data)):
                distance_matrix[i][j] = np.linalg.norm(data[i]-data[j])
        return distance_matrix

    def get_neighbors(self, point_id):

        """
        Parameters
        ----------
        point_id: int
            The id of the point whose neighbors are to be found
        """
        neighbors = []
        for i in range(len(self.data)):
            if self.distance_matrix[point_id][i] <= self.eps:
                neighbors.append(i)
        return neighbors 

    def expand_cluster(self, point_id, neighbors):
        """
        Parameters
        ----------
        point_id: int
            The id of the point whose neighbors are to be found
        neighbors: list
            The list of neighbors of the point
        """
        self.cluster[self.cluster_id].append(point_id)
        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                new_neighbors = self.get_neighbors(neighbor)
                if len(new_neighbors) >= self.min_samples:
                    neighbors.extend(new_neighbors)
            if neighbor not in self.cluster[self.cluster_id]:
                self.cluster[self.cluster_id].append(neighbor)
        return self.cluster 

if __name__ == "__main__":
    DATAS = random.rand(100,2)
    DATAS = np.array(DATAS)
    dbscan = DBSCAN()
    cluster, noise = dbscan.fit(DATAS)
    print(noise)


    

