#import,from
import tkinter as tk
from tkinter import filedialog

#meta
root = tk.Tk()
root.title("File Reference App (by Ik)")

#main
def open_file():
    filepath = filedialog.askopenfilename()

# ボタンを作成
btn_open = tk.Button(root, text="ファイルを開く", command=open_file)
btn_open.pack(pady=10)

#ここまでプログラム
root.mainloop()