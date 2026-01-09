import ttkbootstrap as ttk

window = ttk.Window(themename="darkly")

window.title("Best Movie")
window.resizable(False,False)
frame = ttk.Frame(window)
frame2 = ttk.Frame(window)
frame3 = ttk.Frame(window)

frame.pack()
frame2.pack()
frame3.pack()
w1 = ttk.Label(frame, text = "Question",
               font= ("Arial" , 18) , justify = "center")
w2 = ttk.Label(frame, text = "Which is the greatest of all movies?",
               justify = "center")
w1.pack(side="top", padx=5, pady=5)
w2.pack(side="top", padx=5, pady=5)

e1 = ttk.Button(frame2, text="A. Starwars Saga")
e2 = ttk.Button(frame2, text="B. Lord of the Rings Trilogy")
e3 = ttk.Button(frame2, text="C. Harry Potter Series")
e4 = ttk.Button(frame2, text="D. Batman Trilogy")


e1.grid(row=0,column=0, padx = 5, pady=5, sticky='ew')
e2.grid(row=0,column=1, padx = 5, pady=5,sticky='ew')
e3.grid(row=1,column=0, padx = 5, pady=5,sticky='ew')
e4.grid(row=1,column=1, padx = 5, pady=5,sticky='ew')

q1 = ttk.Button(frame3, text="SUBMIT")

q1.pack(side="left", padx=5, pady=5)













window.mainloop()
