import ttkbootstrap as ttk
window = window = ttk.Window(themename='darkly')
window.resizable(False,False)
window.title("Destiny Chooser")

top = ttk.Frame(window)
mid = ttk.Frame(window)
mid2 = ttk.Frame(window)
buttom = ttk.Frame(window)

top.pack()
mid.pack()
mid2.pack(fill='x')
buttom.pack()

w1 = ttk.Label(top, text = "CHOOSE YOUR DESTINY...",
               font=("Cambria",18))
w1.pack(side="top", padx=5, pady=5,
    )
img = ttk.PhotoImage(file="vader.png")
w2 = ttk.Button(mid, image=img)
img2 = ttk.PhotoImage(file="yoda.png")
w3 = ttk.Button(mid, image=img2)

w2.pack(side="left", padx=5, pady=5)
w3.pack(side="left", padx=5, pady=5)

choice = ttk.StringVar(value="A")

b1 = ttk.Radiobutton(mid2, text="Dark Side", value="A", variable=choice)
b2 = ttk.Radiobutton(mid2, text="Light Side", value="B", variable=choice)

b1.pack(side="left", padx=10, pady=5)
b2.pack(side="left", padx=10, pady=5)


agree_var = ttk.StringVar()

b3 = ttk.Checkbutton(mid2, text="Force Sensitive",variable=agree_var,
                     bootstyle="round-toggle", onvalue=True)
b4 = ttk.Checkbutton(mid2, text="LightSaver Skilled",variable=agree_var,
                     bootstyle="round-toggle", onvalue=True)

b3.pack(side="left", padx=15, pady=5,fill='x')
b4.pack(side="left", padx=15, pady=5,fill='x')

b5 = ttk.Button(buttom, text="Follow you Destiny...")

b5.pack(side="top",padx=5, pady=5)

