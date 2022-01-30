from distutils.log import info
from pdb import line_prefix
from tkinter import * 
import subprocess
import gettext
from tkinter import font

root = Tk()
root.geometry("1900x1080")
root.title("Lan passwords List")
Label(root,text="Press to show your LAN passwords and usernames",font="times 15 bold").grid()

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]



def submit_value():
    for wifi in wifis:
        results = subprocess.check_output(['netsh','wlan','show','profile',wifi, 'key=clear']).decode('utf-8').split('\n')
        results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
        try:
            Label(root,text=(f'Name: {wifi}, Password: {results[0]}'),font="times 15").grid()
        except IndexError:
            Label(root,text=(f'Name: {wifi}, Password: Cannot be read!'),font="times 15").grid()

Button(text="Submit", command = submit_value ).grid()





root.mainloop()