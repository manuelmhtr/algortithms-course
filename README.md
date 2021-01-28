# Algorithms Specialization

My assignments for the Stanford [Algorithms Specialization](https://www.coursera.org/specializations/algorithms).

### 01 Karatsuba Multiplication

Multiplies two integers using the Karatsuba Multiplication algorithm.

```sh
$ python3 ./karatsuba.py <integer 1> <integer 2>
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
