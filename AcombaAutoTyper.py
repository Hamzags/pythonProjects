import tkinter as tk
import datetime
import pyautogui
import getpass

def create_buttons():
    rep_button_values = {
        'Reparation': {
            'RepCompMsgLaisse': 'Reparation completee - Message laisse - ' + get_current_datetime() + ' - ' + get_user_initials(),
            'RepCompClientAvise': 'Reparation completee - Client avise - ' + get_current_datetime() + ' - ' + get_user_initials()
        },
        'Diagnostic': {
            'MsgPourDiag': 'Message laisse - ' + get_current_datetime() + ' - ' + get_user_initials(),
            'ClientAviseDiagAccepte': 'Client avise diag - Accepte frais $ - ' + get_current_datetime() + ' - ' + get_user_initials()
        },
        'Autre': {
            'Autre1': 'Autre 1',
            'Autre2': 'Autre 2'
        }
    }

    font = 'Arial Unicode MS'
    for key, value in rep_button_values.items():
        tk.Label(root, text=key, font=(font, 14)).pack(pady=8)
        for btn_key, btn_value in value.items():
            button = tk.Button(root, text=btn_key, font=(font, 12), command=lambda v=btn_value: on_button_click(v))
            button.pack(pady=4)

def on_button_click(value):
    def type_value():
        x, y = pyautogui.position()
        pyautogui.click(x=x, y=y)
        pyautogui.typewrite(value)

    root.after(2200, type_value)

def get_user_initials():
    username = getpass.getuser()
    initials = ''.join(word[0] for word in username.split())
    return initials

def get_current_datetime():
    now = datetime.datetime.now()
    return now.strftime("%d/%m/%Y - %H:%M:%S")

root = tk.Tk()
root.geometry('400x400')
root.title('Acomba Auto Typer')

create_buttons()

root.mainloop()
