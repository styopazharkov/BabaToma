from flask import Flask, redirect, url_for, render_template, request, session, abort
app = Flask(__name__)

app.secret_key = "An arbitrary key"

ANSWER1 = '1'
ANSWER2 = 'ЧерныйКот'
ANSWER3 = '1'
ANSWER4 = '1'
ANSWER5 = '1'
ANSWER6 = '1'
ANSWER7 = '1'
ANSWER8 = '1'
ANSWER9 = '1'
ANSWER10 = '1'
ERROR_MESSAGE = "Неверный Код!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lvl1', methods=['GET','POST'])
def lvl1():
    session['lvl'] = 1
    try:
        error = session.pop('error')
    except KeyError:
        error = ""
    return render_template('lvl1.html', error = error)

@app.route('/lvl2', methods=['GET','POST'])
def lvl2():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER1:
            session['lvl'] = 2
        else:
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 1
    except  KeyError:
        pass
    if session['lvl'] >= 2:
        try:
            error = session.pop('error')
        except KeyError:
            error = ""
        return render_template('lvl2.html', error = error)
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
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 2
    except  KeyError:
        pass
    if session['lvl'] >= 3:
        try:
            error = session.pop('error')
        except KeyError:
            error = ""
        return render_template('lvl3.html', error = error)
    else:
        return redirect(url_for('lvl2'))

@app.route('/lvl4', methods=['GET', 'POST'])
def lvl4():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER3:
            session['lvl'] = 4
        else:
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 3
    except  KeyError:
        pass
    if session['lvl'] >= 4:
        try:
            error = session.pop('error')
        except KeyError:
            error = ""
        return render_template('lvl4.html', error = error)
    else:
        return redirect(url_for('lvl3'))

@app.route('/lvl5', methods=['GET', 'POST'])
def lvl5():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER4:
            session['lvl'] = 5
        else:
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 4
    except  KeyError:
        pass
    if session['lvl'] >= 5:
        try:
            error = session.pop('error')
        except KeyError:
            error = ""
        return render_template('lvl5.html', error = error)
    else:
        return redirect(url_for('lvl4'))

@app.route('/lvl6', methods=['GET', 'POST'])
def lvl6():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER5:
            session['lvl'] = 6
        else:
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 5
    except  KeyError:
        pass
    if session['lvl'] >= 6:
        try:
            error = session.pop('error')
        except KeyError:
            error = ""
        return render_template('lvl6.html', error = error)
    else:
        return redirect(url_for('lvl5'))

@app.route('/lvl7', methods=['GET', 'POST'])
def lvl7():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER6:
            session['lvl'] = 7
        else:
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 6
    except  KeyError:
        pass
    if session['lvl'] >= 7:
        try:
            error = session.pop('error')
        except KeyError:
            error = ""
        return render_template('lvl7.html', error = error)
    else:
        return redirect(url_for('lvl6'))

@app.route('/lvl8', methods=['GET', 'POST'])
def lvl8():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER7:
            session['lvl'] = 8
        else:
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 7
    except  KeyError:
        pass
    if session['lvl'] >= 8:
        try:
            error = session.pop('error')
        except KeyError:
            error = ""
        return render_template('lvl8.html', error = error)
    else:
        return redirect(url_for('lvl7'))

@app.route('/lvl9', methods=['GET', 'POST'])
def lvl9():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER8:
            session['lvl'] = 9
        else:
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 8
    except  KeyError:
        pass
    if session['lvl'] >= 9:
        try:
            error = session.pop('error')
        except KeyError:
            error = ""
        return render_template('lvl9.html', error = error)
    else:
        return redirect(url_for('lvl8'))

@app.route('/lvl10', methods=['GET', 'POST'])
def lvl10():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER9:
            session['lvl'] = 10
        else:
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 9
    except  KeyError:
        pass
    if session['lvl'] >= 10:
        try:
            error = session.pop('error')
        except KeyError:
            error = ""
        return render_template('lvl10.html', error = error)
    else:
        return redirect(url_for('lvl9'))

@app.route('/finish', methods=['GET', 'POST'])
def finish():
    if not session.get('lvl'):
        return redirect(url_for('index'))
    try:
        code = request.form['code']
        if code == ANSWER10:
            session['lvl'] = 11
        else:
            session['error'] = ERROR_MESSAGE
            session['lvl'] = 10
    except  KeyError:
        pass
    if session['lvl'] >= 11:
        return render_template('finish.html')
    else:
        return redirect(url_for('lvl10'))

    
if __name__ == "__main__":
    app.run(debug = True) 