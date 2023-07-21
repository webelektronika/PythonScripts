from cryptography.fernet import Fernet
 
msg = input("* Enter a string to encrypt: ")
 
#key = Fernet.generate_key()
key = b'wFjZYcvRM9DPfsaNtmPV8Pr6tcl-IuwsWznRx_rSkps='

fernet = Fernet(key)
 
encMsg = fernet.encrypt(msg.encode())
 
print("Clear text: ", msg)
print("key: ", key)
print("encrypted string: ", encMsg)
 
decMsg = fernet.decrypt(encMsg).decode() 
print("decrypted string: ", decMsg)
