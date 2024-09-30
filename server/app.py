#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)  # This should print in the console
    return parameter  # This should display in the browser

@app.route('/count/<int:parameter>')
def count_route(parameter):
    return "\n".join(str(i) for i in range(parameter))



@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_route(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation'







if __name__ == '__main__':
    app.run(port=5555, debug=True)
