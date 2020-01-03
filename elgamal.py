#!/usr/bin/env python3

# Source of Info: https://www.debjitbiswas.com/elgamal/

from Crypto.Util.number import inverse
import sympy
import random
from binascii import hexlify, unhexlify

# Prime Number (p)
p = 7247
# Generator (g)
g = 138
# Alice's Private Key (x)
x = 2781
# Bob's Private Key (r)
r = 5660
# The Encrypted Message (m)
m = 3243

def shared_secret(g,x,p):
  # Shared Secret (h)
  h = pow(g,x,p)
  return h

def decrypt(x,c1,c2,p):
  s = pow(c1,x,p)
  dm = (c2 * inverse(s,p)) % p
  return dm

def encrypt(m,r,g,p,h):
  c1 = pow(g,r,p)
  c2 = (pow(h,r) * m) % p
  return c1,c2


if __name__ == "__main__":
  print("Warning: Anthing more than 3 characters could take a very long time to encrypt")
  input_message = input("Enter message to encrypt: ")
  inputbytes = str.encode(input_message)
  m = int(hexlify(inputbytes), 16)
  p = sympy.randprime(m*2, m*4)
  g = sympy.randprime(int(m/2), m)
  x = random.randint(int(m/2),m)
  r = random.randint(int(m/2),m)

  print("Bob's MESSAGE         : {}".format(input_message))
  print("MESSAGE as an int (M) : {}".format(m))
  print("Prime number (P)      : {}".format(p))
  print("Generator (G)         : {}".format(g))
  print("Alice private key (X) : {}".format(x))
  print("Bob's private key (R) : {}".format(r))

  h = shared_secret(g,x,p)
  print("Shared secret (H)     : {}".format(h))

  c1, c2 = encrypt(m,r,g,p,h)
  print("Encrypted Message (C1): {}".format(c1))
  print("Encrypted Message (C2): {}".format(c2))

  dm = decrypt(x,c1,c2,p)
  print("Decrypted Integer (dm): {}".format(dm))
  x = format(dm, 'x')
  print("Decrypted Hex (x)     : {}".format(x))
  message = unhexlify(x)
  print("Decrypted Message     : {}".format(message))
