from src.acquisition import create_disk_image, capture_memory_dump
from src.analysis import analyze_file_system
from src.reporting import generate_report
from src.utils import calculate_hash

# Step 1: Acquire Data
create_disk_image('/dev/sda', 'disk_image.dd')
capture_memory_dump('memory_dump.bin')

# Step 2: Analyze Data
analyze_file_system('disk_image.dd')

# Step 3: Generate Report
sample_data = {
    "files": [
        {"name": "example.txt", "size": 1024, "created": "2024-01-01"},
        {"name": "image.jpg", "size": 2048, "created": "2024-02-01"}
    ]
}
generate_report(sample_data, 'report_template.html', 'report.html')
