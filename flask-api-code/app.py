from flask import Flask, render_template, jsonify
from flask import request, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home_page1():
    msg = """
    Company Name: ABC Corporation<br>
    Location: India<br>
    Contact Detail: 999-999-9999<br>
    """
    return msg

@app.route('/welcome', methods = ['GET', 'POST'])
def welcome():
    return "Welcome to ABC Corporation"

@app.route('/tt', methods = ['GET', 'POST'])
def home_page():
    return render_template("index.html")

@app.route('/math', methods=['POST'])
def calculate():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0
        if ops == 'add':
            result = 'Sum of: ' + str(num1+num2)
        return render_template('results.html', result=result)

@app.route('/postman_data', methods=['POST'])
def calculate_postman():
    if request.method == 'POST':
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = 0
        if ops == 'add':
            result = 'Sum of: ' + str(num1+num2)
        return jsonify(result)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/test2")
def test():
    data = request.args.get('x')
    return "This is data input {}".format(data)

@app.route('/user/<name>')
def hello_user(name):
   if name =='welcome':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__=="__main__":
    app.run(host="0.0.0.0")
