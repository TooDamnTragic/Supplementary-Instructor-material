import string

# The target text to decrypt to find FLAG
key = "nevermore"

def alpha_to_num(ch):
    return ord(ch) - ord('a')

def num_to_alpha(num):
    return chr(num + ord('a'))

def mod_inv(a, m):
    # Using extended Euclidean algorithm to find modular inverse
    return pow(a, -1, m) if a % m != 0 else None

def decrypt_with_params(text, A, B):
    a_1 = mod_inv(A, 26)
    if not a_1:
        return None  # Skip if no modular inverse exists for A
    
    result = ""
    for ch in text:
        if ch not in string.ascii_lowercase:
            continue  # skip non-lowercase letters
        y = alpha_to_num(ch)
        x = ((y - B) * a_1) % 26
        result += num_to_alpha(x)
    return result

def encrypt_with_params(text, A, B):
    result = ""
    for ch in text:
        if ch not in string.ascii_lowercase:
            continue  # skip non-lowercase letters
        x = alpha_to_num(ch)
        y = (A * x + B) % 26
        result += num_to_alpha(y)
    return result

# Possible values for A are those that are coprime with 26
possible_A_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
possible_B_values = range(26)

# Try all combinations of A and B
for A in possible_A_values:
    for B in possible_B_values:
        encrypted_text = encrypt_with_params(key, A, B)
        
        # This is the text to use in the server interaction:
        print(f"Try with A = {A}, B = {B}, Encrypted text: {encrypted_text}")
