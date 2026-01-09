import ttkbootstrap as ttk
import tkinter.messagebox as mbox

    
window = ttk.Window(themename='flatly')
window.title("Password Manager")
f1 = ttk.Frame(window)
f2 = ttk.Frame(window)

f1.pack()
f2.pack(fill='x')

l1 = ttk.Label(f1, text="Create a password(8 characters minimum):")
l2 = ttk.Entry(f1,show="*")
l3 = ttk.Label(f1, text="Confirm your password:")
l4 = ttk.Entry(f1,show="*")

l1.pack(padx=10,pady=10,fill='x')
l2.pack(padx=10,pady=10,fill='x')
l3.pack(padx=10,pady=10,fill='x')
l4.pack(padx=10,pady=10,fill='x')
def show_warning():
    w1=l2.get()
    w2=int(w1.Count())
    w3=l4.get()
    w4=int(l4.Count())
    if w2==w4:
        mbox.showwarning
    elif w1 == w3:
         mbox.showwarning
            #else
    mbox.showwarning1("Done", "Be careful!")
    
b1 = ttk.Button(f2, text="OK",command=show_warning)
b2 = ttk.Button(f2, text="Cancel",command=show_warning)


b2.pack(side="right",padx=10,pady=10,fill='x')
b1.pack(side="right",padx=10,pady=10,fill='x')


window.mainloop()
