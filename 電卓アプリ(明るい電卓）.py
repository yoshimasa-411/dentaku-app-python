# ----------------------------------------------------------
# 明るい電卓アプリ
# ----------------------------------------------------------

# 1: まず、画面を作るための道具「tkinter」を使えるようにします。
import tkinter as tk

# 2: エラーを教える小さな窓を使う道具も取り出します。
from tkinter import messagebox

# 3: 押した数字や記号をためておく「式の箱」を作ります。最初は空っぽ。
expression = ""

# 4: 計算の画面（結果を見せる部分）を入れるための箱を準備します。
display_label = None

# 5: ボタンを押したときに、その数字や記号を式にくっつける仕事を作ります。
def append_to_expression(value):
    global expression
    # 押したボタンの文字を、いまある式の後ろにつなげます。
    expression += str(value)
    # 新しい式を画面に表示します。
    display_label.config(text=expression)

# 6: 「＝」ボタンを押したときに、計算をして結果を出す仕事を作ります。
def calculate():
    global expression
    try:
        # 文字の式を本当の計算にして、答えを出します。
        result = eval(expression)
        # 結果を文字にして、もう一度箱に入れます。
        expression = str(result)
        # 結果を画面に表示します。
        display_label.config(text=expression)
    except Exception:
        # もし計算で間違いがあったら、エラーの小窓を出します。
        messagebox.showerror("エラー", "計算できません。もう一度やってね。")
        expression = ""
        display_label.config(text=expression)

# 7: 「C」ボタンで、今の式をぜんぶ消す仕事を作ります。
def clear_expression():
    global expression
    expression = ""
    display_label.config(text=expression)

# 8: ウィンドウ（アプリの画面）を作ります。
root = tk.Tk()

# 9: ウィンドウの上の名前をつけます。
root.title("明るい電卓")

# 10: 背景の色をやわらかい赤色にします。
root.configure(bg="red")

# 11: 計算式や結果を見せる大きな文字の箱を作ります。
display_label = tk.Label(
    root, text=expression, width=24, anchor='e',
    font=("Comic Sans MS", 26, "bold"),
    bg="#ffffff", fg="#333333", relief="groove", bd=5
)
# 12: この箱をいちばん上の列に置きます（4マス分使う）。
display_label.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

# 13: ボタンを作る小さな工場のような関数を作ります。
def make_button(text, cmd, r, c, colspan=1, color="black"):
    # ボタンを作ります（丸っこくて見やすく）
    btn = tk.Button(
        root, text=text, width=5, height=2,
        command=cmd,
        font=("Comic Sans MS", 18, ""),
        bg=color, fg="white",
        activebackground="#a7d8f0",  # ← 押したときに少し濃くなる色
        relief="raised", bd=4
    )
    # ボタンを表のどの場所に置くか決めます。
    btn.grid(row=r, column=c, columnspan=colspan, padx=5, pady=5, ipadx=4, ipady=4)
    return btn

# 14: ボタンの並びを決めるリストを作ります。
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# 15: ボタンを1つずつ作って配置します。
for (text, r, c) in buttons:
    if text == '=':
        # 「＝」ボタンは特別な色（紫）で作ります。
        make_button(text, calculate, r, c, color="purple")
    else:
        # ほかのボタンは押すとその文字が式にくっつくようにします。
        make_button(text, lambda v=text: append_to_expression(v), r, c)

# 16: 「C」ボタンをいちばん下に大きく配置します。
make_button('C', clear_expression, 5, 0, colspan=4, color="green")

# 17: アプリを動かすための命令。これがないと画面がすぐ消えます。
root.mainloop()
