import tkinter
from tkinter import ttk
import socket






    # 自分のIPアドレス取得
    #host = socket.gethostname()
    #print(host)

    #ip = socket.gethostbyname(host)
    #print(ip)


if __name__ == '__main__':

    #---------- Window作成 ----------
    root = tkinter.Tk()
    root.title("チャットくん")  #画面サイズ
    root.resizable(False, False)  #リサイズ不可

    #---------- Frame作成 ----------
    frame_left   = tkinter.Frame(root)
    frame_right  = tkinter.Frame(root)
    frame_bottom = tkinter.Frame(root)

    #---------- Frame配置 ----------
    frame_left.grid(row=0, column=0)
    frame_right.grid(row=0, column=1)
    frame_bottom.grid(row=1, column=0, columnspan=2)


    #---------- Frame(left) ----------
    #Label
    label_dest = tkinter.Label(frame_left, text="通信相手")
    label_dest.grid(row=0, column=0)

    #Entry
    entry_dest_sv = tkinter.StringVar()
    entry_dest = tkinter.Entry(frame_left, textvariable=entry_dest_sv, width=20)
    entry_dest.grid(row=0, column=1)


    #---------- Frame(right) ----------
    #Label
    label_src = tkinter.Label(frame_right, text="自分")
    label_src.grid(row=0, column=0)

    #Text
    entry_src_sv = tkinter.StringVar()
    entry_src = tkinter.Entry(frame_right, textvariable=entry_src_sv, width=20)
    entry_src.grid(row=0, column=1)

    #
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    entry_src_sv.set(ip)




    root.mainloop()



