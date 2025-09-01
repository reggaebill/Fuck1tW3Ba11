from cryptography.fernet import Fernet


###you know what to do
key = b''
f = Fernet(key)

###use this next line to encrypt a message. String must be prefixed with b' and suffixed with '
#token = f.encrypt(b"")

###use this line's output to update ReadME
#print(token)


###update token with new README message to decrypt
token = b''
###this is the juice.
message = (f.decrypt(token))

print(message)