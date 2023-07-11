from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['pdf']
    pdf_reader = PyPDF2.PdfFileReader(file)
    num_pages = pdf_reader.numPages

    return render_template('viewer.html', num_pages=num_pages)

if __name__ == '__main__':
    app.run(debug=True)
