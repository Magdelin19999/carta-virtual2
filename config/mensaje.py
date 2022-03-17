
from smtplib import SMTP
from email.message import EmailMessage

def mensaje():
    usuario ='jeisonmavisoyface@gmail.com'
    admin = 'magdelinpai1999@gmail.com'
    
    msg = EmailMessage()
    msg.set_content('Mensaje de confirmacioneeeeeeeeeee')
    print('enviando correo')

    msg['Subject']='Asunto de prueba'
    msg['Form']=admin
    msg['To']=usuario

    # el correo del admin
    username = 'magdelinpai1999@gmail.com'
    password = '1124867339'

    server = SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    code = server.rcpt(usuario)
    print(code)
    server.quit()