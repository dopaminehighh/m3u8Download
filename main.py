import os
from dotenv import load_dotenv
import downloadTsFiles
import mergeTsFiles
import fileinput

def main():
    load_dotenv()  # Load variables from .env file

    # Read URLs from a file
    with open("urls.txt", "r") as file:
        urls = file.readlines()
    
    downloaded = open(os.getenv("DOWNLOADED_URLS"), "r+")

    for url in urls:
        downloaded.seek(0)
        if url in downloaded.read():
            continue
        print("Extracting from", url, "\n")
        count = 1
        m3u8_file_url = url.strip()
        base_ts_url = "/".join(m3u8_file_url.split("/")[:-1]) + "/*"
        output_dir = os.getenv("OUTPUT_DIR")

        downloadTsFiles.download_ts_files(count, m3u8_file_url, base_ts_url, output_dir)

        input_dir = os.getenv("INPUT_DIR")
        output_file = os.getenv("OUTPUT_FILE")
        ffmpeg_path = os.getenv("FFMPEG_PATH") # change to blank string if installed on system

        while os.path.exists(input_dir + "%d" % count):
            input_dir_merge = input_dir + "%d" % count
            output_file_merge = output_file.replace("*", "%d" % count)
            count += 1
            with open(os.getenv("MERGED_VIDEOS"), "r+") as merged:
                if output_file_merge in merged.read():
                    continue
                merged.write("output_file_merge")
            mergeTsFiles.merge_ts_files(input_dir_merge, output_file_merge, ffmpeg_path)
            
        # Remove the processed URL from urls.txt
        with fileinput.FileInput("urls.txt", inplace=True) as file:
            for line in file:
                if line.strip() != url.strip():
                    print(line, end='')
    
        downloaded.write("\n" + url)

    downloaded.close()

if __name__ == "__main__":
    main()
