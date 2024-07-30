import unittest
from src.acquisition import create_disk_image, capture_memory_dump
import os

class TestAcquisition(unittest.TestCase):
    
    def test_create_disk_image(self):
        # Simulate creating a disk image
        disk_path = '/dev/null'  # Using /dev/null for a safe test
        output_path = 'test_disk_image.dd'
        
        create_disk_image(disk_path, output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)

    def test_capture_memory_dump(self):
        # Simulate capturing a memory dump
        output_path = 'test_memory_dump.bin'
        
        capture_memory_dump(output_path)
        self.assertTrue(os.path.exists(output_path))
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
