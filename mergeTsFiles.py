import os
import subprocess

def merge_ts_files(input_dir, output_file, ffmpeg_path) -> None:
    # List all .ts files in the input directory
    ts_files = [file for file in os.listdir(input_dir) if file.endswith('.ts')]

    # Generate a text file listing all .ts files
    with open('input.txt', 'w') as f:
        for ts_file in sorted(ts_files):
            f.write(f"file '{os.path.join(input_dir, ts_file)}'\n")

    # Run ffmpeg command to merge the .ts files
    command = [os.path.join(ffmpeg_path, 'ffmpeg'), '-y', '-f', 'concat', '-safe', '0', '-i', 'input.txt', '-c', 'copy', output_file]
    subprocess.run(command)

    # Clean up temporary files
    os.remove('input.txt')

if __name__ == "__main__":
    count = 1
    input_dir = "downloaded_ts_files/"
    output_file = "merged_video.mp4"
    ffmpeg_path = "ffmpeg-6.1-amd64-static/"

    while os.path.exists(input_dir + "%d" % count):
        input_dir_merge = input_dir + "%d" % count
        output_file_merge = output_file.replace("*", "%d" % count)
        count += 1
        with open("mergedVideos.txt", "r+") as merged:
            if output_file_merge in merged.read():
                continue
            merged.write(output_file_merge)
        merge_ts_files(input_dir_merge, output_file_merge, ffmpeg_path)