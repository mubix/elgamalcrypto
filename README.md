# elgamalcrypto
Simple Python Elgamal Encryption and Decryption Tool

This script needs some work on figuring out how to encrypt faster as the power for c2 takes forever if you are into bigger numbers, but the decryption works great.

## Dependencies

- `pip install sympy` - This is so the prime generator works quickly.

## Example Run

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
