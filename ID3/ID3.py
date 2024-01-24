import numpy as np
import graphviz
from collections import Counter

class Node:
    def __init__(self, data, target, parent_feature_value=None, parent=None):
        self.data = data
        self.target = target
        self.children = {}
        self.parent_feature_value = parent_feature_value
        self.parent = parent
        self.feature = None
        self.label = None

def entropy(target):
    count = Counter(target)
    total_samples = len(target)
    entropy_val = 0.0

    for label in count:
        prob = count[label] / total_samples
        entropy_val -= prob * np.log2(prob)

    return entropy_val

def information_gain(data, target, feature):
    unique_values = np.unique(data[:, feature])

    total_entropy = entropy(target)

    weighted_entropy = 0.0
    for value in unique_values:
        subset_indices = np.where(data[:, feature] == value)
        subset_target = target[subset_indices]
        subset_entropy = entropy(subset_target)
        weighted_entropy += (len(subset_target) / len(target)) * subset_entropy

    return total_entropy - weighted_entropy

def id3(data, target, features, parent_feature_value=None):
    if len(np.unique(target)) == 1:
        # If all examples have the same class, create a leaf node
        return Node(data, target, parent_feature_value=parent_feature_value)

    if len(features) == 0:
        # If there are no features left, create a leaf node with the majority class
        majority_class = Counter(target).most_common(1)[0][0]
        return Node(data, target, parent_feature_value=parent_feature_value, label=majority_class)

    best_feature = max(features, key=lambda feature: information_gain(data, target, feature))
    node = Node(data, target, parent_feature_value=parent_feature_value, parent=None)
    node.feature = best_feature

    unique_values = np.unique(data[:, best_feature])
    for value in unique_values:
        subset_indices = np.where(data[:, best_feature] == value)
        subset_data = data[subset_indices]
        subset_target = target[subset_indices]

        child = id3(subset_data, subset_target, [f for f in features if f != best_feature], parent_feature_value=value)
        node.children[value] = child

    return node


    
def predict(node, sample):
    if node.label is not None:
        return node.label

    if not node.children or sample[node.feature] not in node.children:
        # If the feature value is not in the training data or the node is a leaf, return a default value (e.g., majority class)
        return Counter(node.target).most_common(1)[0][0]

    child_node = node.children[sample[node.feature]]
    return predict(child_node, sample)

def visualize_tree(node, dot, parent_name=None, edge_label=None):
    if node.label is not None:
        dot.node(str(node.label), label=str(node.label))
    else:
        dot.node(str(node.feature), label=f"Feature {node.feature}")

        for value, child_node in node.children.items():
            if edge_label:
                dot.edge(str(node.feature), str(child_node.feature), label=edge_label)
            else:
                dot.edge(str(node.feature), str(child_node.feature), label=str(value))
            visualize_tree(child_node, dot, parent_name=str(node.feature), edge_label=str(value))


# Example usage:
data = np.array([[1, 'Sunny', 'Hot', 'High', False],
                 [2, 'Sunny', 'Hot', 'High', True],
                 [3, 'Overcast', 'Hot', 'High', False],
                 [4, 'Rain', 'Mild', 'High', False],
                 [5, 'Rain', 'Cool', 'Normal', False],
                 [6, 'Rain', 'Cool', 'Normal', True],
                 [7, 'Overcast', 'Cool', 'Normal', True],
                 [8, 'Sunny', 'Mild', 'High', False],
                 [9, 'Sunny', 'Cool', 'Normal', False],
                 [10, 'Rain', 'Mild', 'Normal', False],
                 [11, 'Sunny', 'Mild', 'Normal', True],
                 [12, 'Overcast', 'Mild', 'High', True],
                 [13, 'Overcast', 'Hot', 'Normal', False],
                 [14, 'Rain', 'Mild', 'High', True]])

target = np.array(['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'])

features = [1, 2, 3, 4]  # indices of features in the dataset

root = id3(data, target, features)
sample = [1, 'Sunny', 'Hot', 'Normal', False]
prediction = predict(root, sample)
print("Prediction:", prediction)
dot = graphviz.Digraph(comment='Decision Tree')

# Visualize the tree
visualize_tree(root, dot)

# Save the DOT representation to a file
dot.render('decision_tree', format='png', cleanup=True)

# Display the tree visualization
dot.view('decision_tree')
