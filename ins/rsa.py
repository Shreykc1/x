def gcd(a, b):
  if a == 0: return b
  return gcd(b % a, a)

def generateKeys(p, q):
  n = p * q
  totient = (p - 1)*(q - 1)
  for i in range(2, totient):
    if gcd(i, totient) == 1:
      public = i
      break
  
  for k in range(10):
    private = (1 + (k * totient))/public
    if private != public and round(private) == private: break

  return (public, round(private))

def encrypt(plaintext, public, n): return (plaintext ** public) % n

def decrypt(ciphertext, private, n): return (ciphertext ** private) % n

def main():
  p = int(input("Enter value of p: "))
  q = int(input("Enter value of q: "))
  n = p * q

  plaintext = int(input("Enter message: "))
  if plaintext >= n:
    print("Message too large")
    exit()

  e, d = generateKeys(p, q)
  encrypted = encrypt(plaintext, e, n)
  decrypted = decrypt(encrypted, d, n)
  print(f"\nPublic Key: {e}")
  print(f"Private Key: {d}")
  print(f"\nEncrypted Message: {encrypted}")
  print(f"Decrypted Message: {decrypted}")

main()

# p = 3
# q = 5
# m = 2
# public = 3
# private = 11
# encrypted = 8