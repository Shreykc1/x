from collections import defaultdict

def multiply(matrix, vector):
    result = [0 for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(vector)):
            result[i] += matrix[i][j] * vector[j]
            result[i] = round(result[i], 2)
    return result

def adjacency_matrix(graph):
    n = len(graph)
    nodes = list(graph.keys())
    positions = { node: index for index, node in enumerate(nodes) }
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for source, destinations in graph.items():
        for destination in destinations:
            matrix[positions[destination]][positions[source]] = 1
    return matrix

def chance_matrix(graph):
    n = len(graph)
    matrix = [[1/n for _ in range(n)] for _ in range(n)]
    return matrix

def pagerank(graph, beta=0.8):
    n = len(graph)
    matrix = adjacency_matrix(graph)
    chances = chance_matrix(graph)
    nodes = list(graph.keys())
    positions = { index: node for index, node in enumerate(nodes) }

    for col in range(n):
        sum = 0
        for row in range(n): sum += matrix[row][col]
        if sum == 0: continue
        for row in range(n):
            matrix[row][col] /= sum

    for row in range(n):
        for col in range(n):
            matrix[row][col] *= beta
            matrix[row][col] += ((1 - beta) * chances[row][col])

    ranks = [0 for _ in range(n)]
    ranks[0] = 1
    while True:
        prev = ranks.copy()
        ranks = multiply(matrix, ranks)
        same = False
        for node in range(n):
            if ranks[node] != prev[node]: same = False
            else: same = True
        if same: break

    for i in range(n): print(f"{positions[i]}: {ranks[i]}")

def add(graph, u, v): graph[u].append(v)

def main():
    graph = defaultdict(list)
    # add(graph, "y", "y")
    # add(graph, "y", "a")
    # add(graph, "a", "y")
    # add(graph, "a", "m")
    # add(graph, "m", "m")
    graph = {
        'y': ['y', 'a'],
        'a': ['y', 'm'],
        'm': ['m'],
    }
    # graph = {
    #     'z0': ['z2'],
    #     'z1': ['z4'],
    #     'z2': ['z1'],
    #     'z3': ['z1', 'z5'],
    #     'z4': [],
    #     'z5': [],
    # }
    pagerank(graph, 0.85)

main()
