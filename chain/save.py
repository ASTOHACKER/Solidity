def __hash__(self,block) -> int:
       #เรียง python object(dict)ให้เป็น = > json object
       encode_block = json.dumps(block,sort_keys=True).encode()
       return encode_block
       
#แสดงถึง previuos block
print(blockchain.get_previous_block())
# เข้ารหัส block แรก
print(blockchain.__hash__(blockchain.chain[0]))
print(blockchain.hash(blockchain.chain[0]))
#TEST SYSTEM
Smart contract lang
Solidity
WASM rust
C++
Golang

Framework blockchain core
Hyperledger 
Ethereum based
Corda R3
Substrate
Bitcoin

Tool and aditional knowleged needed
Web3js
Ethers
Hardhat
Truffle
Crypto Wallet e.g. trust wallet metamask
Consensus algorithm
Merkle tree
Hashfuncfion

Advanced knowledge optional
Zero knowledge proof
Interop crosschain