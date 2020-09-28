from flask_mail import Mail, Message

mail = Mail()


def send_mail(recipient, title, html):
    msg = Message(title, recipients=[recipient])
    msg.html = html
    mail.send(msg)
