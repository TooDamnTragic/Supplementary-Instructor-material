import base64
import itertools
import string

# Base64 URL-encoded message
encoded_message = 'S8NNIMA3XylLsUwjRjSLJXk5QHhGzVu-dBZdwL5-RzxK2r930KO7wsI-eXdaPmtq_8I9TQPZfTOMYuZoU9PW01R9g0pFxIfUbnRJTkc='

# Step 1: Convert Base64 URL encoding to standard Base64
standard_base64 = encoded_message.replace('-', '+').replace('_', '/')
missing_padding = len(standard_base64) % 4
if missing_padding:
    standard_base64 += '=' * (4 - missing_padding)

# Step 2: Decode the Base64 string
decoded_bytes = base64.b64decode(standard_base64)
print(f"Decoded data length: {len(decoded_bytes)} bytes")

# Step 3: Analyze the Decoded Data
print("First 16 bytes of decoded data (hex):", decoded_bytes[:16].hex())

# Step 4: Attempt XOR Decryption with Potential Keys
possible_keys = [
    'REDRUM', 'redrum', 'SHINING', 'shining', 'THE SHINING'
    'ALLWORKANDNOPLAYMAKESJACKADULLBOY',
    'All work and no play makes Jack a dull boy',
    'DANNY', 'danny', 'ROOM237', 'room237',
    'OVERLOOK', 'overlook'
]

def xor_decrypt(data, key):
    key_bytes = key.encode('utf-8')
    return bytes([data[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data))])

for key in possible_keys:
    plaintext = xor_decrypt(decoded_bytes, key)
    try:
        text = plaintext.decode('utf-8')
        if all(char.isprintable() or char == '\n' for char in text):
            print(f"\nDecrypted with key '{key}':\n{text}")
    except UnicodeDecodeError:
        continue

# Step 5: Break Repeating-Key XOR Encryption Using Frequency Analysis
def single_byte_xor(data, key):
    return bytes([b ^ key for b in data])

def score_text(text):
    # Frequency analysis scoring
    frequency = {
        'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835,
        'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888,
        'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490,
        'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645,
        'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
        'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692,
        'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }
    return sum([frequency.get(chr(byte).lower(), 0) for byte in text])

best_score = 0
best_result = None
for key in range(256):
    plaintext = single_byte_xor(decoded_bytes, key)
    try:
        if all(chr(b) in string.printable for b in plaintext):
            score = score_text(plaintext)
            if score > best_score:
                best_score = score
                best_result = (key, plaintext)
    except:
        continue

if best_result:
    key, plaintext = best_result
    print(f"\nBest single-byte XOR key: {key}")
    print(f"Decrypted text:\n{plaintext.decode('utf-8')}")
else:
    print("No valid single-byte XOR decryption found.")

# Step 6: Attempt to Break Repeating-Key XOR Cipher
def hamming_distance(b1, b2):
    """Calculate the Hamming distance between two byte strings"""
    min_len = min(len(b1), len(b2))
    b1 = b1[:min_len]
    b2 = b2[:min_len]
    return sum(bin(byte1 ^ byte2).count('1') for byte1, byte2 in zip(b1, b2))

normalized_distances = []
for key_size in range(2, 41):
    # Create chunks of size key_size
    chunks = [decoded_bytes[i:i+key_size] for i in range(0, len(decoded_bytes), key_size)]
    # Need at least two chunks of equal length
    if len(chunks) < 2:
        continue
    if len(chunks[0]) != key_size or len(chunks[1]) != key_size:
        continue
    pairs = list(itertools.combinations(chunks[:4], 2))
    distances = [hamming_distance(p[0], p[1]) / key_size for p in pairs]
    normalized_distance = sum(distances) / len(distances)
    normalized_distances.append((key_size, normalized_distance))

# Sort key sizes by normalized distance
likely_key_sizes = sorted(normalized_distances, key=lambda x: x[1])[:5]
print("Likely key sizes:", [size for size, _ in likely_key_sizes])

for key_size, _ in likely_key_sizes:
    key = b''
    for i in range(key_size):
        block = decoded_bytes[i::key_size]
        scores = []
        for k in range(256):
            decrypted_block = bytes([b ^ k for b in block])
            try:
                decrypted_text = decrypted_block.decode('latin1')
                score = score_text(decrypted_block)
                scores.append((score, k))
            except:
                continue
        if scores:
            _, best_k = max(scores)
            key += bytes([best_k])
        else:
            key += b'\x00'

    full_key = (key * (len(decoded_bytes) // len(key))) + key[:len(decoded_bytes) % len(key)]
    plaintext = bytes([b ^ k for b, k in zip(decoded_bytes, full_key)])
    try:
        text = plaintext.decode('utf-8')
        if all(char in string.printable or char == '\n' for char in text):
            print(f"\nDecrypted with key size {key_size} and key '{key.decode('utf-8', errors='ignore')}':\n{text}")
    except UnicodeDecodeError:
        continue

# Additional attempt with a specific key
key = 'allworkandnoplaymakesjackadullboy'
key_bytes = key.encode('utf-8')
key_length = len(key_bytes)
full_key = (key_bytes * (len(decoded_bytes) // key_length)) + key_bytes[:len(decoded_bytes) % key_length]
plaintext = bytes([b ^ k for b, k in zip(decoded_bytes, full_key)])

try:
    text = plaintext.decode('utf-8')
    print(f"\nDecrypted with key '{key}':\n{text}")
except UnicodeDecodeError:
    print("Decryption with the key failed.")
