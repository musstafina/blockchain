import random
import math
import hashlib
import json
import time
from datetime import datetime

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to calculate the modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate a key pair for RSA encryption
def generate_keypair(bitlength=8):
    p = q = 0

    # Choose two random prime numbers
    while p == q:
        p = random_prime(bitlength)
        q = random_prime(bitlength)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose a random public key (e) such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Calculate the private key (d) using the modular inverse of e
    d = mod_inverse(e, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

# Function to generate a random prime number
def random_prime(bitlength):
    while True:
        num = random.getrandbits(bitlength)
        if is_prime(num):
            return num

# Function to create a SHA-256 hash of the input data
def hash_function(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to encrypt a message using RSA
def encrypt(message, public_key):
    n, e = public_key
    cipher_text = [(ord(char) ** e) % n for char in message]
    return cipher_text

# Function to decrypt a message using RSA
def decrypt(cipher_text, private_key):
    n, d = private_key
    plain_text = [chr((char ** d) % n) for char in cipher_text]
    return ''.join(plain_text)

# Function to create a digital signature of a message using RSA
def sign(message, private_key):
    n, d = private_key
    hashed_message = hash_function(message)
    signature = [(ord(char) ** d) % n for char in hashed_message]
    return signature

# Function to verify the digital signature of a message using RSA
def verify_signature(message, signature, public_key):
    n, e = public_key
    hashed_message = hash_function(message)
    decrypted_signature = [(char ** e) % n for char in signature]
    return decrypted_signature == [ord(char) for char in hashed_message]

# Function to format a timestamp for display
def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')

# Class representing a block in a blockchain
class Block:
    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = time.time()
        self.merkle_root = self.calculate_merkle_root()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_merkle_root(self):
        return hash_function(json.dumps(self.transactions))

    def calculate_hash(self):
        block_data = f"{self.previous_hash}{self.merkle_root}{self.nonce}"
        return hash_function(block_data)

# Class representing a blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(previous_hash="0", transactions=[])

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(previous_hash=previous_block.hash, transactions=transactions)
        self.chain.append(new_block)

# Main function to run the blockchain application
def main():
    # Generate RSA key pair
    public_key, private_key = generate_keypair()

    # Create a blockchain
    blockchain = Blockchain()

    while True:
        print("\n1. Add Transaction")
        print("2. Display Blockchain")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sender = input("Enter sender: ")
            receiver = input("Enter receiver: ")
            amount = float(input("Enter amount: "))

            # Encrypt data and create a digital signature
            encrypted_data = encrypt(json.dumps({"sender": sender, "receiver": receiver, "amount": amount}), public_key)
            signature = sign(json.dumps({"sender": sender, "receiver": receiver, "amount": amount}), private_key)

            timestamp = time.time()
            formatted_timestamp = format_timestamp(timestamp)

            # Create a transaction and add it to the blockchain
            transaction = {"encrypted_data": encrypted_data, "signature": signature, "timestamp": formatted_timestamp}
            blockchain.add_block([transaction])

            print("Transaction added successfully.")

        elif choice == "2":
            for i, block in enumerate(blockchain.chain):
                print(f"\nBlock {i + 1}:")
                print("Previous Hash:", block.previous_hash)
                print("Merkle Root:", block.merkle_root)
                print("Nonce:", block.nonce)
                print("Hash:", block.hash)
                print("Transactions:")
                for transaction in block.transactions:
                    decrypted_data = decrypt(transaction["encrypted_data"], private_key)
                    is_valid_signature = verify_signature(decrypted_data, transaction["signature"], public_key)
                    print(f"  Sender: {json.loads(decrypted_data)['sender']}")
                    print(f"  Receiver: {json.loads(decrypted_data)['receiver']}")
                    print(f"  Amount: {json.loads(decrypted_data)['amount']}")
                    print(f"  Digital Signature: {'Valid' if is_valid_signature else 'Invalid'}")
                    print(f"  Timestamp: {transaction['timestamp']}")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
