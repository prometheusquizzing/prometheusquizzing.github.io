from flask import Flask, render_template,send_from_directory


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/aboutus')
def aboutUs():
	return render_template('aboutus.html')

@app.route('/archive')
def archive():
	return render_template('archive.html')

@app.route('/archive/<path:path>')
def fileDl(path):
	return send_from_directory('files',path)


if __name__ == '__main__':
    app.run(debug=True)
