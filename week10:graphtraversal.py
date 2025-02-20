# Graph Traversals: Given a graph, traverse it in BFS and DFS orders.

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            queue.extend(graph[node])

    return traversal

def dfs(graph, start, visited=None, traversal=None):
    if visited is None:
        visited = set()
        traversal = []

    visited.add(start)
    traversal.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal)

    return traversal

def main():
    graph = {}
    num_edges = int(input("Enter number of edges: "))

    print("Enter edges (format: u v, representing an edge between u and v):")
    for _ in range(num_edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    start = input("Enter starting node: ")

    print("BFS Traversal:", bfs(graph, start))
    print("DFS Traversal:", dfs(graph, start))

if __name__ == "__main__":
    main()
