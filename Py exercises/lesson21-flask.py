from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return ('Hello,world'
        'asdf')


@app.route('/physics')
def broski():
    return 'hi geogre'

@app.route('/ping')
def ping():
        return jsonify({"ok": True})

@app.route('/test')
def serve_html():
    return render_template("temp1.html")

if __name__== "__main__":
    app.run(debug=True)
