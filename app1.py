# Put your app in here.
from flask import Flask
from flask import request
from operations.py import add
from operations.py import sub
from operations.py import mult
from operations.py import div


app = Flask(__name__)

@app.route('/calculator')
def home_page():
    return """
    <html>
        <body>
            <input type ='text' placeholder='enter number 1' name='num1'/>
            <input type='text' placeholder='enter number 2' name='num2/>
            <button>Submit</button>
        </body>
    </html>
    """

@app.route('calculator/add', methods=['POST'])
def add_two():
    a = request.form['num1']
    b = request.form['num2']
    return add(a,b)

@app.route('calculator/sub', methods=['POST'])
def sub_two():
    a = request.form['num1']
    b = request.form['num2']
    return sub(a,b)

@app.route('calculator/mult', methods=['POST'])
def mult_two():
    a = request.form['num1']
    b = request.form['num2']
    return mult(a,b)

@app.route('calculator/div', methods=['POST'])
def div_two():
    a = request.form['num1']
    b = request.form['num2']
    return div(a,b)


