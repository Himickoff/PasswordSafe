from tkinter import *
import shutil
import os
import pyAesCrypt
import tkinter.messagebox as mb


def encrypt():
    dir = 'mainFile.txt'
    password = mainPasswordEntry.get()
    bufferSize = 512 * 1024
    pyAesCrypt.encryptFile(str(dir), str(dir) + '.aes', password, bufferSize)
    os.rename("mainFile.txt.aes", 'mainFile.aes')
    os.remove('mainFile.txt')


def decrypt():
    dir = 'mainFile.aes'
    password = mainPasswordEntry.get()
    bufferSize = 512 * 1024
    pyAesCrypt.decryptFile(str(dir), str(dir) + '.txt', password, bufferSize)

    os.rename('mainFile.aes.txt', 'mainFile.txt')
    os.remove('mainFile.aes')


def save():
    check = mainPasswordEntry.get()
    if check == '':
        mb.showwarning("Предупреждение", "Пожалуйста введите пароль")
    else:
        file1 = 'mainFile.txt'  # File with data
        try:
            decrypt()
        except:  # if no file, create it
            file = open('mainFile.txt', 'w')
            file.close()
        save = "Логин:" + entryLogin.get() + "  " + "Пароль:" + entryPassword.get() + ' ' + '(с сайта' + ' ' + noticeEntry.get() + ')' + '\n'
        # Create variable with data from input
        file = open('mainFile.txt', 'a')
        file.write(save)
        file.close()
        encrypt()
        input_window("Сохранение пошло успешно")


def show():  # Output passwords in panel(text)
    text = create_text()
    file = 'mainFile.txt'
    decrypt()
    text.delete('1.0', END)
    text1 = output_password()
    text.insert(0.0, text1)
    encrypt()


def input_window(text1):
    text = create_text()
    text.delete('1.0', END)
    text.insert(0.0, text1)


def output_password():
    file = open("mainFile.txt", 'r')
    message = file.read()
    file.close()
    return message


def backup():  # Backup key and main file on external device
    try:
        os.mkdir("E:\BackUp")
    except:
        pass
    try:
        shutil.copyfile("mainFile.aes", "E:\BackUp\mainFile.aes")
        input_window("Резервная копия успешно создана")
    except:
        input_window("Ошибка резервной копии")


#  Tkinter
def login():
    global entryLogin
    labelLogin = Label(text="Логин", font='arial 15')
    labelLogin.place(x=140, y=0)
    entryLogin = Entry(bd=3, width=40)
    entryLogin.place(x=200, y=4)


def password():
    global entryPassword
    labelPassword = Label(text="Пароль", font='arial 15')
    labelPassword.place(x=125, y=28)
    entryPassword = Entry(bd=3, width=40)
    entryPassword.place(x=200, y=33)


def main_password():
    global mainPasswordEntry
    mainPasswordLabel = Label(text="Мастер Пароль", font='arial 15')
    mainPasswordLabel.place(x=0, y=110)
    mainPasswordEntry = Entry(show='*', bd=3)
    mainPasswordEntry.place(x=150, y=115)


def save_button():
    saveButton = Button(text="Сохранить", command=save, font='arial 11')
    saveButton.place(x=460, y=10)


def create_text():
    global panel
    panel = Text()
    panel.place(x=5, y=150)
    return panel


def backup_button():
    backUp = Button(text="Резервная копия", command=backup)
    backUp.place(x=560, y=0)


def show_button():
    showPass = Button(text='Показать сохранённые логины и пароли', command=show, font='arial 10')
    showPass.place(x=300, y=110)


def name():
    global noticeEntry
    noticeLabel = Label(text="Название сайта", font='arial 13')
    noticeLabel.place(x=70, y=59)
    noticeEntry = Entry(bd=3, width=40)
    noticeEntry.place(x=200, y=60)


def edit_button():
    editButton = Button(text="Сохранить изменения", command=edit)
    editButton.place(x=520, y=70)


def edit():
    save = panel.get('1.0', END)
    file1 = 'mainFile.txt'  # File with data
    try:
        decrypt()
    except:  # if no file, create it
        file = open('mainFile.txt', 'w')
        file.close()
    # Create variable with data from input
    file = open('mainFile.txt', 'w')
    file.write(save)
    file.close()
    encrypt()
    input_window("Измнения умешно сохранены")


root = Tk()  # Create window
root.title("Программа для хранения паролей")
root.geometry("660x550")
root.resizable(width=False, height=False)
login()
password()
main_password()
save_button()
create_text()
backup_button()
show_button()
name()
edit_button()
root.mainloop()
