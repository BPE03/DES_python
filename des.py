import deslib

# Input Key
key = '1234567890ABCDEF'
plain_text = "udah bisa coyyyy halogen"

rk = deslib.make_rk(key)

print("Encryption")
cipher_text = deslib.encrypt(plain_text, rk)
print("Hex Cipher Text : ", deslib.bin2hex(cipher_text))
cipher_text = cipher_text.encode('latin-1')
cipher_text = cipher_text.decode('latin-1')
cipher_text = deslib.bin2text(cipher_text)

print("Decryption")
text = (deslib.decrypt(cipher_text, rk))
#text = deslib.hex2text(text)
print("Plain Text : ", text)