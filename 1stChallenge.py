import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class InvalidSignature(Exception):
    pass

class InvalidKey(Exception):
    pass

def crac(pas):
    passwd = pas
    passwd = bytes(passwd, 'utf-8')
    cleartext = pas
    cleartext = bytes(cleartext, 'utf-8')
    print(passwd)
    print(cleartext)
    try:
        salt = b'\xd4\x1f\xceg\xe9\xafW\xad\xb7+Y\xc3\xd9t\xe1\xc6'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(passwd))
        f = Fernet(key)
        cyphertext = f.encrypt(cleartext)
        problem = b'gAAAAABgoqMJ17XcgGFW347sJ9q1cXjzd1Cl74v42sZVhmbGGer1_l1NFfZSM-FRCVpCaZ9-JYjy5Ut0Ycy4E1GHyUxCSEgROSw2HFsJjX43qZgk2AyMG1Vzfxx8V212x3WWwszfCV1rR2KWHvUyorQB-0asgI3NLcrZiLVjJSQHg2qOqqKNUyv-TQsR-EIo-GgI4FOnA1kyFymTQv2Vcjxq4zAtUO3-nssuxuVC_n27xefX4eRd_GrnonCvRL_0b_3KYt-pQp4iT_hcbvuEnuM--Ue-F_BjYg=='
        print(f.decrypt(cyphertext))
        cap =f.decrypt(problem)
        print(cap)

    except Exception:
        pass

s = 'stefano'
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

for x in range(len(s) + 1):
    for x2 in range(0, 10):
        add2 = number[x2]
        w1 = s[:x] + add2 + s[x:]
        for y in range(len(w1) + 1):
            for z in range(0, 26):
                add = password[z]
                w2 = w1[:y] + add + w1[y:]
                passwd = w2
                crac(passwd)
                print(passwd)