from flask import Flask, render_template, request, redirect
from assistant.ai import get_ai_response

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():

    user_message = request.form['message']

    response = get_ai_response(user_message)

    return response


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)