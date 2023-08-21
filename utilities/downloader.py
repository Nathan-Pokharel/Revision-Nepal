import urllib.request
import os
import re
from urllib.parse import urlparse, unquote

# List of base URLs you want to scrape
base_urls = [
        'https://papers.gceguide.com/A%20Levels/Chemistry%20(9701)/',
        'https://papers.gceguide.com/A%20Levels/Computing%20(9691)/',
        ]

def find_and_download_papers(base_url):
    Years = {}

    def find_Years():
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        request = urllib.request.Request(base_url, headers=headers)
        response = urllib.request.urlopen(request)
        html_content = response.read().decode('utf-8')

        pattern = r'<a href="(\d{4})" class="name">'
        matches = re.findall(pattern, html_content)
        for match in matches:
            year_path = base_url + match + "/"
            Years[match] = find_Files(year_path)

    def find_Files(url):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html_content = response.read().decode('utf-8')

        filename_pattern = r'<a href="(\d{4}_\w+\.pdf)" class="name">'
        filename_matches = re.findall(filename_pattern, html_content)

        return filename_matches

    def downloader(year, path, folder_name):
        download_url = base_url + year + "/" + path
        download_path = os.path.join("static", "files", folder_name.replace('/', os.sep), year)
        os.makedirs(download_path, exist_ok=True)

        if re.search(r'_ms_', path):
            download_path = os.path.join(download_path, "ms")
            os.makedirs(download_path, exist_ok=True)

        full_download_path = os.path.join(download_path, path)
        print(f"Downloading: {download_url} to {full_download_path}")

        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        with urllib.request.urlopen(urllib.request.Request(download_url, headers=headers)) as response, open(full_download_path, 'wb') as out_file:
            out_file.write(response.read())

    find_Years()

    url_path = urlparse(base_url).path
    folder_name = unquote(url_path.split('/')[-2]).replace(' ', '_').replace('(', '').replace(')', '')

    for year, paths in Years.items():
        for path in paths:
            downloader(year, path, folder_name)

# Loop through each base URL and call the find_and_download_papers function
for base_url in base_urls:
    find_and_download_papers(base_url)

