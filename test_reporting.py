import unittest
from src.reporting import generate_report
import os

class TestReporting(unittest.TestCase):
    
    def test_generate_report(self):
        sample_data = {
            "files": [
                {"name": "example.txt", "size": 1024, "created": "2024-01-01"},
                {"name": "image.jpg", "size": 2048, "created": "2024-02-01"}
            ]
        }
        template_path = 'test_report_template.html'
        output_path = 'test_report.html'
        
        # Creating a sample template for testing
        with open(template_path, 'w') as file:
            file.write('<html><body>{{ data }}</body></html>')
        
        generate_report(sample_data, template_path, output_path)
        self.assertTrue(os.path.exists(output_path))
        
        # Clean up
        os.remove(template_path)
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
