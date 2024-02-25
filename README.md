# Program: TS Files Downloader and Merger

This Python program is designed to download and merge TS (MPEG transport stream) files from a list of URLs specified in a file. The program is particularly useful for scenarios where you need to download video content split into multiple TS files (e.g., HLS streaming) and merge them into a single video file.

## Features

- **Download TS Files**: The program reads a list of URLs from a file (`urls.txt`) and downloads the corresponding TS files.

- **Merge TS Files**: After downloading the TS files, the program merges them into a single .mp4 video file using the FFmpeg utility.

- **Track Downloaded URLs**: The program keeps track of the downloaded URLs to avoid re-downloading the same files in subsequent runs.

## Usage

1. **Installation**

   - Remember FFmpeg is required for the program to merge. Installation guide can be found [here](https://www.ffmpeg.org/download.html)

   - Clone the repository to your local machine:

     ```
     git clone https://github.com/dopaminehighh/m3u8Download.git
     ```

   - Install the required dependencies using pip:

     ```
     pip install -r requirements.txt
     ```

3. **Configuration**

   - Edit the FFmpeg path to your path, or make it a blank string ('') if is installed into the system

   - Populate the `urls.txt` file with the URLs of the TS files you want to download and merge.

4. **Execution**

   - Run the program using Python:

     ```
     python3 main.py
     ```

   - The program will download the TS files from the URLs specified in `urls.txt`, merge them into a single video file, and store the merged file in the specified output directory.

## Dependencies

- `python-dotenv`: For loading environment variables from the `.env` file.
- `ffmpeg`: For merging TS files into a single video file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


