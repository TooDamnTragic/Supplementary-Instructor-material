import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import itertools

def attempt_vigenere_decrypt(ciphertext, key):
    decrypted = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            # Determine the shift for this character
            shift = ord(key[i % key_length].upper()) - ord('A')
            # Decrypt the character
            if char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += char
    return decrypted

def attempt_aes_decrypt(ciphertext, key):
    try:
        # Pad the key to 16, 24, or 32 bytes
        key = key.encode('utf-8')
        key = key.ljust(32, b'\0')[:32]
        
        # Decode base64
        ciphertext = base64.b64decode(ciphertext)
        
        # Try different modes
        for mode in [AES.MODE_ECB, AES.MODE_CBC]:
            cipher = AES.new(key, mode)
            try:
                decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
                return decrypted.decode('utf-8')
            except:
                pass
    except:
        pass
    return None

def attempt_xor_decrypt(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext)
    decrypted = ""
    for i, char in enumerate(ciphertext):
        decrypted += chr(char ^ ord(key[i % len(key)]))
    return decrypted

def main():
    ciphertext = "S8NNIMA3XylLsUwjRjSLJXk5QHhGzVu-dBZdwL5-RzxK2r930KO7wsI-eXdaPmtq_8I9TQPZfTOMYuZoU9PW01R9g0pFxIfUbnRJTkc="
    key = "THE SHINING"
    
    print("Attempting Vigenère decryption:")
    print(attempt_vigenere_decrypt(ciphertext, key))
    
    print("\nAttempting AES decryption:")
    aes_result = attempt_aes_decrypt(ciphertext, key)
    if aes_result:
        print(aes_result)
    else:
        print("AES decryption failed")
    
    print("\nAttempting XOR decryption:")
    print(attempt_xor_decrypt(ciphertext, key))
    
    print("\nAttempting with key variations:")
    key_variations = [''.join(p) for p in itertools.permutations(key)]
    for variant in key_variations[:5]:  # Limit to first 5 variations to avoid excessive output
        print(f"\nUsing key variant: {variant}")
        print("Vigenère:", attempt_vigenere_decrypt(ciphertext, variant))
        aes_result = attempt_aes_decrypt(ciphertext, variant)
        print("AES:", aes_result if aes_result else "Failed")
        print("XOR:", attempt_xor_decrypt(ciphertext, variant))

if __name__ == "__main__":
    main()