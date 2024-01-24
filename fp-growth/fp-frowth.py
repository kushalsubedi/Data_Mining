DATA = [ 
    ['I1','I2','I5'],
    ['I1','I3','I4'],
    ['I2','I3','I4'],
    ['I1','I2','I3','I4'],
    ['I1','I2','I3'],
    ['I5','I1'],
    ['I4','I3','I2'],
    ['I2','I5'],
    ['I2','I3','I5'],
    ['I1','I2','I3']
    ]



class TreeNode :
    def __init__(self,item,count,parent):
        self.item = item
        self.count = count
        self.parent = parent
        self.children = {}
        self.nodeLink = None

def create_tree(dataset, min_support):
    header_table = {}
    for transaction, count in dataset.items():
        for item in transaction:
            header_table[item] = header_table.get(item, [0, None])
            header_table[item][0] += count

    frequent_items = {k: v for k, v in header_table.items() if v[0] >= min_support}
    if not frequent_items:
        return None, None

    root = TreeNode(None, 0, None)

    for transaction, count in dataset.items():
        transaction_sorted = [item for item in transaction if item in frequent_items]
        transaction_sorted.sort(key=lambda x: frequent_items[x][0], reverse=True)
        insert_tree(transaction_sorted, count, root, frequent_items)

    return root, header_table



def insert_tree(items, count, node, frequent_items):
    if not items:
        return
    first_item = items[0]
    if first_item in node.children:
        child = node.children[first_item]
        child.count += count
    else:
        child = TreeNode(first_item, count, node)
        node.children[first_item] = child
        if frequent_items[first_item][1] is None:
            frequent_items[first_item][1] = child
        else:
            update_header(frequent_items[first_item][1], child)
    insert_tree(items[1:], count, child, frequent_items)

def update_header(node_to_test,target_node):
    while(node_to_test.nodeLink != None):
        node_to_test = node_to_test.nodeLink
    node_to_test.nodeLink = target_node

def mine_frequent_itemsets(tree,header_table,min_support,current_itemset,frequent_itemsets):

    for item,count in header_table.items():
        current_itemset.append(item)
        frequent_itemsets.append(current_itemset[:])
        conditional_pattern_base = get_conditional_pattern_bases(item,header_table)
        conditional_tree,conditional_header = create_tree(conditional_pattern_base,min_support)
        if conditional_header != None:
            mine_frequent_itemsets(conditional_tree,conditional_header,min_support,current_itemset,frequent_itemsets)
        current_itemset.pop()

def get_conditional_pattern_bases(item, header_table):
    conditional_pattern_bases = {}
    node = header_table[item]

    while node is not None:
        prefix_path =get_prefix_path(node)
        if len(prefix_path) > 1:
            conditional_pattern_bases[frozenset(prefix_path[1:])] = node.count
        node = node.node_link

    return conditional_pattern_bases


def get_prefix_path(node):
    path = []
    while node is not None:
        if isinstance(node, TreeNode):  # Check if it's a TreeNode
            path.append(node.item)
            node = node.parent
        else:  # If it's a list, take the second element (parent)
            path.append(node[0])
            node = node[1]
    path.reverse()
    return path


def load_data(DATA):
    data = []
    for transactions in DATA:
        data.append(transactions)
    return data 

def create_dataset(data):
    dataset = {}
    for transactions in data:
        dataset[frozenset(transactions)] = dataset.get(frozenset(transactions),0) + 1
    return dataset 

def main():
    data = load_data(DATA)
    dataset = create_dataset(data)
    min_support = 2
    root,header_table = create_tree(dataset,min_support)
    frequent_itemsets = []
    mine_frequent_itemsets(root,header_table,min_support,[],frequent_itemsets)
    print(frequent_itemsets)

if __name__ == '__main__':
    main()
