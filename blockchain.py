# Written by Kavin Mohan while following along with "Introduction to Blockchain" on Codecademy

# Blockchain class implementation

#imports the Block class from block.py
from block import Block

# Blockchain constructor
class Blockchain:
  def __init__(self):
    self.chain = [] #contains a list of all the blocks
    self.all_transactions = []  #contains all the transactions
    self.genesis_block()

    #genesis block method, 420 chosen as hard coded hash
  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "420")
    self.chain.append(genesis_block)
    return self.chain

  # prints contents of blockchain
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()    
  
  # add block to blockchain `chain`
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
   #generate hash and proof of work
    new_block.generate_hash()
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block) #actually adds the block to the chain
    return(proof, new_block)
    

 # validate every block in the chain by checking the hashes
  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if(current.hash != current.generate_hash()):
        print("The current hash of the block does not equal the generated hash of the block.")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("The previous block's hash does not equal the previous hash value stored in the current block.")
        return False
    return True
  
# proof of work generated with default difficulty of 2 leading zeroes 
  def proof_of_work(self,block, difficulty=2):
    proof = block.generate_hash()
    while proof[:difficulty] != '0'*difficulty: #increment nonce until target hash is reached
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0
    return proof