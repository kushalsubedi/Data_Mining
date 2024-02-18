from typing import List, Tuple
import matplotlib.pyplot as plt 
import random

AGE = [22, 23, 25, 27, 28, 29, 30, 31, 33, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46]
WEIGHT = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 70, 71, 72, 73, 74, 75, 76, 77, 78]

CLUSTER = 2
CLUSTER1 = []
CLUSTER2 = []


def cluster_center(C: Tuple) -> Tuple:
    x, y = zip(*C)
    return sum(x) / len(x), sum(y) / len(y) 
       

def distance(x1, y1, C: Tuple) -> float:
    x2, y2 = C
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def check_center(X: List, Y: List, cluster_center1: Tuple, cluster_center2: Tuple):
    global CLUSTER1, CLUSTER2  # Using global keyword to modify global variables
    CLUSTER1 = []
    CLUSTER2 = []
    for i in range(len(X)):
        if distance(X[i], Y[i], cluster_center1) < distance(X[i], Y[i], cluster_center2):
            CLUSTER1.append((X[i], Y[i]))
        else:
            CLUSTER2.append((X[i], Y[i]))

    cluster_center1 = cluster_center(CLUSTER1)
    cluster_center2 = cluster_center(CLUSTER2)

    return cluster_center1, cluster_center2


def k_mean(AGE, WEIGHT, k):
    cluster_center1 = (AGE[0], WEIGHT[0])
    cluster_center2 = (AGE[1], WEIGHT[1])
    prev_cluster_center1 = None
    prev_cluster_center2 = None

    while (prev_cluster_center1 != cluster_center1) or (prev_cluster_center2 != cluster_center2):
        prev_cluster_center1 = cluster_center1
        prev_cluster_center2 = cluster_center2
        cluster_center1, cluster_center2 = check_center(AGE, WEIGHT, cluster_center1, cluster_center2)

    return cluster_center1, cluster_center2

if __name__ == "__main__":
    cluster_center1, cluster_center2 = k_mean(AGE, WEIGHT, CLUSTER)
    predict = (40, 60)
    if distance(predict[0], predict[1], cluster_center1) < distance(predict[0], predict[1], cluster_center2):
        print("Predicted cluster:", predict, "is in cluster 1")
    else:
        print("Predicted cluster:", predict, "is in cluster 2")
    cluster1_x, cluster1_y = zip(*CLUSTER1)
    cluster2_x, cluster2_y = zip(*CLUSTER2)
    print("Cluster Centers:", cluster_center1, cluster_center2)
    plt.scatter(cluster1_x, cluster1_y, color='blue', label='Cluster 1', alpha=0.5)
    plt.scatter(cluster2_x, cluster2_y, color='red', label='Cluster 2', alpha=0.5)
    plt.scatter(*cluster_center1, color='blue', marker='x', s=200, label='Cluster 1 Center')
    plt.scatter(*cluster_center2, color='red', marker='x', s=200, label='Cluster 2 Center')
    plt.title('K-Mean')
    plt.xlabel('AGE')
    plt.ylabel('WEIGHT')
    plt.legend()
    plt.show()
