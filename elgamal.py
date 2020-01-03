#!/usr/bin/env python3
# Created by Rob 'mubix' Fuller

# Source of Info: https://www.debjitbiswas.com/elgamal/

from Crypto.Util.number import inverse
import sympy
import random
from binascii import hexlify, unhexlify

def shared_secret(g,x,p):
  # Shared Secret (h)
  h = pow(g,x,p)
  return h

def encrypt(m,r,g,p,h):
  c1 = pow(g,r,p)
  # Stolen from https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/PublicKey/ElGamal.py
  c2 = (m * pow(h, r, p) ) % p
  return c1,c2

def decrypt(x,c1,c2,p):
  s = pow(c1,x,p)
  dm = (c2 * inverse(s,p)) % p
  return dm

if __name__ == "__main__":
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
