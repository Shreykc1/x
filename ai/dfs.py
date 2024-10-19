class Graph():
    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        self.dict = dict

def dfs(graph, start, visited=None, total_distance=0):
    if visited is None:
        visited = set()
    
    visited.add(start)

    
    print(start)
    
    for i in graph[start] - visited:
        total_distance += 1
        total_distance = dfs(graph, i, visited, total_distance)
    
    return total_distance

myDict = {
    "a": set(["b", "c"]),
    "b": set(["a", "d", "e"]),
    "c": set(["a", "f"]),
    "d": set(["b"]),
    "e": set(["b"]),
    "f": set(["c"])
}


total_distance = dfs(myDict, 'a')
print(f"Total distance traveled: {total_distance}")