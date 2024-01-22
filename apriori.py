import itertools

from typing import Dict, List, Set, Tuple
from collections import defaultdict

DATA = [
        ['Milk', 'Onion', 'Kidney Beans', 'Eggs', 'Yogurt'],
        ['Dill', 'Onion', 'Eggs', 'Yogurt'],
        ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
        ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
        ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs'],
        ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
        ['Eggs', 'Apple', 'Kidney Beans', 'Milk'],
        ['Corn','Apple', 'Kidney Beans'],
        ['Nut', 'Apple', 'Kidney Beans'],
        ['Nut', 'Ice cream', 'Kidney Beans'],
        ['Ice cream', 'Apple', 'Kidney Beans'],
        ['Onion','Apple', 'Kidney Beans'],
        ['Yoghurt','Corn', 'Kidney Beans'],
        ['Ice Cream','Bread','Kidney Beans']
        ]
CONFIDENCE = 0.8 
MIN_SUPPORT_COUNT = 3

def get_item(Data:List[List])->Dict[str, int]:
    item_map = {}
    item_map2 = {}
    for transaction in Data:
        for item in transaction:
            if item in item_map:
                item_map[item] += 1
            else:
                item_map[item] = 1
    for item, count in item_map.items():
        if int(count) >=  MIN_SUPPORT_COUNT:
            item_map2[item] = count 
    return item_map2

#print(get_item(DATA))

def frequent_itemset (get_item:Dict[str, int],data:List[List])->Dict[Tuple[str], int]:
    frequent_itemset = []
    for i in range(2, 3):
        frequent_itemset.extend(set(itertools.combinations(get_item.keys(), i)))
   
    #print(frequent_itemset )
    occurrence = {} 
    for itemset in frequent_itemset:
        support_count = sum(1 for transaction in DATA if set(itemset).issubset(transaction))
        if support_count >= MIN_SUPPORT_COUNT:
            occurrence[itemset] = support_count
    return occurrence



for itemset, support_count in frequent_itemset(get_item(DATA), DATA).items():
    print(f"{itemset} = {support_count}")
 
  
def apriori():
    pass
