class Graph():
    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        self.dict = dict

def bfs(graph,start):
    visited = set()
    stacc = []
    a = start
    while len(visited) != len(graph):
        for i in graph[a] - visited:
            stacc.append(i)
        a = stacc.pop(0)
        visited.add(a)
    return visited

myDict = {
    "a": set(["b", "c"]),
    "b": set(["a", "d", "e"]),
    "c": set(["a", "f"]),
    "d": set(["b"]),
    "e": set(["b"]),
    "f": set(["c"])
}


total_distance = bfs(myDict, 'a')
print(f" {total_distance}")