#!/usr/bin/env python3

import string

def ascii_val(ch):
    """Return the ASCII integer of character ch."""
    return ord(ch)

def is_alphanumeric_ascii(ch):
    """
    Check if ch is an alphanumeric character in ASCII:
      '0'-'9', 'A'-'Z', or 'a'-'z'.
    """
    return ch.isalnum()

# Build a list of all alphanumeric ASCII chars.
alnum_chars = [chr(c) for c in range(128) if chr(c).isalnum()]

# We'll test ALL possible combinations of (c1, c2, c3, c4) from the alphanumeric set
# to see if (c1 ^ c2) + (c3 * c4) == 232.

valid_solutions = []

for c1 in alnum_chars:
    val1 = ascii_val(c1)
    for c2 in alnum_chars:
        val2 = ascii_val(c2)
        # XOR part:
        xor_val = val1 ^ val2

        # Now for c3 and c4, check product
        # But note: the smallest possible ASCII product among alnum chars is 48*48=2304
        # which already exceeds 232, so we *know* there's no solution.
        # We'll illustrate by brute-forcing anyway (though it yields no result).

        for c3 in alnum_chars:
            val3 = ascii_val(c3)
            for c4 in alnum_chars:
                val4 = ascii_val(c4)
                lhs = xor_val + (val3 * val4)
                if lhs == 232:
                    valid_solutions.append((c1, c2, c3, c4))

if valid_solutions:
    print("Found at least one solution to the first constraint!")
    for sol in valid_solutions:
        print(sol)
else:
    print("No solutions found for the first constraint. Puzzle is unsolvable under standard ASCII.")
