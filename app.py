#coding=utf-8
from flask import Flask
from flask import render_template
from flask import request
from mongo import Mongo
import time
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    m = Mongo()
    if request.method == 'POST':
        if request.form['xliuyan'] != '':
            xinliuyan = {"content": request.form['xliuyan'], "time": time.strftime('%Y-%m-%d %H:%M:%S')}
            m.insert(xinliuyan)
            return render_template('index.html', newmessage=m.show())
        return render_template('index.html', newmessage=m.show())
    return render_template('index.html', newmessage=m.show())
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
