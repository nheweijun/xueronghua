#coding=utf-8
from flask import Flask
from flask import render_template
from flask import request
from Global import liuyan
from function import huoqu
import pymongo
import time
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    connection = pymongo.MongoClient('localhost', 27017)
    db = connection.test
    if request.method == 'POST':
        if request.form['xliuyan'] != '':
            xinliuyan = ''
            xinliuyan = request.form['xliuyan'] + ' ' + time.strftime('%m-%d %H:%M', time.localtime(time.time()))
            liuyan.append(xinliuyan)
            return render_template('index.html', newmessage=huoqu())
        return render_template('index.html', newmessage=huoqu())
    return render_template('index.html', newmessage=huoqu())
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
