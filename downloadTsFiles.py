import os
import requests

def download_ts_files(count, m3u8_file_url, base_ts_url, output_dir) -> None:
    # Create output directory
    while os.path.exists(output_dir + "%d" % count):
        count += 1
    output_dir = output_dir + "%d" % count
    os.makedirs(output_dir)

    # Fetch m3u8 file content
    response = requests.get(m3u8_file_url)
    if response.status_code != 200:
        print(f"Failed to fetch m3u8 file from {m3u8_file_url}")
        return

    m3u8_content = response.text.split('\n')

    # Extract video file names
    ts_files = [line.split(',')[-1] for line in m3u8_content if line.endswith('.ts')]

    # Download each ts file
    for ts_file in ts_files:
        ts_url = base_ts_url.replace('*', ts_file)
        output_path = os.path.join(output_dir, ts_file)
        
        print(f"Downloading {ts_url} to {output_path}")
        
        # Download the file
        response = requests.get(ts_url)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {ts_file}")
        else:
            print(f"Failed to download {ts_file}")

    if os.path.exists(output_dir + '/intro.ts'):
        os.remove(output_dir + '/intro.ts')

if __name__ == "__main__":
    count = 1
    m3u8_file_url = "LINK"
    base_ts_url = "LINK"
    output_dir = "./downloaded_ts_files/"

    download_ts_files(count, m3u8_file_url, base_ts_url, output_dir)
