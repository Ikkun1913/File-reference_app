#import,from
import tkinter as tk
import os
from tkinter import filedialog

#meta
root = tk.Tk()
root.title("File Reference App (by Ik)")

#main
def open_file():
    filepath = filedialog.askopenfilename()

def open_folder():
    iDir = os.path.abspath(os.path.dirname(__file__))
    folder_name = tk.filedialog.askdirectory(initialdir=iDir)

# ボタンを作成
btn_open = tk.Button(root, text="ファイルを開く", command=open_file)
btn_open.pack(pady=10)

button = tk.Button(root, text="フォルダを開く", command=open_folder)
button.pack(pady=10)

#ここまでプログラム
root.mainloop()