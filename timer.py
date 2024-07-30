import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
from tkinter import *
import ttkbootstrap as tb
#AK11
zaman=0
root=tb.Window(themename="cyborg")
root.title("Sayaç")
root.geometry("400x250")

def sil_saydir():
    global zaman
    zaman=int(my_entry.get())


    for widget in root.winfo_children():
        widget.destroy()

    def saydir():
        my_button1.destroy()
        global zaman
        if zaman>=0:
            seconds=zaman%60
            minutes=int(zaman/60)%60
            hours=int(zaman/3600)%24
            textt=f"{hours:02}:{minutes:02}:{seconds:02}"
            my_label1.config(text=textt,font=("Helvetica",75),width=10,background="black")
            zaman-=1
            root.after(1000,saydir)
        else:
            my_label1.config(text="Süre Doldu",font=("Arial",35),background="white",foreground="black")
            cikis_button=tb.Button(root,text="Uygulamayı Kapat",bootstyle="danger outline",command=root.quit,width=40)
            cikis_button.pack(pady=30)



    my_frame=tb.Frame(root,bootstyle="light")
    my_frame.pack(pady=10)    
    my_label1=tb.Label(my_frame,bootstyle="inverse-dark",text="Sayaç Başlasın mı?",font=("Helvetica",18))
    my_label1.pack(pady=5,padx=5)
    my_button1=tb.Button(root,bootstyle="danger outline",text="Evet",command=saydir)
    my_button1.pack(pady=2)
    

my_label=tb.Label(root,bootstyle="primary",text="Saniye giriniz alta",font=("Helvetica",18))
my_label.pack(pady=5)
my_entry=tb.Entry(root,bootstyle="danger",width=40,font=("Helvetica",18),foreground="white")
my_entry.pack(pady=5)
my_button=tb.Button(root,bootstyle="danger outline",text="Tıkla",command=sil_saydir)
my_button.pack(pady=5 )

root.mainloop()