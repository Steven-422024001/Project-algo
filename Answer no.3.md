# Algorithm Complexity Analysis

# 1. **Euclid's Algorithm (Basic Algorithm)**
**Description**:  
Algorithm to find the **greatest common divisor (GCD)** of two integers. This is useful in problems involving divisibility or simplification of fractions.

**Time Complexity**:  
- **Best Case**: \(O(1)\) – The algorithm may find the GCD immediately if the numbers are the same.  
- **Worst Case**: \(O(\log n)\) – The time grows logarithmically with the size of the numbers.  
- **Average Case**: \(O(\log n)\) – In most cases, the time complexity behaves logarithmically.
**Space Complexity**:  
\(O(1)\) – The algorithm only requires a small, constant amount of memory.



## 2. **Insertion Sort (Sorting Algorithm)**
**Description**:  
This sorting algorithm works by repeatedly inserting each element into its correct position relative to the already sorted portion of the array.

**Time Complexity**:  
- **Best Case**: \(O(n)\) – If the array is already sorted, only a simple check is needed for each element.  
- **Worst Case**: \(O(n^2)\) – In the case where the array is in reverse order, many comparisons and shifts are required.  
- **Average Case**: \(O(n^2)\) – Typically, the algorithm has quadratic time complexity when elements are not sorted.
**Space Complexity**:  
\(O(1)\) – Insertion sort is an **in-place** sorting algorithm, requiring no extra space beyond the input array.



## 3. **Kadane's Algorithm (Array Algorithm)**
**Description**:  
Kadane's Algorithm is used to find the **maximum sum** of a contiguous subarray within a given array, making it useful for problems like finding the maximum profit in a sequence of stock prices.

**Time Complexity**:  
- **Best Case**: \(O(n)\) – The algorithm needs to check each element at least once.  
- **Worst Case**: \(O(n)\) – No matter the array's structure, the algorithm performs a single pass.  
- **Average Case**: \(O(n)\) – The algorithm still takes linear time on average.
**Space Complexity**:  
\(O(1)\) – The algorithm only uses a constant amount of space, making it very memory efficient.



## 4. **Dijkstra's Algorithm (Graph Algorithm)**
**Description**:  
Dijkstra's Algorithm is used to find the **shortest path** from a source node to all other nodes in a graph. This is typically used in routing applications, such as GPS systems.

**Time Complexity**:  
- **Best Case**: \(O(E + V \log V)\) – In sparse graphs (few edges), the time complexity may be closer to this value.  
- **Worst Case**: \(O(E + V \log V)\) – In the worst case, when the graph is dense, the time complexity remains the same.  
- **Average Case**: \(O(E + V \log V)\) – Typically, this complexity holds for graphs with a reasonably distributed number of edges.
**Space Complexity**:  
\(O(V + E)\) – The algorithm requires space for storing all the graph's vertices \(V\) and edges \(E\).