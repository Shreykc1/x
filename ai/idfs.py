from collections import defaultdict

def dls(graph, currentnode, goal, limit, path):
  if limit == 0:
    if currentnode == goal: return path + [currentnode]
    else: return None
  elif limit > 0:
    path = path + [currentnode]
    if currentnode == goal: return path
    for neighbor, cost in graph[currentnode]:
      if neighbor not in path:
        result = dls(graph, neighbor, goal, limit - 1, path)
        if result is not None: return result
    return None

def idfs(graph, start, goal):
  depth = 0
  while True:
    result = dls(graph, start, goal, depth, [])
    if result is not None: return result
    depth += 1

def add(graph, u, v, cost):
  graph[u].append((v, cost))
  graph[v].append((u, cost))

def main():
  graph = defaultdict(list)
  add(graph, "A", "Z", 75)
  add(graph, "A", "T", 118)
  add(graph, "A", "S", 140)
  add(graph, "Z", "O", 71)
  add(graph, "O", "S", 151)
  add(graph, "T", "L", 111)
  add(graph, "L", "M", 70)
  add(graph, "M", "D", 75)
  add(graph, "D", "C", 120)
  add(graph, "S", "R", 80)
  add(graph, "S", "F", 99)
  add(graph, "R", "C", 146)
  add(graph, "C", "P", 138)
  add(graph, "R", "P", 97)
  add(graph, "F", "B", 211)
  add(graph, "P", "B", 101)
  add(graph, "B", "G", 90)
  add(graph, "B", "U", 85)
  add(graph, "U", "H", 98)
  add(graph, "H", "E", 86)
  add(graph, "U", "V", 142)
  add(graph, "V", "I", 92)
  add(graph, "I", "N", 87)

  start = input("Enter start node: ")
  goal = "B"
  path = idfs(graph, start, goal)
  if path: print(f"Path from {start} to {goal}: {path}")
  else: print("No path found")

if __name__ == '__main__': main()
