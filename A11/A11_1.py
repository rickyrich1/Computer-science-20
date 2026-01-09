import ttkbootstrap as ttk
window = ttk.Window(themename = 'flatly')
window.resizable(False, False)
window.title("Account information")

top = ttk.Labelframe(window, text = "Account Information")
bottom = ttk.Labelframe(window, text = "Submission")

top.pack(side = "top", padx = 5, pady = 5)
bottom.pack(side = "top", padx = 5, pady = 5,fill='x')

w1 = ttk.Label(top, text = "First name:")
w2 = ttk.Entry(top)
w3 = ttk.Label(top, text = "Last name:")
w4 = ttk.Entry(top)
w5 = ttk.Label(top, text = "Username:")
w6 = ttk.Entry(top)

w1.grid(row=0,column=0, padx = 5, pady=5)
w2.grid(row=0, column=1, padx = 5, pady=5)
w3.grid(row=1, column=0, padx = 5, pady=5)
w4.grid(row=1, column=1, padx = 5, pady=5)
w5.grid(row=2, column=0, padx = 5, pady=5)
w6.grid(row=2, column=1, padx = 5, pady=5)

e1 = ttk.Button(bottom, text = "Save")
e2 = ttk.Button(bottom, text = "Clear")
e3 = ttk.Button(bottom, text = "Exit")
e1.pack(side = "left", padx = 5, pady=5)
e2.pack(side = "left", padx = 5, pady=5)
e3.pack(side = "left", padx = 5, pady=5)
























window.mainloop()
