from collections import deque

def bfs_graph(vertices, adj):
    bfs = []
    visited = set()
    que = deque()
    que.append(0)
    visited.add(0)
    while que:
        node = que.popleft()
        bfs.append(node)
        for child in adj[node]:
            if child not in visited:
                que.append(child)
                visited.add(child)
    return bfs

print('-----------------------------------------------------------')
print('\tWelcome to Breadth First Search for a graph')
print('-----------------------------------------------------------\n')
t = int(input("Enter the number of testcases: "))
for _ in range(t):
    print('\n*************** Testcase', _+1, '***************\n')
    vertices, edges = map(int, input("Enter number of vertices & edges: ").split())
    adj = [[] for vertex in range(vertices)]
    for edge in range(edges):
        start, end = map(int, input("Enter edge: ").split())
        adj[start].append(end)
    path = bfs_graph(vertices, adj)
    print("\nBFS Traversal:")
    for node in path:
        print(node, end =' ')
    print()
