import pytsk3
import datetime

def analyze_file_system(image_path):
    img = pytsk3.Img_Info(image_path)
    fs = pytsk3.FS_Info(img)

    for directory in fs.open_dir(path="/"):
        for entry in directory:
            if entry.info.name.name in [b'.', b'..']:
                continue
            print(f"Name: {entry.info.name.name.decode('utf-8')}")
            print(f"Size: {entry.info.meta.size}")
            print(f"Created: {datetime.datetime.utcfromtimestamp(entry.info.meta.crtime)}")
            print(f"Modified: {datetime.datetime.utcfromtimestamp(entry.info.meta.mtime)}")
            print("-----")

# Example usage
if __name__ == "__main__":
    analyze_file_system('disk_image.dd')
