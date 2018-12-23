from flask import Flask, request
from flask_cors import CORS
from mail import send_mail

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return 'Check Ok'


@app.route('/mail')
def mail():
    email = request.args.get('email')
    tel = request.args.get('tel')
    body = request.args.get('body')
    answer = request.args.get('answer')

    # over simple validator
    if answer == '5':
        message = f'Сообщение от {email} | Телефон: {tel} | Текст сообщение: {body}'
        send_mail(to_email=email, message=message)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5444, debug=True)
