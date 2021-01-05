from flask import Flask, redirect, url_for, render_template, request, session, abort
app = Flask(__name__)

@app.route('/')
def index():
    return 'this is the index page'

@app.route('/lvl1', methods=['POST'])
def lvl1():
    return render_template('lvl1.html')

@app.route('/lvl2', methods=['POST'])
def lvl2():
    return render_template('lvl2.html')


if __name__ == "__main__":
    app.run(debug = True) 