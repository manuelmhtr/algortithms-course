# Algorithms Specialization

My assignments for the Stanford [Algorithms Specialization](https://www.coursera.org/specializations/algorithms).

### 01 Karatsuba Multiplication

Multiplies two integers using the Karatsuba Multiplication algorithm.

```sh
$ python3 ./karatsuba/solution.py <integer 1> <integer 2>
```

### 02 Inversions count

Given an arrays of integer, counts the number of inversions there are in the list. An inversion occurs when an integer is placed outside the ascending order in the list. For example the array `[1, 2, 3]` has not inversions but `[1, 3, 5, 2, 4, 6]` has 3: `(3, 2)`, `(5, 2)` and `(5, 4)`.

```sh
$ python3 ./inversions-count/solution.py
# It will use the file sample-input.txt as input
```

### 03 Quick sort

Given an arrays of integer, counts the number of comparisons the algorithm has to do in order to sort the list. It uses 3 strategies to select the pivot in the quick sort splitting routine:

* Using the first element
* Using the last element
* Using the median element among the first, last and the middle elements

```sh
$ python3 ./quick-sort/solution.py
# It will use the file sample-input.txt as input
```

### 04 Min Cuts

Given a undirected graph, counts them minimum number of cuts using the Kramer's algorithm.

```sh
$ python3 ./min-cuts/solution.py
# It will use the file sample-input.txt as input
```

### 05 Strongly Connected Components

Given a directed graph, find all the [strongly connected components](https://www.geeksforgeeks.org/strongly-connected-components/) and print the largest 5 of them.

```sh
$ python3 ./strongly-connected-components/solution.py
# It will use the file sample-input.txt as input
```

### 06 Dijkstra's Shortest Path

Calculates the shortest distances from a source node to all other nodes in a graph using the (Dijkstra's algorithm)[https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm].

```sh
$ python3 ./dijkstras-shortest-path/solution.py
# It will use the file input.txt as input
```

### 07 Medians using heaps

Calculates the sum of medians in a numbers list, using the Heap data structure.

```sh
$ python3 ./median-heaps/solution.py
# It will use the file input.txt as input
```

### 08 2-Sum problem

Given a range `T` and a set `U` of integers, counts how many values in `T` can be calculated with the sum of 2 different integers `x` and `y` present in the set `U`.

```sh
$ python3 ./two-sum/solution.py
# It will use the file input.txt as input
```

### 09 Greedy algorithms

Given a list of jobs to be processed, each one with a weight and length defined. Prioritize the jobs using 2 different greedy algorithms and report their respective total completion times.

```sh
$ python3 ./greedy-algorithms/solution.py
# It will use the file input.txt as input
```

### 10 Prim's Minimum Spanning Tree

Given an undirected graph with a cost assigned on each edge. Calculates the total cost of the minimum spanning tree (MST) using Prim's algorithm.

```sh
$ python3 ./prims-min-spanning-tree/solution.py
# It will use the file input.txt as input
```

### 11 Max Spacing K-Clustering

Find the max spacing distance after grouping a list of nodes in `k` clusters using Kruskal's algorithm.

```sh
$ python3 ./k-clustering/max-spacing/solution.py
# It will use the file max-spacing/input.txt as input
```

### 12 Largest K in K-Clustering

Find the largest number of K clusters required to group a list of nodes with a spacing of at least 3. Nodes are represented using a 24 bits label and the distance between them is calculated using the _Hamming distance_.

```sh
$ python3 ./k-clustering/max-k/solution.py
# It will use the file max-k/input.txt as input
```

### 13 Huffman Coding

Given an alphabet of symbols and their frequencies, encode them using the Huffman coding algorithm and determine the minimum and the maximum lengths of the codewords.

```sh
$ python3 ./huffman-coding/solution.py
# It will use the file input.txt as input
```

### 14 Maximum-Weight independent Set of a Path Graph

Give a list of nodes that form a path graph, find the set of independent nodes (ie. they are not adjacent) that sum the maximum possible weight.

```sh
$ python3 ./max-weight-set-in-path-graph/solution.py
# It will use the file input.txt as input
```
