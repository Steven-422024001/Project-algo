class Graphs:
    def kruskal_algorithm(self, n, edges):
        """
        Kruskal's Algorithm: Membuat MST (Minimum Spanning Tree) dari graf.
        """
        edges.sort(key=lambda x: x[2])
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        mst = []
        for u, v, weight in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))
        return mst

    def dijkstra_algorithm(self, graph, start):
        """
        Dijkstra's Algorithm: Mencari jarak terpendek dari satu simpul ke simpul lainnya.
        """
        import heapq
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return distances

    def bellman_ford_algorithm(self, n, edges, start):
        """
        Bellman-Ford Algorithm: Mencari jarak terpendek, mendukung bobot negatif.
        """
        distances = [float('inf')] * n
        distances[start] = 0
        for _ in range(n - 1):
            for u, v, weight in edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
        return distances

    def floyd_warshall_algorithm(self, graph):
        """
        Floyd-Warshall Algorithm: Semua pasangan jarak terpendek.
        """
        n = len(graph)
        dist = [[float('inf')] * n for _ in range(n)]
        for u in range(n):
            dist[u][u] = 0
        for u, neighbors in enumerate(graph):
            for v, weight in neighbors.items():
                dist[u][v] = weight
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

    def topological_sort(self, n, edges):
        """
        Topological Sort: Urutan linier simpul graf berarah.
        """
        from collections import defaultdict, deque
        indegree = [0] * n
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        queue = deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return topo_order

    def flood_fill(self, image, sr, sc, new_color):
        """
        Flood Fill: Mengubah warna area terhubung.
        """
        original_color = image[sr][sc]
        if original_color == new_color:
            return image

        def dfs(x, y):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != original_color:
                return
            image[x][y] = new_color
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy)

        dfs(sr, sc)
        return image

    def lee_algorithm(self, grid, start, end):
        """
        Lee Algorithm: BFS untuk menemukan jarak terpendek dalam grid.
        """
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        queue = deque([(*start, 0)])
        visited = set()
        visited.add(start)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            x, y, dist = queue.popleft()
            if (x, y) == end:
                return dist
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))
        return -1
