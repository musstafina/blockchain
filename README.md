# Blockchain Command-Line Application README

## Introduction

Welcome to our blockchain application! This command-line interface (CLI) application showcases the implementation of various blockchain components, including asymmetric encryption, digital signatures, and core blockchain features. The application allows users to add transactions to the blockchain, view the entire blockchain, and exit the program.

## Team Members

- Adema
- Nargiz
- Akniet

## Project Structure

The project is organized into the following components:

- **Encryption Module (Task 1):**
  - The `is_prime`, `gcd`, `mod_inverse`, `generate_keypair`, `random_prime`, `hash_function`, `encrypt`, `decrypt`, `sign`, and `verify_signature` functions are responsible for asymmetric encryption and digital signature generation and verification.

- **Blockchain Module (Task 2):**
  - The `Block` class represents an individual block in the blockchain, and the `Blockchain` class manages the entire chain.
  - The `calculate_merkle_root` function uses a hash function to generate the Merkle root for a block.
  - The `calculate_hash` function calculates the hash of a block based on its components.
  - The `create_genesis_block` function initializes the blockchain with a genesis block.
  - The `add_block` function adds a new block to the blockchain.

- **Main Program (Task 3):**
  - The `main` function serves as the entry point of the program, providing a menu for users to add transactions, display the blockchain, or exit.
- **Bonus Features:**
  - Proof-of-Work (PoW): Each block in the blockchain is mined with a proof-of-work mechanism, adding a level of security.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/musstafina/blockchain.git
   cd blockchain
   ```

2. **Run the Application:**
   ```bash
   python task.py
   ```

3. **Follow the Menu Options:**
   - Choose option `1` to add a transaction.
   - Choose option `2` to display the blockchain.
   - Choose option `3` to exit the program.

## Example Transaction

- Sender: A
- Receiver: B
- Amount: 10.0

The transaction is encrypted, signed, and added to the blockchain.

## Conclusion

Thank you for exploring our blockchain application! We look forward to presenting the project and answering any questions during the demonstration.
