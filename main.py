from flask import Flask, request, render_template, redirect, url_for
import os
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        data = pd.read_csv(filepath)
        # Process the CSV data as needed
        return 'file {} uploaded successfully'.format(file.filename)
    else:
        return 'invalid file format. please upload a CSV file.'

if __name__ == '__main__':
    app.run(debug=True, port=5000)