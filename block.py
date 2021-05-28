# Written by Kavin Mohan while following along with "Introduction to Blockchain" on Codecademy

# Definition of Block class with constructor and print_block and generate_hash methods
from datetime import datetime
from hashlib import sha256



class Block:
  # Block class constructor
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.hash = self.generate_hash()
    
  # prints block contents
  def print_block(self):
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
  # hash the blocks contents 
  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()