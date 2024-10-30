import deslib

# Input Key
key = 'ABCDEF1234567890'
plain_text = "Hello world is definitely writtenn in more than 64 bits"

rk = deslib.make_rk(key)

print("Encryption")
cipher_text = deslib.bin2hex(deslib.encrypt(plain_text, rk))
print("Hex Cipher Text : ", cipher_text)
cipher_text = deslib.hex2text(cipher_text)

print("Decryption")
text = deslib.bin2hex(deslib.unpad(deslib.decrypt(cipher_text, rk)))
text = deslib.hex2text(text)
print("Plain Text : ", text)