from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# pip uninstall crypto
# pip install pycryptodome

def encrypt(plaintext, key):
  if len(key) not in (16, 24, 32):
    print("Key must be 16/24/32 bytes long")
    exit()

  if type(plaintext) is str: plaintext = plaintext.encode('utf-8')
  plaintext = pad(plaintext, AES.block_size)
  iv = get_random_bytes(AES.block_size)
  cipher = AES.new(key, AES.MODE_CBC, iv) # cbc mode
  ciphertext = cipher.encrypt(plaintext)

  return iv + ciphertext

def decrypt(ciphertext, key):
  if len(key) not in (16, 24, 32):
    print("Key must be 16/24/32 bytes long")
    exit()
  
  iv = ciphertext[ : AES.block_size]
  ciphertext = ciphertext[AES.block_size : ]
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plaintext = cipher.decrypt(ciphertext)
  plaintext = unpad(plaintext, AES.block_size)

  return plaintext.decode('utf-8')

text = input("Enter message: ")
key = b'ABCDEFGHIJKLMNOPQRSTUVWX'

e = encrypt(text, key)
print(f"\nEncrypted message: {e.hex()}")
d = decrypt(e, key)
print(f"Decrypted message: {d}")

# ciphertext = c71d1299fb5595b1ed0489623d6ccc8436fe161322155021b12864a97030e29c
# key = ABCDEFGHIJKLMNOPQRSTUVWX
# plaintext = hello world