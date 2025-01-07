import json

def parse_large_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as output:
        for line in file:
            data = json.loads(line)
            for key, value in data.items():
                if any(kw in key.lower() or kw in str(value).lower() for kw in ["flag", "password", "key", "secret"]):
                    output.write(f"Potential flag in {key}: {value}\n")

parse_large_json('./SI/project.json')
