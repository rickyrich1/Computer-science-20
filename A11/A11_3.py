import ttkbootstrap as ttk
window = ttk.Window(themename='flatly')
window.resizable(False,False)
window.title("Calculator")

top = ttk.Frame(window)
bottom = ttk.Frame(window)

top.pack(fill='x')
bottom.pack()

w1 = ttk.Entry(top,)

w1.pack(side = "left", padx=5, pady=5,fill='x', expand=True)

e1 = ttk.Button(bottom, text="7")
e2 = ttk.Button(bottom, text="8")
e3 = ttk.Button(bottom, text="9")
e4 = ttk.Button(bottom, text="/")
e5 = ttk.Button(bottom, text="4")
e6 = ttk.Button(bottom, text="5")
e7 = ttk.Button(bottom, text="6")
e8 = ttk.Button(bottom, text="*")
e9 = ttk.Button(bottom, text="1")
e10 = ttk.Button(bottom, text="2")
e11 = ttk.Button(bottom, text="3")
e12 = ttk.Button(bottom, text="-")
e13 = ttk.Button(bottom, text="0")
e14 = ttk.Button(bottom, text="+")
e15 = ttk.Button(bottom, text="C")
e16 = ttk.Button(bottom, text="=")




e1.grid(row=0,column=0, padx = 5, pady=5,sticky='ew')
e2.grid(row=0,column=1, padx = 5, pady=5,sticky='ew')
e3.grid(row=0,column=2, padx = 5, pady=5,sticky='ew')
e4.grid(row=0,column=3, padx = 5, pady=5,sticky='ew')
e5.grid(row=1,column=0, padx = 5, pady=5,sticky='ew')
e6.grid(row=1,column=1, padx = 5, pady=5,sticky='ew')
e7.grid(row=1,column=2, padx = 5, pady=5,sticky='ew')
e8.grid(row=1,column=3, padx = 5, pady=5,sticky='ew')
e9.grid(row=2,column=0, padx = 5, pady=5,sticky='ew')
e10.grid(row=2,column=1, padx = 5, pady=5,sticky='ew')
e11.grid(row=2,column=2, padx = 5, pady=5,sticky='ew')
e12.grid(row=2,column=3, padx = 5, pady=5,sticky='ew')
e13.grid(row=3,column=0, padx = 5, pady=5,sticky='ew')
e14.grid(row=3,column=1, padx = 5, pady=5,sticky='ew')
e15.grid(row=3,column=2, padx = 5, pady=5,sticky='ew')
e16.grid(row=3,column=3, padx = 5, pady=5,sticky='ew')








window.mainloop()
