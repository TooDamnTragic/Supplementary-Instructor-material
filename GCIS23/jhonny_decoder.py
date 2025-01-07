import base64
import gzip
from io import BytesIO

# Input string
s_urlsafe = 'S8NNIMA3XylLsUwjRjSLJXk5QHhGzVu-dBZdwL5-RzxK2r930KO7wsI-eXdaPmtq_8I9TQPZfTOMYuZoU9PW01R9g0pFxIfUbnRJTkc='

# Step 1: Decode the Base64 (URL Safe) string
decoded_bytes = base64.urlsafe_b64decode(s_urlsafe)

# Step 2: XOR the decoded bytes with the key "THE SHINING"
key = 'THE SHINING'
key_bytes = key.encode('utf-8')
key_length = len(key_bytes)

output_bytes = bytearray()
for i in range(len(decoded_bytes)):
    xor_byte = decoded_bytes[i] ^ key_bytes[i % key_length]
    output_bytes.append(xor_byte)

# Step 3: Decompress the XORed data using gzip
with gzip.GzipFile(fileobj=BytesIO(output_bytes)) as f:
    decompressed_data = f.read()

# Step 4: Decode the decompressed data to get the flag
result = decompressed_data.decode('utf-8')

# Print the final decrypted message
print("Decrypted message:")
print(result)
