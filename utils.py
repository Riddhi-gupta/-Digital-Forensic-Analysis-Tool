import hashlib

def calculate_hash(file_path, hash_type='sha256'):
    hash_func = getattr(hashlib, hash_type)()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# Example usage
if __name__ == "__main__":
    print(calculate_hash('example_file.txt'))
