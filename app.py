# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")

def load_form():
    return render_template('upload.html')
# Write load_form function below to Open and redirect to default upload webpage
@app.route('/', methods=['POST'])
def upload_image():
    file = request.file['file']
    filename = secure_filename(file.filename)
    file.save(os.path.jion('static/',filename))

    display_message = 'Image sucessfully upload ad display below'
    return render_template('upload.html', filename=filename, message = display_message)

@app.route('display/<filename>')
def display_message(filename):
    return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run()