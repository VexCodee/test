from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        operation_str = 'dodawanie'
        result = num1 + num2 if num1 + num2 <= 100 else None
    elif operation == 'subtract':
        operation_str = 'odejmowanie'
        result = num1 - num2 if num1 >= num2 else num2 - num1
    elif operation == 'multiply':
        operation_str = 'mnożenie'
        result = num1 * num2 if num1 * num2 <= 100 else None
    elif operation == 'divide':
        operation_str = 'dzielenie'
        if num2 != 0 and num1 % num2 == 0:
            result = num1 // num2
        else:
            result = 'Nie można wykonać dzielenia'
    else:
        operation_str = 'Nieznana operacja'
        result = None

    return render_template('result.html', num1=num1, num2=num2, operation=operation, operation_str=operation_str, result=result)


@app.route('/random')
def random_operation():
    operation = random.choice(['dodawanie', 'odejmowanie', 'mnozenie', 'dzielenie'])

    if operation == 'dodawanie':
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100 - num1)
        operation_str = 'dodawanie'
    elif operation == 'odejmowanie':
        num1 = random.randint(0, 100)
        num2 = random.randint(0, num1)
        operation_str = 'odejmowanie'
    elif operation == 'mnozenie':
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operation_str = 'mnożenie'
    else:
        num1 = random.randint(1, 100)
        divisors = [i for i in range(1, num1 + 1) if num1 % i == 0]
        num2 = random.choice(divisors)
        operation_str = 'dzielenie'

    return render_template('random.html', num1=num1, num2=num2, operation=operation, operation_str=operation_str)


@app.route('/check', methods=['POST'])
def check():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operation = request.form['operation']
    user_answer = int(request.form['answer'])

    if operation == 'dodawanie':
        correct_answer = num1 + num2

    elif operation == 'odejmowanie':
        correct_answer = num1 - num2

    elif operation == 'mnozenie':
        correct_answer = num1 * num2

    elif operation == 'dzielenie':
        if num2 != 0 and num1 % num2 == 0:
            correct_answer = num1 // num2
        else:
            correct_answer = None

    is_correct = user_answer == correct_answer if correct_answer is not None else False

    return render_template('check.html', num1=num1, num2=num2, operation=operation, user_answer=user_answer,
                           correct_answer=correct_answer, is_correct=is_correct)


if __name__ == '__main__':
    app.run(debug=True)