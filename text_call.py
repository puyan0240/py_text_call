import tkinter
from tkinter import ttk
import socket


#言語テーブル
LANG_TBL_NAME=0
LANG_TBL_PARAME=1   # 翻訳、読み上げ
lang_tbl = [
    ["Japanese (日本語)", "ja"],
    ["English (英語)", "en"],
    ["German (ドイツ語)", "de"],
    ["French (フランス語)", "fr"],
    ["Italian (イタリア語)", "it"],
    ["Spanish (スペイン語)", "es"],
    ["Portuguese (ポルトガル語)", "pt"],
    ["Russian (ロシア語)", "ru"],
    ["Korean (韓国語)", "ko"],
    ["chinese (中国語)", "zh-cn"],
    ["Vietnamese (ベトナム語)", "vi"]
]



def click_send_btn():
    #入力枠の内容を取得
    text = entry_center3_sv.get()

    #入力枠の内容を送信枠に表示
    entry_center2_sv.set(text)

    #入力枠をクリア
    entry_center3_sv.set("")


if __name__ == '__main__':

    #---------- Window作成 ----------
    root = tkinter.Tk()
    root.title("チャットくん")  #画面サイズ
    root.resizable(False, False)  #リサイズ不可

    #---------- Frame作成 ----------
    frame_left    = tkinter.Frame(root)
    frame_right   = tkinter.Frame(root)
    frame_center1 = tkinter.Frame(root)
    frame_center2 = tkinter.Frame(root)
    frame_center3 = tkinter.Frame(root)
    frame_bottom  = tkinter.Frame(root)
    separator     = ttk.Separator(root, orient="horizontal", style="blue.TSeparator")

    #---------- Frame配置 ----------
    frame_left.grid(row=0, column=0)
    frame_right.grid(row=0, column=1)
    frame_center1.grid(row=1, column=0, columnspan=2)
    frame_center2.grid(row=2, column=0, columnspan=2)
    separator.grid(row=3, column=0, columnspan=2, sticky="ew")
    frame_center3.grid(row=4, column=0, columnspan=2)
    frame_bottom.grid(row=5, column=0, columnspan=2)


    #---------- Frame(left) ----------
    #Label
    label_left = tkinter.Label(frame_left, text="通信相手")
    label_left.grid(row=0, column=0)

    #Entry
    entry_left_sv = tkinter.StringVar()
    entry_left = tkinter.Entry(frame_left, textvariable=entry_left_sv, width=20)
    entry_left.grid(row=0, column=1)


    #---------- Frame(right) ----------
    #Label
    label_right = tkinter.Label(frame_right, text="自分")
    label_right.grid(row=0, column=0)

    #Entry
    entry_rigth_sv = tkinter.StringVar()
    entry_rigth = tkinter.Entry(frame_right, textvariable=entry_rigth_sv, width=20)
    entry_rigth.grid(row=0, column=1)

    #EntryにIPアドレスを表示
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    entry_rigth_sv.set(ip)


    #---------- Frame(center1) ----------
    #Label
    label_center1 = tkinter.Label(frame_center1, text="受信")
    label_center1.grid(row=0, column=0)

    #Entry
    entry_center1_sv = tkinter.StringVar()
    entry_center1 = tkinter.Entry(frame_center1, textvariable=entry_center1_sv, width=100)
    entry_center1.config(state=tkinter.DISABLED)
    entry_center1.grid(row=0, column=1)


    #---------- Frame(center2) ----------
    #Label
    label_center2 = tkinter.Label(frame_center2, text="送信")
    label_center2.grid(row=0, column=0)

    #Entry
    entry_center2_sv = tkinter.StringVar()
    entry_center2 = tkinter.Entry(frame_center2, textvariable=entry_center2_sv, width=100)
    entry_center2.config(state=tkinter.DISABLED)
    entry_center2.grid(row=0, column=1)


    #---------- Frame(center3) ----------
    #Label
    label_center3 = tkinter.Label(frame_center3, text="入力")
    label_center3.grid(row=0, column=0)

    #Entry
    entry_center3_sv = tkinter.StringVar()
    entry_center3 = tkinter.Entry(frame_center3, textvariable=entry_center3_sv, width=100)
    entry_center3.grid(row=0, column=1)

    #---------- Frame(Bottom) ----------
    #Button
    send_btn = tkinter.Button(frame_bottom, text="送信", command=click_send_btn)
    send_btn.grid(row=0, column=0, padx=40, pady=15, ipadx=15, ipady=10)

    #Label
    label_bottom = tkinter.Label(frame_bottom, text="言語")
    label_bottom.grid(row=0, column=1)

    #Combobox
    cb_bottom_menu = []
    for val in lang_tbl:
        cb_bottom_menu.append(val[LANG_TBL_NAME])
    cb_bottom = ttk.Combobox(frame_bottom, textvariable=tkinter.StringVar(), values=cb_bottom_menu, state="readonly", width=25)
    cb_bottom.current(0)
    cb_bottom.grid(row=0, column=2)


    root.mainloop()



