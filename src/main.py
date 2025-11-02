#import,from
import tkinter
from tkinter import filedialog

#meta
root = tkinter.Tk()
root.title("File Reference App (by Ik)")

#main
def open_file():
    """ファイル選択ダイアログを開き、選択されたファイルパスを取得する"""
    filepath = filedialog.askopenfilename()

# ファイル選択ボタンを作成
btn_open = tk.Button(root, text="ファイルを開く", command=open_file)
btn_open.pack(pady=10)

#ここまでプログラム
root.mainloop()