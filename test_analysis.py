import unittest
from src.analysis import analyze_file_system
import pytsk3

class MockFSInfo(pytsk3.FS_Info):
    # Mocked FS_Info class for testing without real disk images
    pass

class TestAnalysis(unittest.TestCase):
    
    def test_analyze_file_system(self):
        # Mocking FS_Info object for testing
        image_path = 'test_disk_image.dd'
        fs_info = MockFSInfo(image_path)
        result = analyze_file_system(fs_info)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
