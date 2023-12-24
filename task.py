import random
import math
import hashlib

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(bitlength=8):
    p = q = 0

    while p == q:
        p = random_prime(bitlength)
        q = random_prime(bitlength)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def random_prime(bitlength):
    while True:
        num = random.getrandbits(bitlength)
        if is_prime(num):
            return num

def sign(message, private_key):
    n, d = private_key
    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    hashed_message_int = int(hashed_message, 16)
    signature = pow(hashed_message_int, d, n)
    return signature

def verify_signature(message, signature, public_key):
    n, e = public_key
    hashed_message = hashlib.sha256(message.encode()).hexdigest()
    hashed_message_int = int(hashed_message, 16)
    decrypted_signature = pow(signature, e, n)
    return decrypted_signature == hashed_message_int


if __name__ == "__main__":
    public_key, private_key = generate_keypair()

    message = "Nargiz, Akniet, Adema"

    signature = sign(message, private_key)

    is_valid_signature = verify_signature(message, signature, public_key)

    print("Original Message:", message)
    print("Signature:", signature)
    print("Is Valid Signature:", is_valid_signature)