from flask import Flask, render_template,send_from_directory
from urllib.parse import unquote
import os

class FileStructure:
    def __init__(self):
        self.base_path = "static/files"
        self.path = self.base_path
        self.folders = []
        self.files = []
        self.sub_folders={}

    def get_directory_listing(self):
        items = os.listdir(self.path)
        for item in items:
            if os.path.isdir(os.path.join(self.path, item)):
                self.folders.append(item)
            elif os.path.isfile(os.path.join(self.path, item)):
                self.files.append(item)
        self.folders.sort(reverse=True)
        self.get_subfolders()

    def get_subfolders(self):
        for folder in self.folders:
            subfolder_path = os.path.join(self.path, folder)
            subfolders = [subfolder for subfolder in os.listdir(subfolder_path) if os.path.isdir(os.path.join(subfolder_path, subfolder))]
            subfolders.sort(reverse=True)  # Sort the subfolders
            self.sub_folders[folder] = subfolders

    def clearstructure(self):
        self.folders = []
        self.files = []
        self.sub_folders = {}


    def add_ms_tags(self):
        ms_folder = os.path.join(self.path, 'ms')
        ms_files = [file.replace("_qp_", "_ms_") for file in self.files]

        if not os.path.exists(ms_folder):
            for i,file in enumerate(self.files):
                self.files[i] = {"name":file,"tags":[""]}
        else:
            for i, file in enumerate(self.files):
                if ms_files[i] in os.listdir(ms_folder):
                    self.files[i] = {"name": file, "tags": ["has_ms"]}
                else:
                    self.files[i] = {"name": file, "tags": [""]}

app = Flask(__name__)
filestructure = FileStructure()

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/explore/')
@app.route('/explore/<path:folder>')
def explore(folder=None):
    if folder:
        filestructure.clearstructure()
        filestructure.path = os.path.join(filestructure.base_path, unquote(unquote(folder)))
        filestructure.get_directory_listing()
        filestructure.add_ms_tags()
    else:
        filestructure.clearstructure()
        filestructure.path = filestructure.base_path
        filestructure.get_directory_listing()
        filestructure.add_ms_tags()

    return render_template('directory.html', filestructure=filestructure)

@app.route('/download/<path:folder>/<path:file>')
def download_file(folder, file):
    file_path = os.path.join(filestructure.base_path, unquote(unquote(folder)), unquote(unquote(file)))
    return send_from_directory(os.path.dirname(file_path), os.path.basename(file_path), as_attachment=True)

if __name__ == '__main__':
    app.run()
