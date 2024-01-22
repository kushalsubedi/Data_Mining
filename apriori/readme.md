# Apriori algorithm 
Apriori algorithm is one of the common and popular algorithm for market basket analysis or association rule mining. It is used to find the frequent itemsets in the given dataset. It is based on the concept that a subset of a frequent itemset must also be a frequent itemset.

## How it works?
Apriori algorithm works on the principle of level-wise search. It begins with an itemset of size 1 (also called as candidate itemset) which is frequent in the given dataset. It then expands the candidate itemset by adding one more item to it and checks if the resulting itemset is frequent. The algorithm terminates when no further itemset can be added to the candidate itemset.

## Steps
1. Find the frequent itemsets in the given dataset.
2. Generate the candidate itemsets.
3. Prune the candidate itemsets which are infrequent.
4. Repeat steps 2 and 3 until no further candidate itemsets can be generated.

## Example
Consider the following dataset:

| Transaction | Items |
| ----------- | ----- |
|1|['Milk', 'Onion', 'Kidney Beans', 'Eggs', 'Yogurt']|
|2|    ['Dill', 'Onion', 'Eggs', 'Yogurt'],|
 |2|   ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],|
 |3|   ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],|
 |4|   ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs'],|
 |5|   ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],|
 |6|   ['Eggs', 'Apple', 'Kidney Beans', 'Milk'],|
 |7|   ['Corn', 'Apple', 'Kidney Beans'],|
 |8|   ['Nut', 'Apple', 'Kidney Beans'],|
 |9|   ['Nut', 'Ice cream', 'Kidney Beans'],|
 |10|   ['Ice cream', 'Apple', 'Kidney Beans'],|
 |11|   ['Onion', 'Apple', 'Kidney Beans'],|
 |12|   ['Yoghurt', 'Corn', 'Kidney Beans'],|
 |13|   ['Ice Cream', 'Bread', 'Kidney Beans']|


### Step 1: Find the frequent itemsets in the given dataset.
The minimum support is 3. So, the frequent itemsets are:

| Itemset | Support |
| ------- | ------- |
--- you know what to do 