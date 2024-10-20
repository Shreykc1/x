def get_neighbours(x, y):
  neighbours = []
  for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N: neighbours.append((nx, ny))
  return neighbours

def perceive(x, y): return world[x][y]

def update_kb(x, y, percepts):
  kb[x][y]['Safe'] = True
  kb[x][y]['P'] = False
  kb[x][y]['W'] = False
  kb[x][y]['B'] = 'B' in percepts
  kb[x][y]['S'] = 'S' in percepts
  infer()

def infer():
  inferences_left = True
  while inferences_left:
    inferences_left = False

    # On Breeze
    for x in range(N):
      for y in range(N):
        if kb[x][y]['B'] == True:
          adjacent_pit_unknown = [(nx, ny) for nx, ny in get_neighbours(x, y) if kb[nx][ny]['P'] == 'Unknown']
          if len(adjacent_pit_unknown) == 1:
            nx, ny = adjacent_pit_unknown[0]
            if kb[nx][ny]['P'] != True:
              kb[nx][ny]['P'] = True
              inferences_left = True
        elif kb[x][y]['B'] == False:
          for nx, ny in get_neighbours(x, y):
            if kb[nx][ny]['P'] != False:
              kb[nx][ny]['P'] = False
              inferences_left = True
              if kb[nx][ny]['W'] == False and kb[nx][ny]['Safe'] != True:
                kb[nx][ny]['Safe'] = True
                inferences_left = True

    # On Stench
    for x in range(N):
      for y in range(N):
        if kb[x][y]['S'] == True:
          adjacent_wumpus_unknown = [(nx, ny) for nx, ny in get_neighbours(x, y) if kb[nx][ny]['W'] == 'Unknown']
          if len(adjacent_wumpus_unknown) == 1:
            nx, ny = adjacent_wumpus_unknown[0]
            if kb[nx][ny]['W'] != True:
              kb[nx][ny]['W'] = True
              for wx in range(N):
                for wy in range(N):
                  if (wx, wy) != (nx, ny) and kb[wx][wy]['W'] != False:
                    kb[wx][wy]['W'] = False
                    inferences_left = True
              inferences_left = True
        elif kb[x][y]['S'] == False:
          for nx, ny in get_neighbours(x, y):
            if kb[nx][ny]['W'] != False:
              kb[nx][ny]['W'] = False
              inferences_left = True
              if kb[nx][ny]['P'] == False and kb[nx][ny]['Safe'] != True:
                kb[nx][ny]['Safe'] = True
                inferences_left = True

def solve():
  x, y = 0, 0
  path = [(x, y)]
  history = [(x, y)]
  visited = set()
  visited.add((x, y))
  update_kb(x, y, perceive(x, y))
  while True:
    percepts = perceive(x, y)
    if 'G' in percepts:
      print("Gold found:", (x, y))
      print("Final Path:", path)
      print("Movement History:", history)
      return
    possible_moves = [(nx, ny) for nx, ny in get_neighbours(x, y) if (nx, ny) not in visited and kb[nx][ny]['Safe'] == True]
    if possible_moves:
      nx, ny = possible_moves[0]
      path.append((nx, ny))
      history.append((nx, ny))
      x, y = nx, ny
      visited.add((x, y))
      update_kb(x, y, perceive(x, y))
    else:
      if len(path) > 1:
        path.pop()
        x, y = path[-1]
        history.append((x, y))
      else:
        print("No path to the gold found.")
        return

world = [
  ['', 'S', 'W', 'S'],
  ['B', 'G', 'SB', ''],
  ['P', 'B', 'P', 'B'],
  ['B', '', 'B', 'P']
]

N = len(world)

kb = {
  x: {
    y: {
      'P': 'Unknown', 'W': 'Unknown', 'B': 'Unknown', 'S': 'Unknown', 'Safe': 'Unknown'
    } for y in range(N)
  } for x in range(N)
}

solve()
