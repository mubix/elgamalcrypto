# elgamalcrypto
Simple Python Elgamal Encryption and Decryption Tool

This script needs some work on figuring out how to encrypt faster as the power for c2 takes forever if you are into bigger numbers, but the decryption works great.

## Helpful Resources:
- Christof Paar's video on Elgamal - https://www.youtube.com/watch?v=tKNY1zhK3sQ
- Christof Paar's book on Cryptography - https://www.amazon.com/Understanding-Cryptography-Textbook-Students-Practitioners/dp/3642041000/
- ElGamal Encryption Playground - https://www.debjitbiswas.com/elgamal/

## Dependencies

- `pip install sympy` - This is so the prime generator works quickly.

## Example 2 Character Run with Verification

```
$ time ./elgamal.py
Warning: Anthing more than 3 characters could take a very long time to encrypt
Enter message to encrypt: it
Bob's MESSAGE         : it
MESSAGE as an int (M) : 26996
Prime number (P)      : 61253
Generator (G)         : 23087
Alice private key (X) : 16103
Bob's private key (R) : 20490
Shared secret (H)     : 36479
Encrypted Message (C1): 2362
Encrypted Message (C2): 6772
Decrypted Integer (dm): 26996
Decrypted Hex (x)     : 6974
Decrypted Message     : b'it'

real	0m1.649s
user	0m0.285s
sys	0m0.016s
```
![](elgamal_run.png)

## Example 3 Character Run

```
$ time python3 elgamal.py
Warning: Anthing more than 3 characters could take a very long time to encrypt
Enter message to encrypt: Bob
Bob's MESSAGE         : Bob
MESSAGE as an int (M) : 4353890
Prime number (P)      : 10053557
Generator (G)         : 3153629
Alice private key (X) : 3872046
Bob's private key (R) : 3291605
Shared secret (H)     : 2352935
Encrypted Message (C1): 9416744
Encrypted Message (C2): 5222411
Decrypted Integer (dm): 4353890
Decrypted Hex (x)     : 426f62
Decrypted Message     : b'Bob'

real	0m25.425s
user	0m23.683s
sys	0m0.048s
```
