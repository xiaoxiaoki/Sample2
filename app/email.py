# coding:utf-8
from threading import Thread
from flask import current_app,render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):

    with app.app_context():
        mail.send(msg)


# def send_email():
#     app = current_app._get_current_object()
#     msg = Message(subject="Hello World!",
#                   sender='1241908493@qq.com',
#                   recipients=["1430250645@qq.com"])
#     msg.body = "testing"
#     msg.html = "<b>testing</b>"
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()
#     return thr


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])  # recipients是个列表，包含所有收件人
    msg.body = render_template(template + '.txt', **kwargs)  # 邮件发送给目标，可以有文本，两种方式呈现，你能看见怎样的取决于你的客户端
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
