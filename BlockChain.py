import hashlib
import json
import random


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.new_block(
            previous_hash="0000000000000000000000000000000000000000000", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

    @property
    def last_block(self):

        return self.chain[-1]
    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

    def outputChain(self):
        print(self.chain)

blockchain = Blockchain()

t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
blockchain.new_block(12345)

t3 = blockchain.new_transaction("Mike", "Alice", '1 BTC')
blockchain.new_block(6789)

choice = False
while choice is not True:
    print("CHOOSE PRODUCT\n\t Product 1. \n\t Product 2.")
    ch = input("\nENTER CHOICE: ")
    rname = input("ENTER RECEPIENT NAME: ")

    if ch == 1:
        u1 = blockchain.new_transaction("Self", rname, "5 BTC")
    elif ch == 2:
        u2 = blockchain.new_transaction("Self", rname, "7 BTC")

    proof = random.randint(0, 9999)
    blockchain.new_block(proof)
    print("Transaction succesful")
    blockchain.outputChain()

    choice = True