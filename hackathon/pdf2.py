# import base64
# import re

# def crack_serialized_obj_from_file(file_path):
#     try:
#         # Read file in binary mode to avoid encoding issues
#         with open(file_path, "rb") as f:
#             content = f.read()
#         # Decode content using ASCII and ignore errors (removes BOM and other non-ASCII bytes)
#         text = content.decode("ascii", errors="ignore")
        
#         # Split into lines and clean each line
#         lines = text.splitlines()
#         cleaned_parts = []
#         for line in lines:
#             line = line.strip()
#             # Remove a trailing semicolon, if present
#             if line.endswith(";"):
#                 line = line[:-1]
#             # Remove surrounding quotes if present
#             if line.startswith('"') and line.endswith('"'):
#                 line = line[1:-1]
#             # Remove a trailing plus sign, if present
#             if line.endswith("+"):
#                 line = line[:-1]
#             cleaned_parts.append(line)
        
#         # Join all parts to form the complete Base64 string
#         base64_str = "".join(cleaned_parts)
#         print("Combined Base64 string (first 200 characters):")
#         # print(base64_str)
        
#         # Decode the Base64 string
#         decoded = base64.b64decode(base64_str)
#         print("\n=== Decoded Serialized Object (first 200 bytes in hex) ===")
#         print(decoded[:200])
        
#         # Search for flag pattern
#         flags = re.findall(b"MetaCTF\{.*?\}", decoded)
#         if flags:
#             print("\n=== Flag(s) found ===")
#             for flag in flags:
#                 print(flag.decode('utf-8'))
#         else:
#             print("\nNo flag found in the decoded serialized object.")
#     except Exception as e:
#         print("Error decoding serialized object:", e)

# if __name__ == '__main__':
#     file_path = input("Enter the path to the text file containing the serialized object: ").strip()
#     crack_serialized_obj_from_file(file_path)


import base64
import re

def crack_serialized_obj_from_file(file_path):
    try:
        # Read file in binary mode to avoid encoding issues
        with open(file_path, "rb") as f:
            content = f.read()
        # Decode content using ASCII and ignore non-ASCII bytes (removes BOM/artifacts)
        text = content.decode("ascii", errors="ignore")
        
        # Split into lines and clean each line
        lines = text.splitlines()
        cleaned_parts = []
        for line in lines:
            line = line.strip()
            # Remove trailing semicolon if present
            if line.endswith(";"):
                line = line[:-1]
            # Remove surrounding quotes if present
            if line.startswith('"') and line.endswith('"'):
                line = line[1:-1]
            # Remove trailing concatenation symbols if present
            if line.endswith("+"):
                line = line[:-1]
            cleaned_parts.append(line)
        
        # Join all parts to form the complete Base64 string
        base64_str = "".join(cleaned_parts)
        print("Combined Base64 string (first 200 characters):")
        print(base64_str[:200])
        
        # Decode the Base64 string
        decoded = base64.b64decode(base64_str)
        print("\n=== Decoded Serialized Object (all bytes in hex) ===")
        print(decoded.hex())
        
        # Search for flag pattern (MetaCTF{...})
        flags = re.findall(b"MetaCTF\{.*?\}", decoded)
        if flags:
            print("\n=== Flag(s) found ===")
            for flag in flags:
                print(flag.decode('utf-8'))
        else:
            print("\nNo flag found in the decoded serialized object.")
    except Exception as e:
        print("Error decoding serialized object:", e)

if __name__ == '__main__':
    file_path = input("Enter the path to the text file containing the serialized object: ").strip()
    crack_serialized_obj_from_file(file_path)
