import unittest
from src.utils import calculate_hash
import hashlib

class TestUtils(unittest.TestCase):
    
    def test_calculate_hash(self):
        # Create a test file
        file_path = 'test_file.txt'
        with open(file_path, 'w') as file:
            file.write('test content')
        
        expected_hash = hashlib.sha256(b'test content').hexdigest()
        calculated_hash = calculate_hash(file_path, 'sha256')
        self.assertEqual(expected_hash, calculated_hash)
        
        # Clean up
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
