import math

def getSequence(key):
  sortedkey = sorted(key)
  sequence = [sortedkey.index(char) for char in key]
  return sequence

def getPermutation(key):
  sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])
  permutation = [_[0] for _ in sorted_key]
  return permutation

def encrypt(plaintext, key):
  ciphertext = ''
  permutation = getPermutation(key)
  rows = math.ceil(len(plaintext) / len(key))
  cols = len(key)
  matrix = [['_' for _ in range(cols)] for _ in range(rows)]

  index = 0
  for i in range(rows):
    for j in range(cols):
      if index < len(plaintext):
        matrix[i][j] = plaintext[index]
        index += 1
  
  for num in permutation:
    for i in range(rows):
      ciphertext += matrix[i][num]

  return ciphertext

def decrypt(ciphertext, key):
  plaintext = ''
  return plaintext

text = input("Enter message: ")
key = input("Enter key: ")
e = encrypt(text, key)
print(f"\nEncrypted message: {e}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")