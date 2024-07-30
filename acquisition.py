import os
import subprocess

def create_disk_image(disk_path, output_path):
    """
    Create a disk image using the dd command (Linux example).
    """
    command = ['dd', f'if={disk_path}', f'of={output_path}', 'conv=noerror,sync']
    subprocess.run(command)

def capture_memory_dump(output_path):
    """
    Capture memory dump (Linux example).
    """
    command = ['dd', 'if=/dev/mem', f'of={output_path}', 'bs=1M']
    subprocess.run(command)

# Example usage
if __name__ == "__main__":
    create_disk_image('/dev/sda', 'disk_image.dd')
    capture_memory_dump('memory_dump.bin')
