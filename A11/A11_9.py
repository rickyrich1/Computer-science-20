import ttkbootstrap as ttk
window= ttk.Window(themename='darkly')
f1 = ttk.Frame(window)
f2 = ttk.Frame(window)
#def next():
    
    
img0 = ttk.PhotoImage(file="slidePic1.PNG")
img1 = ttk.PhotoImage(file="slidePic2.PNG")
img2 = ttk.PhotoImage(file="slidePic3.PNG")
img3 = ttk.PhotoImage(file="slidePic4.PNG")
img4 = ttk.PhotoImage(file="slidePic5.PNG")

b1 = ttk.Button(f2,text="Previous")
b2 = ttk.Button(f2,text="Next")

b1.pack()
b2.pack()
label1= ttk.Label(f1, image=img0).pack(padx=10,pady=10)





window.mainloop()
