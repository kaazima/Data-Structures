# Function that checks if a path exists between 2 given nodes of an undirected graph
def validPath(vertices, adj, start, end):
    visited = set()
    return dfs(start, end, visited, adj)
    
# Recursive dfs function
def dfs(start, end, visited, adj):
    visited.add(start)
    if start==end:
        return True
    for neighbour in adj[start]:
        if neighbour not in visited:
            if dfs(neighbour, end, visited, adj)==True:
                return True
    return False

print('---------------------------------------------------------------------')
print('\tCheck if a path exists in an undirected graph')
print('---------------------------------------------------------------------\n')
t = int(input("Enter the number of testcases: "))
for _ in range(t):
    print('\n*************** Testcase', _+1, '***************\n')
    vertices, edges = map(int, input("Enter number of vertices & edges: ").split())
    adj = [[] for vertex in range(vertices)]
    # Create an adjacency list
    for edge in range(edges):
        start, end = map(int, input("Enter edge: ").split())
        adj[start].append(end)
        adj[end].append(start) # This line should be removed for directed graph
    start, end = map(int, input("Enter start node & end node: ").split())
    if validPath(vertices, adj, start, end) == True:
        print('Path exists between',start,'&',end);
    else:
        print('Path does not exist between',start,'&',end)