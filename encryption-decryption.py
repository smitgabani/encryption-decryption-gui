from tkinter import *
import base64 # Vigenère cipher

root = Tk()
root.title("Encryption Decryption")
root.geometry("500x300")
root.resizable(0,0)

##################################################
f1 = Frame(root)
f1.pack(anchor=CENTER)

f2 = Frame(root)
f2.pack(anchor=CENTER)

##################################################
message = StringVar()
key = StringVar()
mode = StringVar()
result = StringVar()

##################################################
def qExit():
    root.destroy()

def Reset():
    #rand.set("")
    message.set("")
    key.set("")
    mode.set("")
    result.set("")

##################################################
messagel = Label(f1, text="Message   ", font = ('calibri', 20))
messagel.grid(column=0, row= 1, pady=(50,0), padx=(50,0))
keyl = Label(f1, text="Key", font = ('calibri', 20))
keyl.grid(column=0, row=2, pady=(0,0), padx=(0,0))
model = Label(f1, text = "Mode", font = ('calibri', 20))
model.grid(column=0, row=3, pady=(0,0), padx=(0,0))
resultl = Label(f1, text="Result ", font = ('calibri', 20))
resultl.grid(column=0, row=4, pady=(0,0), padx=(0,0))
messagee= Entry(f1, font=('arial', 16), textvariable=message)
messagee.grid(column= 1, row= 1, pady=(50,0), padx=(0,50))
keye = Entry(f1, font=('arial', 16), textvariable=key)
keye.grid(column=1, row = 2, pady=(0,0), padx=(0,50))
modee = Entry(f1, font=('arial', 16), textvariable=mode)
modee.grid(column=1, row = 3, pady=(0,0), padx=(0,50))
resulte = Entry(f1, font=('arial', 16), textvariable=result)
resulte.grid(column=1, row=4, pady=(0,0), padx=(0,50))

##################################################
def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)

def Ref():
    clear = message.get()
    k = key.get()
    m = mode.get()
    print("Message= ", messagee.get())

    if (m == 'e'):
        result.set(encode(k, clear))
        print("Mode Enc, Result :", result.get() )
    else:
        result.set(decode(k, clear))
        print("Mode Dec, Result :", result.get())

##################################################
encdyc = Button(f2, text=" Result ", font = ('calibri', 15), command=Ref)
encdyc.grid(column=0, row=1, pady=(20,30), padx=(0,30))
reset = Button(f2, text=" Reset ", font=('calibri', 15), command=Reset)
reset.grid(column=1, row=1, pady=(20,30), padx=(0,30))
exit = Button(f2, text="  Exit  ", font = ('calibri', 15),command=qExit)
exit.grid(column=2, row=1, pady=(20,30), padx=(0,30))

root.mainloop()
