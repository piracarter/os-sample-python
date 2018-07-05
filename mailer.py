import smtplib

from email.mime.text import MIMEText

msg = MIMEText("Un simple texto para validar que funciona correctamente un post-commit")
msg['Subject'] = 'Correo enviado desde hook post-commit by-python'
msg['From'] = 'root-master@lab.example.com'
msg['To'] = 'root@lab.example.com'

s = smtplib.SMTP('mail.example.com')
s.sendmail('root-master@lab.example.com', ['root@lab.example.com'], msg.as_string())
s.quit()
