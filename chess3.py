# def square_to_index(square):
#     file = square[0].lower()
#     rank = square[1]
#     file_num = ord(file) - ord('a')
#     rank_num = int(rank) - 1
#     return rank_num * 8 + file_num

# moves = [
#     'b3', 'e5', 'd3', 'd6', 'c4', 'Qd7', 'h4', 'a6', 'Qc2', 'Ne7', 'Kd1', 'Kd8', 'h5', 'Qa4', 'Rh4', 'b6',
#     'Nf3', 'h6', 'Rh2', 'a5', 'Nxe5', 'Qb5', 'd4', 'Ra7', 'Nd7', 'c5', 'd5', 'f6', 'Qf5', 'Rc7', 'Qg4', 'Bxd7',
#     'Qf5', 'Qb4', 'Qxf6', 'Ba4', 'Qxg7', 'Kc8', 'f3', 'Bb5', 'Rh3', 'Qd2+', 'Bxd2', 'Rd7', 'Qf7', 'Rd8', 'g4',
#     'Kc7', 'cxb5', 'Bg7', 'Rh4', 'Bd4', 'Qxe7+', 'Nd7', 'Qe6', 'Bxa1', 'Bh3', 'Bb2', 'Qxd7+', 'Kb8', 'a3', 'Bc3',
#     'Be3', 'Be5', 'Qh7', 'Bf4', 'Qc2', 'Rhe8', 'Bd4', 'Kc7', 'Bf1', 'Re5', 'Qa2', 'Rh8', 'Qa1', 'Bg5', 'Rh3',
#     'Re7', 'Bg2', 'Kb8', 'Rh1', 'Be3', 'Bxe3', 'Rg7', 'Bh3', 'Rgh7', 'f4', 'Ra7', 'Rf1', 'Rf8', 'Qh8', 'Re7',
#     'Rh1', 'Re5', 'Qh7', 'Re4', 'a4', 'Rd4+', 'Kc2', 'Rd8', 'Qh8', 'Rxf4', 'Bg1', 'Kc7', 'Qe8', 'Kb8', 'Qd7',
#     'Rxg4', 'Be3', 'Rf4', 'Bd4', 'c4', 'Rd1', 'Rh4', 'Bc3', 'Rxh3', 'Rg1', 'Rxc3+', 'Kb2', 'Rh8', 'Ka2', 'Rd8',
#     'Kb2', 'Rc1', 'Ka2', 'Rc3', 'Qh3', 'Rxc3', 'Kb2', 'Rg3', 'Qe4', 'Re3', 'Rf2', 'Rh8', 'Rg2', 'Rg3', 'Rf4',
#     'Ka8', 'Qe6', 'Re3', 'Rf3', 'Rg1', 'Qe7', 'Rh2', 'Qe6', 'Rb8', 'Qe3', 'Rb7', 'Qg3', 'Rg7', 'Qxh2', 'Rg2',
#     'Rg4', 'Rxh2', 'Nc3', 'Kb7', 'bxa5', 'Rh4', 'Rxh4', 'Kc7', 'Rh1', 'bxa5', 'Re1', 'Kb8', 'Rb1', 'Kc7', 'Rg1',
#     'Kd8', 'Ka2', 'Re1', 'Kd8', 'Ka1', 'Rh1', 'Ke7'
# ]

# binary_str = []
# for move in moves:
#     # Extract the square part (e.g., 'e5' from 'Nxe5' or 'd7' from 'Qd7')
#     filtered = ''.join(c for c in move if c.isalnum())
#     square = filtered[-2:]  # Get last two alphanumeric chars (destination square)
#     # Handle edge cases like 'a4' where the square is correct
#     if len(square) == 2 and square[0].isalpha() and square[1].isdigit():
#         try:
#             index = square_to_index(square)
#             binary_str.append(f"{index:06b}")  # Ensure 6-bit binary
#         except:
#             continue

# # Concatenate all binary and split into bytes
# full_binary = ''.join(binary_str)
# bytes_list = [full_binary[i:i+8] for i in range(0, len(full_binary), 8)]
# bytes_list = [b for b in bytes_list if len(b) == 8]  # Ensure full bytes

# # Convert to bytes
# flag_bytes = bytes(int(byte, 2) for byte in bytes_list)

# # Search for the flag pattern 'RS{' in the bytes
# flag = ""
# for i in range(len(flag_bytes)):
#     # Check if current and next bytes form 'RS{'
#     if flag_bytes[i:i+3] == b'RS{':
#         # Capture until '}' is found
#         end = flag_bytes.find(b'}', i)
#         if end != -1:
#             flag = flag_bytes[i:end+1].decode('latin-1')
#             break

# print(f"Flag: {flag}")


def square_to_index(square):
    file = square[0].lower()
    rank = square[1]
    return (int(rank) - 1) * 8 + (ord(file) - ord('a'))

moves = [
    'b3', 'e5', 'd3', 'd6', 'c4', 'Qd7', 'h4', 'a6', 'Qc2', 'Ne7', 'Kd1', 'Kd8', 'h5', 'Qa4', 'Rh4', 'b6',
    'Nf3', 'h6', 'Rh2', 'a5', 'Nxe5', 'Qb5', 'd4', 'Ra7', 'Nd7', 'c5', 'd5', 'f6', 'Qf5', 'Rc7', 'Qg4', 'Bxd7',
    'Qf5', 'Qb4', 'Qxf6', 'Ba4', 'Qxg7', 'Kc8', 'f3', 'Bb5', 'Rh3', 'Qd2+', 'Bxd2', 'Rd7', 'Qf7', 'Rd8', 'g4',
    'Kc7', 'cxb5', 'Bg7', 'Rh4', 'Bd4', 'Qxe7+', 'Nd7', 'Qe6', 'Bxa1', 'Bh3', 'Bb2', 'Qxd7+', 'Kb8', 'a3', 'Bc3',
    'Be3', 'Be5', 'Qh7', 'Bf4', 'Qc2', 'Rhe8', 'Bd4', 'Kc7', 'Bf1', 'Re5', 'Qa2', 'Rh8', 'Qa1', 'Bg5', 'Rh3',
    'Re7', 'Bg2', 'Kb8', 'Rh1', 'Be3', 'Bxe3', 'Rg7', 'Bh3', 'Rgh7', 'f4', 'Ra7', 'Rf1', 'Rf8', 'Qh8', 'Re7',
    'Rh1', 'Re5', 'Qh7', 'Re4', 'a4', 'Rd4+', 'Kc2', 'Rd8', 'Qh8', 'Rxf4', 'Bg1', 'Kc7', 'Qe8', 'Kb8', 'Qd7',
    'Rxg4', 'Be3', 'Rf4', 'Bd4', 'c4', 'Rd1', 'Rh4', 'Bc3', 'Rxh3', 'Rg1', 'Rxc3+', 'Kb2', 'Rh8', 'Ka2', 'Rd8',
    'Kb2', 'Rc1', 'Ka2', 'Rc3', 'Qh3', 'Rxc3', 'Kb2', 'Rg3', 'Qe4', 'Re3', 'Rf2', 'Rh8', 'Rg2', 'Rg3', 'Rf4',
    'Ka8', 'Qe6', 'Re3', 'Rf3', 'Rg1', 'Qe7', 'Rh2', 'Qe6', 'Rb8', 'Qe3', 'Rb7', 'Qg3', 'Rg7', 'Qxh2', 'Rg2',
    'Rg4', 'Rxh2', 'Nc3', 'Kb7', 'bxa5', 'Rh4', 'Rxh4', 'Kc7', 'Rh1', 'bxa5', 'Re1', 'Kb8', 'Rb1', 'Kc7', 'Rg1',
    'Kd8', 'Ka2', 'Re1', 'Kd8', 'Ka1', 'Rh1', 'Ke7'
]

# Extract destination squares robustly
binary_str = []
for move in moves:
    # Remove non-alphanumeric characters (e.g., '+', 'x', '#')
    clean_move = ''.join([c for c in move if c.isalnum()])
    # Find the destination square (last 2 characters, e.g., 'e5' in 'Nxe5')
    if len(clean_move) >= 2:
        square = clean_move[-2:]
        if square[0].isalpha() and square[1].isdigit():
            try:
                index = square_to_index(square)
                binary_str.append(f"{index:06b}")  # 6-bit binary
            except:
                continue

# Concatenate binary and split into 8-bit bytes
full_binary = ''.join(binary_str)
# Truncate to ensure length is a multiple of 8
full_binary = full_binary[:len(full_binary)//8 * 8]

# Convert to bytes
flag_bytes = bytes(int(full_binary[i:i+8], 2) for i in range(0, len(full_binary), 8))

# Search for "RS{" in the byte stream
flag = ""
for i in range(len(flag_bytes) - 3):
    if flag_bytes[i:i+3] == b'RS{':
        end = flag_bytes.find(b'}', i)
        if end != -1:
            flag = flag_bytes[i:end+1].decode('utf-8', errors='ignore')
            break

print(f"Flag found: {flag}")