from flask import Flask, redirect, url_for, render_template, request, session, abort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lvl1', methods=['POST'])
def lvl1():
    return render_template('lvl1.html')

@app.route('/lvl2', methods=['POST'])
def lvl2():
    code = request.form['code']
    if code == "1":
        return render_template('lvl2.html')
    else:
        return lvl1()

@app.route('/lvl3', methods=['POST'])
def lvl3():
    return render_template('lvl3.html')

if __name__ == "__main__":
    app.run(debug = True) 