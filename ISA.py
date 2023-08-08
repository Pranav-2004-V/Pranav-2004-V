from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

def generate_rsa_key_pair():
    # Generate an RSA key pair with a key length of 2048 bits
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_rsa(message, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    encrypted_message = cipher_rsa.encrypt(message)
    return encrypted_message

def decrypt_rsa(encrypted_message, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    decrypted_message = cipher_rsa.decrypt(encrypted_message)
    return decrypted_message

def encrypt_aes(message, session_key):
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message)
    return cipher_aes.nonce, tag, ciphertext

def decrypt_aes(nonce, tag, ciphertext, session_key):
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    decrypted_message = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return decrypted_message

# Generate RSA key pair
private_key, public_key = generate_rsa_key_pair()

# Message to be encrypted
message = b'This is a secret message'

# Generate a random session key for AES encryption
session_key = get_random_bytes(16)  # 16 bytes = 128 bits key length

# Encrypt the session key using RSA public key
encrypted_session_key = encrypt_rsa(session_key, public_key)

# Encrypt the message using AES with the session key
nonce, tag, ciphertext = encrypt_aes(message, session_key)

# Print the original message, encrypted session key, and encrypted message
print('Original message:', message)
print('Encrypted session key:', base64.b64encode(encrypted_session_key).decode('utf-8'))
print('Encrypted message:', base64.b64encode(ciphertext).decode('utf-8'))

# Decrypt the session key using RSA private key
decrypted_session_key = decrypt_rsa(encrypted_session_key, private_key)

# Decrypt the message using AES with the decrypted session key
decrypted_message = decrypt_aes(nonce, tag, ciphertext, decrypted_session_key)

# Print the decrypted message
print('Decrypted message:', decrypted_message)
