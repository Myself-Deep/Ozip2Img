import os
import shutil
import subprocess

def extract_ozip(ozip_path, extract_dir):
    """Extracts the contents of an Oppo OZIP file."""
    try:
        subprocess.run(['java', '-jar', 'ozipdecrypt.jar', ozip_path, extract_dir], check=True)
        print("OZIP extraction successful!")
    except subprocess.CalledProcessError as e:
        print("Error extracting OZIP:", e)

def create_ext4_image(input_dir, output_image):
    """Creates an Ext4 filesystem image from a directory."""
    try:
        subprocess.run(['mke2fs', '-t', 'ext4', '-d', input_dir, '-r', '/', '-L', 'EXT4_IMAGE', output_image], check=True)
        print("Ext4 image creation successful!")
    except subprocess.CalledProcessError as e:
        print("Error creating Ext4 image:", e)

def main():
    ozip_path = input("Enter the path to the Oppo OZIP file: ").strip()
    if not os.path.exists(ozip_path):
        print("Error: OZIP file not found.")
        return

    extract_dir = "ozip_extracted"
    os.makedirs(extract_dir, exist_ok=True)
    
    extract_ozip(ozip_path, extract_dir)

    output_image = input("Enter the path for the output Ext4 image: ").strip()
    create_ext4_image(extract_dir, output_image)

    shutil.rmtree(extract_dir)

if __name__ == "__main__":
    main()
