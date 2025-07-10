import re

pgn_text = r"""
[Event "?"]
[Site "?"]
[Date "????.??.??"]
[Round "?"]
[White "?"]
[Black "?"]
[Result "*"]

1. b3 e5 2. d3 d6 3. c4 Qd7 4. h4 a6 5. Qc2 Ne7 6. Kd1 Kd8 7. h5 Qa4 8. Rh4 b6
9. Nf3 h6 10. Rh2 a5 11. Nxe5 Qb5 12. d4 Ra7 13. Nd7 c5 14. d5 f6 15. Qf5 Rc5
16. Qg4 Bxd7 17. Qf5 Qb4 18. Qxf6 Ba4 19. Qxg7 Kc8 20. f3 Bb5 21. Rh3 Qd2+ 22.
Bxd2 Rd7 23. Qf7 Rd8 24. g4 Kc7 25. cxb5 Bg7 26. Rh4 Bd4 27. Qxe7+ Nd7 28. Qe6
Bxa1 29. Bh3 Bb2 30. Qxd7+ Kb8 31. a3 Bc3 32. Be3 Be5 33. Qh7 Bf4 34. Qc2 Rhe8
35. Bd4 Kc7 36. Bf1 Re5 37. Qa2 Rh8 38. Qa1 Bg5 39. Rh3 Re7 40. Bg2 Kb8 41. Rh1
Be3 42. Bxe3 Rg7 43. Bh3 Rgh7 44. f4 Ra7 45. Rf1 Rf8 46. Qh8 Re7 47. Rh1 Re5 48.
Qh7 Re4 49. a4 Rd4+ 50. Kc2 Rd8 51. Qh8 Rxf4 52. Bg1 Kc7 53. Qe8 Kb8 54. Qd7
Rxg4 55. Be3 Rf4 56. Bd4 c4 57. Rd1 Rh4 58. Bc3 Rxh3 59. Rg1 Rxc3+ 60. Kb2 Rh8
61. Ka2 Rd8 62. Kb2 Rc1 63. Qh3 Rc3 64. Qg4 Kb7 65. Rg2 Rg3 66. Qe4 Re3 67. Rf2
Rh8 68. b4 Rg3 69. Rf3 Rg1 70. Qe6 Rg2 71. Rf4 Ka8 72. Qe7 Rh2 73. Qe6 Rb8 74.
Qe3 Rb7 75. Qg3 Rg2 76. Qxh2 Rg2 77. Rg4 Rxh2 78. Nc3 Kb7 79. bxa5 Rh4 80. Rxh4
Kc7 81. Rh1 bxa5 82. Re1 Kb8 83. Rb1 Kc7 84. Rg1 Kd8 85. Ka2 Ke7 86. Re1 Kf6 87.
Ka1 Ke7 88. Rh1 Kd8 *
497
""".strip()

# 1. Extract all move tokens from the PGN (like 'b3', 'e5', 'Nf3', etc.).
#    Typically, PGN moves appear after digits like "1." or "1...".
#    We'll do a simple regex that grabs tokens that are NOT whitespace and not punctuation fields:
#    We only want the actual moves, ignoring PGN tags [Event "..."] etc.

# A quick approach: find lines AFTER the 7th bracket or so, or after some line that starts with a digit.
# We'll do a naive approach: we'll just skip lines with bracket, skip lines with '*', skip "497", skip numeric lines, etc.

lines = pgn_text.splitlines()
move_tokens = []

for line in lines:
    # Skip bracket lines or the final "497" line
    if line.startswith("[") or line.endswith("]"):
        continue
    if "Result" in line:
        continue
    if line.strip() == "*" or line.strip() == "497":
        continue
    # Now parse potential moves
    # We'll split by whitespace
    parts = line.split()
    # Filter out move numbers like "1.", "2.", "10."
    for part in parts:
        # If it's something like "1." or "2." or "..." skip
        if part.replace('.', '').isdigit():
            continue
        move_tokens.append(part)

# At this point, move_tokens might contain: ['b3', 'e5', 'd3', 'd6', 'c4', 'Qd7', ...]

# 2. Convert each move token to a 2-char square (if possible).
#    We'll ignore piece letters (Nf3 -> f3, Qc2-> c2, etc.).
#    Also ignore check symbols (+), captures (x), or suffixes (#). 
#    We'll just attempt to parse the last 2 chars if they look like file+rank.

def square_to_num(sq):
    """
    Convert a 2-char square like 'a1', 'h8' to an integer in [0..63],
    using file a=0..h=7, rank 1=0..8=7 => ID = 8*rank + file.
    Return None if invalid.
    """
    file_char = sq[0]
    rank_char = sq[1]
    file_val = ord(file_char) - ord('a')  # a->0,...,h->7
    rank_val = ord(rank_char) - ord('1')  # 1->0,...,8->7
    if 0 <= file_val < 8 and 0 <= rank_val < 8:
        return 8*rank_val + file_val
    return None

squares = []  # list of 6-bit numbers

for move in move_tokens:
    # strip off leading piece letters
    # possible piece letters: Q, K, R, B, N
    # also possible disambiguations like "Nxe5"? We'll just grab the last 2 letters if they look like a file/rank
    candidate = move[-2:]  # e.g. "f3" if "Nf3"
    sq_id = square_to_num(candidate)
    if sq_id is not None:
        squares.append(sq_id)

# Now we have a bunch of integer squares in [0..63]. Let's pack them into bits.

bitstring = ""
for sq in squares:
    # convert sq to a 6-bit binary string
    b6 = format(sq, '06b')  # 6-bit
    bitstring += b6

# The puzzle might have leftover bits if the total isn't multiple of 8. We'll see.
# Let's see how many bits we have:
num_bits = len(bitstring)
print(f"Extracted {len(squares)} squares, total {num_bits} bits.")

# We'll decode in 8-bit chunks:
message_bytes = []
for i in range(0, num_bits, 8):
    chunk = bitstring[i:i+8]
    if len(chunk) < 8:
        # leftover <8 bits, ignore or pad with zeros if needed
        break
    val = int(chunk, 2)
    message_bytes.append(val)

decoded = "".join(chr(b) for b in message_bytes)

print("Decoded ASCII (best guess):")
print(repr(decoded))
