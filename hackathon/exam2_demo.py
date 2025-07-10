#!/usr/bin/env python3
import sys

#python3 exam2_demo.py C.txt D.txt

def read_data(filename):
    #returns a list of tuples: [(x1, y1), (x2, y2), ...].
    
    data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            x_str, y_str = line.split(',')
            x, y = float(x_str), float(y_str)
            data.append((x, y))
    return data

def compute_smallest_addition(list_c, list_d):
    #For each point in list_c, find the point in list_d with closest X val
    #Returns a list of tuples: [(best_match_index_in_list_d, sum_of_those_x_values), ...]
    results = []
    for c_x, c_y in list_c:
        min_diff = float('inf')
        min_index = -1

        for idx_d, (d_x, d_y) in enumerate(list_d):
            diff = abs(c_x - d_x)
            if diff < min_diff:
                min_diff = diff
                min_index = idx_d

        # x-coord of c plus the x-coord of the found point in d
        sum_of_x = c_x + list_d[min_index][0]
        results.append((min_index, sum_of_x))

    return results

def main():
    if len(sys.argv) != 3:
        print("Usage: exam2_demo.py <file_C> <file_D>")
        sys.exit(1)
    c_file = sys.argv[1]
    d_file = sys.argv[2]
    c_data = read_data(c_file)
    d_data = read_data(d_file)
    results = compute_smallest_addition(c_data, d_data)

    for i, (closest_idx, addition) in enumerate(results):
        c_x, c_y = c_data[i]
        d_x, d_y = d_data[closest_idx]
        print(
            f"The smallest addition of the X position of point C[{i}] "
            f"(({c_x}, {c_y})) is D[{closest_idx}] "
            f"(({d_x}, {d_y})). Addition = {addition}"
        )

if __name__ == "__main__":
    main()
