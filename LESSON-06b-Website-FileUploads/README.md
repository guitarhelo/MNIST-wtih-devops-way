
# FilesUpload

Create new directory les06b  (under trg, since you want to use same venv)

## Step 1

Create app.py

    import os
    from flask import Flask, render_template, request
    from werkzeug import secure_filename

    UPLOAD_FOLDER = './uploads'

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    @app.route('/')
    def upload_file():
    return render_template('simple_upload.html')
        
    @app.route('/uploader', methods = ['GET', 'POST'])
    def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        return 'file uploaded successfully'

    if __name__ == "__main__":
        port = int(os.getenv("PORT", 4001))
        app.run(host='0.0.0.0', port=port, debug=True)

Let's go through what is happening here.  Most parts are familiar now.

## Step 2

Missing a 'simple_upload.html', let's create the file

Where to put the file?  templates

    <html>
    <body>
        <form action="{{ url_for('uploader_file') }}" method = "POST" 
            enctype = "multipart/form-data">
            <input type = "file" name = "file" />
            <input type = "submit"/>
        </form>
    </body>
    </html>

## Step 3

Run the program.  You may encounter some errors. You should be able to debug it.

# Recap

* ...
