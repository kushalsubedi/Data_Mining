import itertools
from typing import Dict, List, Set, Tuple
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

DATA = [
    ['Milk', 'Onion', 'Kidney Beans', 'Eggs', 'Yogurt'],
    ['Dill', 'Onion', 'Eggs', 'Yogurt'],
    ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
    ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
    ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs'],
    ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
    ['Eggs', 'Apple', 'Kidney Beans', 'Milk'],
    ['Corn', 'Apple', 'Kidney Beans'],
    ['Nut', 'Apple', 'Kidney Beans'],
    ['Nut', 'Ice cream', 'Kidney Beans'],
    ['Ice cream', 'Apple', 'Kidney Beans'],
    ['Onion', 'Apple', 'Kidney Beans'],
    ['Yoghurt', 'Corn', 'Kidney Beans'],
    ['Ice Cream', 'Bread', 'Kidney Beans']
]
CONFIDENCE = 0.8
MIN_SUPPORT_COUNT = 3


def get_item(Data: List[List]) -> Dict[str, int]:
    item_map = {}
    item_map2 = {}
    for transaction in Data:
        for item in transaction:
            if item in item_map:
                item_map[item] += 1
            else:
                item_map[item] = 1
    for item, count in item_map.items():
        if int(count) >= MIN_SUPPORT_COUNT:
            item_map2[item] = count
    return item_map2


def generate_candidates(prev_candidates: List[Tuple[str]], k: int) -> List[Tuple[str]]:
    candidates = []
    for i in range(len(prev_candidates)):
        for j in range(i + 1, len(prev_candidates)):
            if prev_candidates[i][:k - 2] == prev_candidates[j][:k - 2]:
                new_candidate = tuple(sorted(set(prev_candidates[i] + prev_candidates[j])))
                candidates.append(new_candidate)
    return candidates


def frequent_itemset(get_item: Dict[str, int], data: List[List], set_size) -> Dict[Tuple[str], int]:
    frequent_itemsets = {}
    candidates = [tuple([item]) for item in get_item.keys()]

    for size in range(2, set_size + 1):
        candidates = generate_candidates(candidates, size)

        # Count support for each candidate
        for transaction in data:
            for candidate in candidates:
                if set(candidate).issubset(transaction):
                    if candidate in frequent_itemsets:
                        frequent_itemsets[candidate] += 1
                    else:
                        frequent_itemsets[candidate] = 1

        candidates = [candidate for candidate in candidates if frequent_itemsets.get(candidate, 0) >= MIN_SUPPORT_COUNT]

    return frequent_itemsets


def generate_rules(frequent_itemsets: Dict[Tuple[str], int], confidence_threshold: float):
    rules = []
    for itemset, support_count in frequent_itemsets.items():
        if len(itemset) > 1:
            for i in range(1, len(itemset)):
                antecedent = itemset[:i]
                consequent = itemset[i:]
                antecedent_support = frequent_itemsets.get(antecedent, 0)
                if antecedent_support == 0:
                    continue
                confidence = support_count / antecedent_support
                if confidence >= confidence_threshold:
                    rules.append((antecedent, consequent, confidence))
    return rules



def plot_association_heatmap(rules):
    antecedents = [', '.join(rule[0]) for rule in rules]
    consequents = [', '.join(rule[1]) for rule in rules]
    confidences = [rule[2] for rule in rules]

    data = pd.DataFrame({'Antecedent': antecedents, 'Consequent': consequents, 'Confidence': confidences})
    pivot_table = data.pivot_table(index='Antecedent', columns='Consequent', values='Confidence', aggfunc='mean', fill_value=0)

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', cbar_kws={'label': 'Confidence'})
    plt.title('Association Rules Heatmap')
    plt.show()

def apriori():
    print("Apriori Algorithm")
    item_map = get_item(DATA)
    print("1-itemsets:", item_map)
    frequent_itemsets_result = frequent_itemset(item_map, DATA, set_size=len(item_map))
    print("Frequent Itemsets:", frequent_itemsets_result)

    rules = generate_rules(frequent_itemsets_result, confidence_threshold=CONFIDENCE)
    print("\nAssociation Rules:")
    for rule in rules:
        antecedent_str = ', '.join(rule[0])
        consequent_str = ', '.join(rule[1])
        print(f"{antecedent_str} => {consequent_str} (Confidence: {rule[2]:.2f})")

    plot_association_heatmap(rules)

if __name__ == "__main__":
    apriori()
