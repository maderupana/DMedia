import pyautogui as pg
import webbrowser as web
import time
import os
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


def import_csv_data():
    global v
    global csv_file_path
    global cari_csv
    csv_file_path = askopenfilename()
    cari_csv = csv_file_path.find(".csv")
    v.set(csv_file_path)


def run_the_browser():
    if v.get() == '':
        messagebox.showerror(
            "Not Found File", "File extention .csv not found")
    if os.stat(csv_file_path).st_size == 0:
        messeges = "your {} file is empty".format(csv_file_path)
        messagebox.showerror(
            "Empty  File", messeges)
    if not v.get():
        messagebox.showerror(
            "Not Found File", "File extention .csv not found")
    if cari_csv == -1:
        messagebox.showerror(
            "Not Found File", "File extention .csv not found")

    data = pd.read_csv(csv_file_path, sep='[;,]', engine='python')
    data_dict = data.to_dict('list')
    tlfs = data_dict['NomorTlf']
    nama = data_dict['Nama']
    sapaan = data_dict['Sapaan']
    pesan = data_dict['Pesan']
    combo = zip(tlfs, nama, sapaan, pesan)
    first = True

    for tlfs, nama, sapaan, pesan in combo:
        # print(tlfs, sapaan, nama, pesan)
        time.sleep(4)
        web.open(
            "https://web.whatsapp.com/send?phone={}&text={} {},{}".format(tlfs, sapaan, nama, pesan))
        if first:
            time.sleep(8)
            # first = False
        width, height = pg.size()
        pg.click(width/2, height/2)
        time.sleep(8)
        pg.press('enter')
        time.sleep(8)
        pg.hotkey('ctrl', 'w')
    time.sleep(4)
    messagebox.showinfo("Done", "System is Complete")


root = tk.Tk()
# root.iconbitmap(
#     "C:/Users/DODI PRANATA/Documents/whatsbulkpy Gui - Render/favicon.ico")
root.title('WhatsApp Auto Sender')
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set',
          command=import_csv_data).grid(row=0, column=2)
tk.Button(root, text='RUN >>', command=run_the_browser,
          bg='lightblue').grid(row=0, column=3)
tk.Label(root, text='Versi. 1.0').grid(row=1, column=0)
root.geometry("325x50")
root.eval('tk::PlaceWindow . center')
root.mainloop()
