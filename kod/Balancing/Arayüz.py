import tkinter as tk
def hesaplama():
    pass

pencere = tk.Tk()
pencere.title("BALANCİNG")
pencere.attributes('-fullscreen', True)
pencere.state("normal")

etiket =tk.Label(text="Balancing/Tork" , font = " Verdana 22 bold",fg="white")
etiket.pack()

buton=tk.Button(pencere,text="Hesapla",fg="white",bg="black",command=hesaplama,font="Verdana 32 bold")
buton.pack(side=tk.BOTTOM,fill=tk.X)
butonç=tk.Button(pencere,text="Exit",fg="Red",bg="White",command=exit,font="Verdana 12 bold",width=8, height=2)
butonç.pack(anchor="ne")
foto=tk.PhotoImage(file="Balancing/park.png")
label =tk.Label(pencere ,  image=foto,width=1200 , height=1332)
label.pack()

pencere.mainloop()