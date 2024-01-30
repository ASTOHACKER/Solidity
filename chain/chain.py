import datetime 
import json
import hashlib
from flask import Flask , jsonify
from flask_ngrok import run_with_ngrok
#################
from web3 import Web3
import requests
alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/qUKMx-nNLImY_kJHhk3OmIZOEdnP4E_R"
w3 = Web3(Web3.HTTPProvider(alchemy_url))

# Print if web3 is successfully connected
print(w3.is_connected())

# Get the latest block number
#print(latest_block)
##################







url = "https://eth-mainnet.g.alchemy.com/v2/docs-demo"

payload = {
    "id": 1,
    "jsonrpc": "2.0",
    "method": "eth_accounts"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
##################

class blockchain:
    def __init__(self) -> None:
        # Group block 
        self.chain = [] #LIST เก็บ block

        self.transaction = 0  # จำนวนเงิน // ข้อมูล
        #genesis block
        self.create_block(nonce=1 , previous_hash="0")
        #smart check 

# create block on block chain system
    def create_block(self,nonce,previous_hash):
        #เก็บส่วนประกอบของ block ของแต่ล่ะ block
        block = {
            "index" : len(self.chain) + 1, 
            "timestamp" : str(datetime.datetime.now()), # แปลง datetime เป็น string เพื่อให้สามารถแสดงข้อมูลได้
            "nonce" : nonce, #ค่า  Nonce =  ค่าที่ใช้ในการค้นหาค่า Hash ของ Block ตามกฎของระบบที่ได้กำหนดไว้ เช่น Proof-of-Work หมายความว่า หากเราต้องการจะสร้าง Block ขึ้นมาสัก Block หนึ่งในระบบ Blockchain เราจะต้องแสดงให้คนอื่น ๆ ที่อยู่ในระบบเห็นว่า เราได้ทำการแก้ปัญหาหรือทำงาน (Work) ตามกฎที่กำหนดไว้แล้ว
            "data" : self.transaction,
            "previous_hash" : previous_hash, # ค่า Current Hash ของ Block ก่อนหน้า ซึ่งเปรียบได้กับค่า Digital Signature ของ Block ก่อนหน้าโดยจะถูกจัดเก็บอยู่ในโครงสร้างของ Block ถัดไปเสมอ และหากมีการแก้ไขข้อมูลใน Block ก่อนหน้าจะทำให้ค่า Hash ของ Block ไม่เท่ากัน ทั้งนี้ในการออกแบบโครงสร้าง Block แต่ละแพลตฟอร์มอาจมีการใช้ชื่อเรียกที่แตกต่างกันออกไป
        }
        self.chain.append(block)
        return  block
    

#get service about previous block
    def get_previous_block(self):
        return self.chain[-1]

# เข้ารหัส block 
    def __hash__(self,block)-> int:
       #เรียง python object(dict)ให้เป็น = > json object
       encode_block = json.dumps(block,sort_keys=True).encode()
       #กำหนด รูปแบบ ให้เป็น SHA256
       return hashlib.sha256(encode_block).hexdigest()
    
    def proof_of_work(self,previous_nonce):
        # อยากได้ค่า nonce == ? ที่ส่งผลให้ได้ target hash = > 4 หลัก => 0000xxxx
        new_nonce = 1 #ค่า nonce ที่ต้องการ
        check_proof = False # ตัวแปรที่เช็ตค่า nonce ให้ได้ตาม target
        #แก้โจทย์ทางคณิตศาสตร์ 
        while check_proof is False:
            #เลขฐาน 16 มา 1 ชุด
            hashoperation = hashlib.sha256(str(new_nonce **2 - previous_nonce **2 ).encode()).hexdigest()
            if hashoperation[:4] == "0000":
                check_proof = True
            else:
                new_nonce += 1
        return new_nonce


    #ตรวจสอบ block 
    def is_chain_valid(self,chain):
        previouos_block  = chain[0]
        block_index = 1
        while block_index<len(chain):
            block = chain[block_index] #BLOCK ที่ตรวขสอบ
            if block["previous_hash"] != self.__hash__(previouos_block):
                return False
            
            previous_nonce = previouos_block["nounce"] #none ของ block ก่อนหน้า
            nonce = block["nonce"] # none ของ block  ที่ตรวจสอบ
            hashoperation = hashlib.sha256(str(nonce **2 - previous_nonce **2 ).encode()).hexdigest()

            if hashoperation[:4] == "0000":
                return False
            previouos_block = block
            block += 1
    
        return True
        
#use blochain
blockchain = blockchain()

print(blockchain.__hash__(blockchain.chain[0]))

#web server
app = Flask(__name__)
run_with_ngrok(app)
ALLOWED_HOSTS = ['*' ]
#routingdadad
@app.route('/')
def hello():
    return "<h1> TEST </h1>"

@app.route('/getchain',methods=["GET"])
def getchain():
    response = {
        "chain" : blockchain.chain,
        "length": len(blockchain.chain)
    }
    return jsonify(response),200


@app.route('/mining',methods=["GET"])
def mining_block():
     
    amount = 1000000 # จำนวนเงินการทำงานธุระกรรม
    blockchain.transaction = blockchain.transaction + amount
    #p o w
    previous_block = blockchain.get_previous_block()
    previous_nonce = previous_block["nonce"]
    #nonce
    nonce = blockchain.proof_of_work(previous_nonce)
    #hash ก่อนหน้า
    previous_hash = blockchain.__hash__(previous_block)
    #update new block
    block = blockchain.create_block(nonce,previous_hash)
    response = {
        "message": "Mining Block... Finished",
        "index"  :  block["index"],
        "timestamp" : block["timestamp"],
        "data" : block["data"],
        "nonce" : block["nonce"],
        "previous_hash" : block["previous_hash"],
    }
    return jsonify(response),200

@app.route('/is_valid',methods=["GET"])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid: # STATUS BLOCKCHAIN
            response = {"message":"IS VALID"}
    else:
        response = {"message":"IS VALID"}
    return jsonify(response),200


#run server
if __name__ == "__main__":
    app.run() 

print(len(blockchain))
print(blockchain.get_previous_block())




