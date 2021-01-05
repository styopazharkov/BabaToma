from flask import Flask, redirect, url_for, render_template, request, session, abort
app = Flask(__name__)

app.secret_key = "An arbitrary key"

ANSWER1 = '1'
ANSWER2 = 'ЧерныйКот'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lvl1', methods=['GET','POST'])
def lvl1():
    session['lvl'] = 1
    return render_template('lvl1.html')

@app.route('/lvl2', methods=['GET','POST'])
def lvl2():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER1:
            session['lvl'] = 2
        else:
            session['lvl'] = 1
    except  KeyError:
        pass
    if session['lvl'] >= 2:
        return render_template('lvl2.html')
    else:
        return redirect(url_for('lvl1'))

@app.route('/lvl3', methods=['GET', 'POST'])
def lvl3():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER2:
            session['lvl'] = 3
        else:
            session['lvl'] = 2
    except  KeyError:
        pass
    if session['lvl'] >= 3:
        return render_template('lvl3.html')
    else:
        return redirect(url_for('lvl2'))

if __name__ == "__main__":
    app.run(debug = True) 