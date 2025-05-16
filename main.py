from flask import Flask, render_template, request, send_from_directory
import datetime



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    current_time = datetime.datetime.now().year
    return render_template('index.html', year=current_time)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('files', filename, as_attachment=True)
if __name__ == "__main__":
    app.run(debug=True)
