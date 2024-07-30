import argparse
from src.acquisition import create_disk_image, capture_memory_dump
from src.analysis import analyze_file_system
from src.reporting import generate_report
from src.utils import calculate_hash

def main():
    parser = argparse.ArgumentParser(description='Digital Forensic Analysis Tool')
    
    parser.add_argument('--acquire-disk', type=str, help='Path to the disk device (e.g., /dev/sda)')
    parser.add_argument('--acquire-memory', action='store_true', help='Flag to capture memory dump')
    parser.add_argument('--image-output', type=str, default='disk_image.dd', help='Output path for disk image')
    parser.add_argument('--memory-output', type=str, default='memory_dump.bin', help='Output path for memory dump')
    parser.add_argument('--analyze', type=str, help='Path to the disk image for analysis')
    parser.add_argument('--report', type=str, help='Output path for the generated report')
    parser.add_argument('--template', type=str, default='report_template.html', help='Path to the report template')
    parser.add_argument('--hash', type=str, help='File path to calculate hash')
    parser.add_argument('--hash-type', type=str, default='sha256', help='Type of hash function (md5, sha1, sha256)')
    
    args = parser.parse_args()
    
    if args.acquire_disk:
        print(f"Creating disk image from {args.acquire_disk}...")
        create_disk_image(args.acquire_disk, args.image_output)
        print(f"Disk image saved to {args.image_output}.")
    
    if args.acquire_memory:
        print("Capturing memory dump...")
        capture_memory_dump(args.memory_output)
        print(f"Memory dump saved to {args.memory_output}.")
    
    if args.analyze:
        print(f"Analyzing file system from image {args.analyze}...")
        analyze_file_system(args.analyze)
    
    if args.report:
        sample_data = {
            "files": [
                {"name": "example.txt", "size": 1024, "created": "2024-01-01"},
                {"name": "image.jpg", "size": 2048, "created": "2024-02-01"}
            ]
        }
        print(f"Generating report to {args.report} using template {args.template}...")
        generate_report(sample_data, args.template, args.report)
        print(f"Report saved to {args.report}.")
    
    if args.hash:
        print(f"Calculating {args.hash_type} hash for {args.hash}...")
        file_hash = calculate_hash(args.hash, args.hash_type)
        print(f"Hash: {file_hash}")

if __name__ == "__main__":
    main()
