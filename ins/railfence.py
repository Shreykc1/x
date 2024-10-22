def encrypt(plaintext, depth):
  ciphertext = ''
  rows = [[] for _ in range(depth)]
  current = 0
  direction = 'S'
  for char in plaintext: # construct rails by travesing diagonally
    rows[current].append(char)
    current = current + 1 if direction == 'S' else current - 1
    if current == depth-1 or current == 0:
      direction = 'N' if direction == 'S' else 'S'

  for row in rows:
    for char in row:
      ciphertext += char

  return ciphertext

def decrypt(ciphertext, depth):
  plaintext = ''
  rows = [[] for _ in range(depth)]
  current = 0
  direction = 'S'
  for char in ciphertext: # construct empty rails by traversing diagonally
    rows[current].append("*")
    current = current + 1 if direction == 'S' else current - 1
    if current == depth-1 or current == 0:
      direction = 'N' if direction == 'S' else 'S'

  char = 0
  for rail in rows:
    for pos in range(len(rail)):
      rail[pos] = ciphertext[char]
      char += 1
    
  current = 0
  direction = 'S'
  for char in ciphertext:
    plaintext += rows[current][0]
    del rows[current][0]
    current = current + 1 if direction == 'S' else current - 1
    if current == depth-1 or current == 0:
      direction = 'N' if direction == 'S' else 'S'
    
  return plaintext

text = input("Enter message: ").upper()
depth = int(input("Enter depth: "))
e = encrypt(text, depth)
print(f"\nEncrypted message: {e}")
d = decrypt(e, depth)
print(f"Decrypted message: {d}") 

# plaintext = MITHIBAI COLLEGE
# depth = 3
# ciphertext = MI LIHBICLEETAOG