***REMOVED***
import re
import subprocess

def natural_sort_key(s):
    # Split the filename into non-digit and digit parts
    parts = re.split(r'(\d+)', s)
    # Convert the digit parts to integers and keep the non-digit parts as strings
    return [int(part) if part.isdigit() else part for part in parts]

def merge_ts_files(input_dir, output_file, ffmpeg_path) -> None:
    # List all .ts files in the input directory and sort them
    ts_files = sorted([file for file in os.listdir(input_dir) if file.endswith('.ts')], key=natural_sort_key)

    # Generate a text file listing all .ts files
    with open('input.txt', 'w') as f:
    ***REMOVED***
            f.write(f"file '{os.path.join(input_dir, ts_file)}'\n")

    # Run ffmpeg command to merge the .ts files
    command = ['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'input.txt','-vsync', '1', '-r', '30', '-c:v', 'libx265', '-crf', '28', '-preset', 'medium', '-c:a', 'copy', output_file]
    subprocess.run(command)

    # Clean up temporary files
    os.remove('input.txt')

***REMOVED***
***REMOVED***
    input_dir = "downloaded_ts_files/"
    output_file = "merged_video*.mp4"
    ffmpeg_path = "" 

    while os.path.exists(input_dir + "%d" % count):
        input_dir_merge = input_dir + "%d" % count
        output_file_merge = output_file.replace("*", "%d" % count)
***REMOVED***
        with open("mergedVideos.txt", "r+") as merged:
            if output_file_merge in merged.read():
                continue
            merged.write(output_file_merge)
        merge_ts_files(input_dir_merge, output_file_merge, ffmpeg_path)