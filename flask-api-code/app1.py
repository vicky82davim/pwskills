from flask import Flask, render_template, jsonify
from flask import request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home_page1():
    msg = """
    Company Name: ABC Corporation<br>
    Location: India<br>
    Contact Detail: 999-999-9999<br>
    """
    return msg

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    print(name)
    if name =='welcome':
        return redirect(url_for('home_page1'))
    else:
        return redirect(url_for('hello_guest',guest = name))

if __name__=="__main__":
    app.run(host="0.0.0.0")
