import random

def f(x): return -(x - 3)**2 + 10

def hillclimbing(start):
  optima = start
  height = f(start)
  while True:
    leftNeighbor = optima - 0.01
    rightNeighbor = optima + 0.01
    leftHeight = f(leftNeighbor)
    rightHeight = f(rightNeighbor)
    if leftHeight >= height and rightHeight >= height:
      if leftHeight >= rightHeight:
        optima = leftNeighbor
        height = leftHeight
      else:
        optima = rightNeighbor
        height = rightHeight
    elif leftHeight >= height:
      optima = leftNeighbor
      height = leftHeight
    elif rightHeight >= height:
      optima = rightNeighbor
      height = rightHeight
    else: break
  return optima, height

def main():
  start = round(random.uniform(0, 10), 3)
  optima, height = hillclimbing(start)
  print(f"Starting Point: {start}")
  print(f"Local Optima: {optima}")
  print(f"f(x): {height}")

main()
