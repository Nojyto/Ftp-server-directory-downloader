import wget
import os
import shutil

base_url = "<insert url>"
output_dir = "output/"

if __name__ == "__main__":
    if os.path.exists(output_dir):
        try:
            shutil.rmtree(output_dir)
        except OSError as e:
            raise Exception(f"Error: {e.filename} - {e.strerror}")
    os.makedirs(output_dir)

    
    print(f"Starting download of {base_url}")
    file_list = wget.download(base_url, output_dir)
    with open(file_list, "r") as files:
        for i, file in enumerate(files, 1):
            print(f"\n[{i:02}] {file}", end='')
            wget.download(base_url + file.split(" ")[-1], output_dir)
            print("\n", end='')
            
    if os.path.exists(file_list):
        os.remove(file_list)