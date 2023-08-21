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
    print("Entered")
    if folder:
        filestructure.clearstructure()
        filestructure.path = os.path.join(filestructure.base_path, unquote(unquote(folder)))
        filestructure.get_directory_listing()
    else:
        filestructure.clearstructure()
        filestructure.path = filestructure.base_path
        filestructure.get_directory_listing()

    return render_template('directory.html', filestructure=filestructure)

@app.route('/download/<path:folder>/<path:file>')
def download_file(folder, file):
    file_path = os.path.join(filestructure.base_path, folder, file)
    print(file_path)
    return send_from_directory(filestructure.base_path, os.path.join(folder, file), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')

