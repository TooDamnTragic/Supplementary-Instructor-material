import base64

# Step 1: Base64 URL-safe decode
encoded_str = 'S8NNIMA3XylLsUwjRjSLJXk5QHhGzVu-dBZdwL5-RzxK2r930KO7wsI-eXdaPmtq_8I9TQPZfTOMYuZoU9PW01R9g0pFxIfUbnRJTkc='
decoded_data = base64.urlsafe_b64decode(encoded_str)

# Step 4: Single-byte XOR decryption
for key in range(256):
    xored = bytes([b ^ key for b in decoded_data])
    if b'All work' in xored:
        flag = xored.decode('utf-8', errors='ignore')
        print(f'Flag: flag{{{flag.strip()}}}')
        break
