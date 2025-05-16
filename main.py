from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('files', filename, as_attachment=True)
if __name__ == "__main__":
    app.run(debug=True)
