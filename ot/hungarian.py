def display(matrix):
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      print(matrix[row][col], end='\t')
    print()
  print()

def addColumn(matrix):
  n = len(matrix) - len(matrix[0])
  while n > 0:
    for row in matrix:
      row.append(0)
    n -= 1

def addRow(matrix):
  n = len(matrix[0]) - len(matrix)
  while n > 0:
    matrix.append([0] * len(matrix[0]))
    n -= 1

def rowSubtract(matrix):
  for row in range(len(matrix)):
    minimum = float('inf')
    for col in range(len(matrix[0])):
      minimum = min(minimum, matrix[row][col])
    for col in range(len(matrix[0])):
      matrix[row][col] -= minimum

def colSubtract(matrix):
  for col in range(len(matrix[0])):
    minimum = float('inf')
    for row in range(len(matrix)):
      minimum = min(minimum, matrix[row][col])
    for row in range(len(matrix)):
      matrix[row][col] -= minimum

def assign(matrix):
  rows, cols = len(matrix), len(matrix[0])

  for step in range(1, 3):
    # row-wise assignment
    for row in range(rows):
      rowzeroes = 0
      zerocol = -1
      for col in range(cols): # count number of zeroes in row
        if matrix[row][col] == 0:
          rowzeroes += 1
          zerocol = col
      if rowzeroes == 1 or (rowzeroes > 1 and step == 2):  # if multiple zeroes, try randomly
        matrix[row][zerocol] = '[0]'
        for nrow in range(rows):
          if matrix[nrow][zerocol] == 0: matrix[nrow][zerocol] = 'X'
    
    # col-wise assignment
    for col in range(cols):
      colzeroes = 0
      zerorow = -1
      for row in range(rows):
        if matrix[row][col] == 0:
          colzeroes += 1
          zerorow = row
      if colzeroes == 1 or (colzeroes > 1 and step == 2):  # if multiple zeroes, try randomly
        matrix[zerorow][col] = '[0]'
        for ncol in range(cols):
          if matrix[zerorow][ncol] == 0: matrix[zerorow][ncol] = 'X'

def hungarian(matrix):
  rows, cols = len(matrix), len(matrix[0])
  markedRows = set()
  markedCols = set()

  # mark unassigned row
  for row in range(rows):
    if '[0]' not in matrix[row]: markedRows.add(row)
  
  # mark assigned row's crossed columns
  for row in markedRows:
    for col in range(cols):
      if matrix[row][col] == 'X': markedCols.add(col)

  # mark crossed column's assigned rows
  for col in markedCols:
    for row in range(rows):
      if matrix[row][col] == '[0]': markedRows.add(row)
  
  # find minimum uncovered element
  minimum = float('inf')
  for row in range(rows):
    for col in range(cols):
      if matrix[row][col] == '[0]' or matrix[row][col] == 'X': matrix[row][col] = 0 # reset all assignments
      if row in markedRows and col not in markedRows:
        minimum = min(minimum, matrix[row][col])
  
  # subtract and add minimum to elements
  for row in range(rows):
    for col in range(cols):
      if row in markedRows and col not in markedCols:
        matrix[row][col] -= minimum
      if row not in markedRows and col in markedCols:
        matrix[row][col] += minimum

def valid(matrix):
  assigned = 0
  for row in matrix:
    if '[0]' in row:  assigned += 1
  return assigned == len(matrix)

def solve(matrix):
  if len(matrix) > len(matrix[0]): addColumn(matrix)
  if len(matrix) < len(matrix[0]): addRow(matrix)
  rowSubtract(matrix)
  colSubtract(matrix)
  assign(matrix)
  display(matrix)

  if not valid(matrix):
    print("\nApplying Hungarian Method\n")
    hungarian(matrix)
    assign(matrix)
    display(matrix)

matrix = [
  [80, 140, 80, 100, 56, 98],
  [48, 64, 94, 126, 170, 100],
  [56, 80, 120, 100, 70, 64],
  [99, 100, 100, 104, 80, 90],
  [64, 80, 90, 60, 60, 76],
]

# matrix = [
#   [10, 7, 8],
#   [8, 9, 7],
#   [7, 12, 6],
#   [10, 10, 8]
# ]

solve(matrix)