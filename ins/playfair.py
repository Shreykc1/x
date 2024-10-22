

def display(grid):
  for i in range(5):
    for j in range(5):
      print(grid[i][j], end=' ')
    print()
  print()

def filter(keyword):
  seen = set()
  key = ''
  for char in keyword:
    if char not in seen: key += char
    seen.add(char)
  return key

def getMatrix(keyword):
  keyword = filter(keyword)
  grid = [['_'] * 5 for _ in range(5)]
  letters = [chr(char) for char in range(65, 91) if chr(char) not in keyword and char != 74] # skip keyword letters and J
  
  ptr = 0
  fillingKey = True
  for row in range(5):
    for col in range(5):
      if fillingKey:
        grid[row][col] = keyword[ptr] if keyword[ptr] != 'J' else 'I'
        ptr += 1
        if ptr >= len(keyword): # finished filling key
          fillingKey = False
          ptr = 0
      else:
        grid[row][col] = letters[ptr]
        ptr += 1

  positions = {} # map for getting character row and column
  for row in range(5):
    for col in range(5):
      positions[grid[row][col]] = (row, col)

  return grid, positions

def getPairsEncrypt(text):
  pairs = []
  text = list(text)
  length = len(text)
  i = 0
  while i < length:
    if i == length - 1: # last letter
      pairs.append(f'{text[i]}X')
      break
    if text[i] == text[i+1]: # same letters
      pairs.append(f'{text[i]}X')
      text.insert(i+1, 'X')
      length += 1
    else: pairs.append(f'{text[i]}{text[i+1]}')
    i += 2
  return pairs

def getPairsDecrypt(ciphertext):
  pairs = []
  ciphertext = list(ciphertext)
  i = 0
  while i < len(ciphertext):
    pairs.append(f'{ciphertext[i]}{ciphertext[i+1]}')
    i += 2
  return pairs


def encrypt(plaintext, key):
  grid, positions = getMatrix(key)
  pairs = getPairsEncrypt(plaintext)

  ciphertext = ""
  for pair in pairs:
    row1, col1 = positions[pair[0]]
    row2, col2 = positions[pair[1]]
    if row1 == row2: ciphertext += grid[row1][(col1 + 1) % 5] + grid[row1][(col2 + 1) % 5] # same row
    elif col1 == col2: ciphertext += grid[(row1 + 1) % 5][col1] + grid[(row2 + 1) % 5][col1] # same col
    else: ciphertext += grid[row2][col1] + grid[row1][col2]
  return ciphertext

def decrypt(ciphertext, key):
  grid, positions = getMatrix(key)
  pairs = getPairsDecrypt(ciphertext)
  plaintext = ""
  for pair in pairs:
    row1, col1 = positions[pair[0]]
    row2, col2 = positions[pair[1]]
    if row1 == row2: plaintext += grid[row1][(col1 + 4) % 5] + grid[row1][(col2 + 4) % 5] # same row
    elif col1 == col2: plaintext += grid[(row1 + 4) % 5][col1] + grid[(row2 + 4) % 5][col1] # same col
    else: plaintext += grid[row2][col1] + grid[row1][col2]
  return plaintext

key = input("Enter keyword: ").upper()
text = input("Enter message: ").upper()
e = encrypt(text, key)
print(f"\nEncrypted message: {e}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")

# key = COMPUTER
# plaintext = COMMUNICATE
# ciphertext = OMRMPCGSTPER