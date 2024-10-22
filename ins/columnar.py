import math

def display(grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      print(grid[i][j], end=' ')
    print()

def getSequence(key):
  letters = list(key)
  positions = []
  for i in range(len(letters)):
    positions.append((letters[i], i))
  positions = sorted(positions)
  
  sequence = [0 for _ in range(len(key))]
  for i in range(len(positions)):
    letter, original = positions[i]
    sequence[original] = i
  
  column_sequence = []
  for i in range(len(sequence)):
    column_sequence.append((sequence[i], i))
  column_sequence.sort()

  return column_sequence

def encrypt(plaintext, key):
  ciphertext = ''
  sequence = getSequence(key)
  rows = math.ceil(len(plaintext) / len(key))
  cols = len(key)
  matrix = [['_' for _ in range(cols)] for _ in range(rows)]

  ptr = 0
  for row in range(rows):
    for col in range(cols):
      if ptr < len(plaintext):
        matrix[row][col] = plaintext[ptr] if plaintext[ptr] != ' ' else '_'
        ptr += 1
      else: matrix[row][col] = '_'
  
  for _, col in sequence: # _ ka matlab useless (like you)
    for row in range(rows):
      ciphertext += matrix[row][col]

  return ciphertext

def decrypt(ciphertext, key):
  plaintext = ''
  sequence = getSequence(key)
  rows = math.ceil(len(ciphertext) / len(key))
  cols = len(key)
  matrix = [['_' for _ in range(cols)] for _ in range(rows)]

  ptr = 0
  for _, col in sequence: # _ ka matlab useless (like you)
    for row in range(rows):
      if ptr < len(ciphertext):
        matrix[row][col] = ciphertext[ptr]
        ptr += 1
      else: matrix[row][col] = '_'

  for row in range(rows):
    for col in range(cols):
      plaintext += matrix[row][col] if matrix[row][col] != '_' else ' '
  return plaintext

text = input("Enter message: ").upper()
key = input("Enter key: ").upper()
e = encrypt(text, key)
print(f"\nEncrypted message: {e}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")

# text = HELLO WORLD
# key = XNRAD
# ciphertext = LR_OL_EW_LO_H_D