def pour(source, destination, current, volume1, volume2):
  jug1, jug2 = current
  if source == "J1":
    if jug1 > 0 and jug2 < volume2:
      amount = min(jug1, volume2 - jug2)
      updatedjug1 = jug1 - amount
      updatedjug2 = jug2 + amount
      return (updatedjug1, updatedjug2)
  else:
    if jug2 > 0 and jug1 < volume1:
      amount = min(jug2, volume1 - jug1)
      updatedjug1 = jug1 + amount
      updatedjug2 = jug2 - amount
      return (updatedjug1, updatedjug2)
  return None

def solve(volume1, volume2, target):
  seen = set()
  stack = [((0, 0), [])]
  while stack:
    current, moves = stack.pop()
    if current[0] == target or current[1] == target: return moves # final result
    seen.add(current)
    for move in ["FJ1", "EJ1", "FJ2", "EJ2", "PJ2J1", "PJ1J2"]:
      if move == "FJ1": new = (volume1, current[1])
      elif move == "FJ2": new = (current[0], volume2)
      elif move == "EJ1": new = (0, current[1])
      elif move == "EJ2": new = (current[0], 0)
      elif move == "PJ1J2": new = pour("J1", "J2", current, volume1, volume2)
      elif move == "PJ2J1": new = pour("J2", "J1", current, volume1, volume2)

      if new and new not in seen:
        updatedmoves = moves + [move]
        stack.append((new, updatedmoves))

  return None # no solution found

def main():
  volume1 = int(input("Enter volume of first jug: "))
  volume2 = int(input("Enter volume of second jug: "))
  target = int(input("Enter volume to be measured: "))
  solution = solve(volume1, volume2, target)
  if solution is None: print("No solution exists")
  else:
    for move in solution:
      text = ''
      if(move == "FJ1"): text = "Fill Jug 1"
      elif(move == "FJ2"): text = "Fill Jug 2"
      elif(move == "EJ1"): text = "Empty Jug 1"
      elif(move == "EJ2"): text = "Empty Jug 2"
      elif(move == "PJ1J2"): text = "Pour Jug 1 into Jug 2"
      elif(move == "PJ2J1"): text = "Pour Jug 2 into Jug 1"
      print(text)

main()