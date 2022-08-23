from hashlib import sha256


# Function for giving a string input and having a hash returned 
def SHA256(text):
    # Example string
    # dummyString = "ABC"

    # Encode it to ascii
    encodedString = text.encode("ascii")

    # Hash of the string in Object format
    hashedString = sha256(encodedString)

    # Hash of the string in 256bit hex
    finalString = hashedString.hexdigest()
    return finalString;


def mine(block_number, transactions, previous_hash, nonce=3): 
    text = str(block_number) + transactions + previous_hash + str(nonce)
    return SHA256(text)
    pass



def miner(): 
    import time
    MAX_NONCE = 3000000000000
    block_number = 5

    transactions = '''
    user1 -> user3,
    user5 -> user0,
    user6 -> user9,
    user44 -> user1
    '''

    previous_hash = "000000000000000000d4c8b9d5388e42bf084e29546357c63cba8324ed4ec8bf"
    
    difficulty_level = 4


    # new_hash = mine(block_number, transactions, previous_hash, difficulty_level, nonce)

    prefix = "0" * difficulty_level
    
    start = time.time()
    for nonce in range(MAX_NONCE):
        new_hash = mine(block_number, transactions, previous_hash, nonce)
        if new_hash.startswith(prefix):
            print("Successfully mined a bitcoin with nonce value:", nonce)
            print("Hash: ", new_hash)
            total_time = str((time.time() - start))
            print("Done in: ", total_time, "seconds")
            return new_hash
        
    
    raise BaseException(f"Couldn't mine a btc after trying {MAX_NONCE} times")
    
if __name__== "__main__":
    miner()

