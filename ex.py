#!/usr/bin/env python3

def solve_constraint1():
    """
    Constraint #1: (c1 ^ c2) + (c3 * c4) = 232
    c1..c4 in [0..255].
    We'll do a small optimization:
      - For c3 in [0..255], c4 in [0..255], compute p = c3*c4.
      - If p <= 232, then d = 232-p.
        For c1 in [0..255], we set c2 = c1 ^ d. That's a valid pair.
      - We'll just pick the first c1=0 => c2=d to satisfy.
    Return (c1, c2, c3, c4).
    """
    for c3 in range(256):
        for c4 in range(256):
            p = c3 * c4
            if p > 232:
                continue
            d = 232 - p
            if d < 0 or d > 255:
                continue
            # pick c1=0 => c2 = c1 ^ d = d
            c1 = 0
            c2 = d
            return (c1, c2, c3, c4)
    return None  # no solution found

def solve_constraint2():
    """
    Constraint #2: (c5^2 + c6) mod 256 = c7
    c5..c7 in [0..255].
    We'll brute force c5, c6 in [0..255], then c7 = (c5^2 + c6) mod 256.
    Return the first solution we find.
    """
    for c5 in range(256):
        for c6 in range(256):
            s = ( (c5*c5) + c6 ) % 256
            c7 = s
            return (c5, c6, c7)
    return None

def solve_constraint3():
    """
    Constraint #3: c8 + (c9 * c10) = (5*c11 + 10) mod 100
    We'll brute force c8..c11 in [0..255], but check the condition mod 100.
    Return the first solution.
    """
    for c8 in range(256):
        for c9 in range(256):
            for c10 in range(256):
                lhs = c8 + c9*c10
                for c11 in range(256):
                    rhs = (5*c11 + 10) % 100
                    if lhs == rhs:
                        return (c8, c9, c10, c11)
    return None

def solve_constraint4():
    """
    Constraint #4: (c12 ^ c13) + (c14 * c15) = 200
    We'll do a partial optimization:
      - For c14,c15 in [0..255], p = c14*c15.
      - If p <= 200, d = 200-p, then we want (c12 ^ c13)=d.
        We'll pick c12=0 => c13=d.
    """
    for c14 in range(256):
        for c15 in range(256):
            p = c14 * c15
            if p > 200:
                continue
            d = 200 - p
            if d >= 0 and d <= 255:
                c12 = 0
                c13 = d
                return (c12, c13, c14, c15)
    return None

def solve_constraint5():
    """
    Constraint #5: (c17 + c18) mod 37 = (c19 * c20) mod 90
    Brute force approach but with some mild pruning.
    """
    for c17 in range(256):
        for c18 in range(256):
            left = (c17 + c18) % 37
            for c19 in range(256):
                for c20 in range(256):
                    right = (c19 * c20) % 90
                    if left == right:
                        return (c17, c18, c19, c20)
    return None

def solve_constraint6():
    """
    Constraint #6: c21^2 + c22^2 = 250
    c21, c22 in [0..255]. We'll brute force squares.
    """
    # Precompute squares mod ??? Actually we want them in normal int range.
    # We want c21^2 + c22^2 = 250 in normal integer sense (0..65025).
    for c21 in range(256):
        sq1 = c21*c21
        for c22 in range(256):
            if sq1 + c22*c22 == 250:
                return (c21, c22)
    return None

def solve_constraint7():
    """
    Constraint #7: (c23 ^ (2*c24)) + (c25 mod 10) = 30
    We'll brute force c23..c25 in [0..255].
    Note that 2*c24 is in [0..510], we can do ^ with c23 in 0..255. We'll do direct approach.
    """
    for c23 in range(256):
        for c24 in range(256):
            double_c24 = 2*c24
            # XOR is bitwise in 8 bits, so we might need double_c24 % 256 or consider >255 values.
            # Typically (c23 ^ x) is done mod 256 if x < 256. But 2*c24 can exceed 255.
            # Let's interpret "bitwise XOR" with 2*c24 truncated to 8 bits => (2*c24) % 256
            # The puzzle wasn't super explicit, but that's typical for 8-bit logic.
            x = (double_c24 % 256)
            part = c23 ^ x
            for c25 in range(256):
                lhs = part + (c25 % 10)
                if lhs == 30:
                    return (c23, c24, c25)
    return None

def solve_constraint8():
    """
    Constraint #8: (c26 * c27) = (c28 ^ 20)
    We'll do a direct approach. c28 ^ 20 in [0..255], product in [0..65025].
    But we only compare in normal 8-bit sense? The puzzle says "The product
    of the 26th and 27th characters be equal to the bitwise XOR of the 28th char and 20."
    Usually that implies 8-bit product? It's ambiguous. We'll assume standard integer product
    but then it must be <256 to equal (c28 ^ 20) in [0..255].
    """
    for c26 in range(256):
        for c27 in range(256):
            prod = c26 * c27
            if prod > 255:
                continue
            for c28 in range(256):
                xor_val = c28 ^ 20
                if xor_val == prod:
                    return (c26, c27, c28)
    return None

def solve_constraint9():
    """
    Constraint #9: ((c29 + c30) ^ (c31 - c32)) = 15
    We'll brute force c29..c32 in [0..255], interpret the difference c31-c32 in normal integer.
    Then do a bitwise XOR in 8-bit context => we likely do ((c31-c32) mod 256).
    We'll assume we do (c31 - c32) mod 256 for the XOR. 
    i.e. x = (c31 - c32) % 256; then ( (c29 + c30) % 256 ) ^ x = 15.
    """
    for c29 in range(256):
        for c30 in range(256):
            sum_ = (c29 + c30) % 256
            for c31 in range(256):
                for c32 in range(256):
                    diff = (c31 - c32) % 256
                    if (sum_ ^ diff) == 15:
                        return (c29, c30, c31, c32)
    return None


def main():
    # Solve each constraint chunk once, picking the FIRST solution we find.
    chunk1 = solve_constraint1()
    if not chunk1:
        print("No solution found for constraint #1 with extended ASCII. Puzzle unsolvable.")
        return
    c1, c2, c3, c4 = chunk1

    chunk2 = solve_constraint2()
    if not chunk2:
        print("No solution for constraint #2.")
        return
    c5, c6, c7 = chunk2

    chunk3 = solve_constraint3()
    if not chunk3:
        print("No solution for constraint #3.")
        return
    c8, c9, c10, c11 = chunk3

    # c16 is not used. Let's pick 0:
    c16 = 0

    chunk4 = solve_constraint4()
    if not chunk4:
        print("No solution for constraint #4.")
        return
    c12, c13, c14, c15 = chunk4

    chunk5 = solve_constraint5()
    if not chunk5:
        print("No solution for constraint #5.")
        return
    c17, c18, c19, c20 = chunk5

    chunk6 = solve_constraint6()
    if not chunk6:
        print("No solution for constraint #6.")
        return
    c21, c22 = chunk6

    chunk7 = solve_constraint7()
    if not chunk7:
        print("No solution for constraint #7.")
        return
    c23, c24, c25 = chunk7

    chunk8 = solve_constraint8()
    if not chunk8:
        print("No solution for constraint #8.")
        return
    c26, c27, c28 = chunk8

    chunk9 = solve_constraint9()
    if not chunk9:
        print("No solution for constraint #9.")
        return
    c29, c30, c31, c32 = chunk9

    # Combine into a single 32-length array (1-based indexing):
    # We'll store them in a list but remember we've used 1-based naming. We'll just position them carefully:
    # Index:   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
    # Variable c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12 c13 c14 c15 c16 c17 c18 c19 c20 c21 c22 c23 c24 c25 c26 c27 c28 c29 c30 c31 c32
    result = [
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16,
        c17, c18, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32
    ]

    # Convert each byte to a character. Some might be non-printable or strange in extended ASCII.
    key_chars = "".join(chr(x) for x in result)

    print("Found a valid extended-ASCII solution!")
    print("32-byte array:", result)
    print("Key (raw extended ASCII):")
    print(repr(key_chars))

if __name__ == "__main__":
    main()
