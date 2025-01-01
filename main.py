from flask import Flask, request, render_template, redirect, url_for, send_from_directory, send_file
import os
import pandas as pd

import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        uniq = request.form.get('unique')
        if file.filename == '':
            return redirect(request.url)
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            subprocess_string = "grep -i -o '[A-Z0-9._%+-]\+@[A-Z0-9.-]\+\.[A-Z]\{2,4\}' {filepath} > emails.csv"
            if uniq:
                subprocess_string = "grep -i -o '[A-Z0-9._%+-]\+@[A-Z0-9.-]\+\.[A-Z]\{2,4\}' {filepath} | sort --unique > emails.csv"
            subprocess.call(subprocess_string, shell=True)
            # data = pd.read_csv(filepath)
            return send_file('/Users/kloppyklops/Desktop/datamate/emails.csv')
    
        else:
            return 'invalid file format. please upload a CSV file.'
        
    return 'something went wrong :('

if __name__ == '__main__':
    app.run(debug=True, port=5000)