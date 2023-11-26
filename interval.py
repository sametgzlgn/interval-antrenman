import tkinter as tk
import time
import threading
import simpleaudio
from tkinter.ttk import Spinbox
from PIL import Image,ImageTk

ALARM = simpleaudio.WaveObject.from_wave_file("alarm.wav")
BIP = simpleaudio.WaveObject.from_wave_file("bip.wav")
zaman = 0
calisma_zamani = 0
dinlenme_zamani = 0
tekrar = 0
toplam_tekrar = 1

def yeni_thread():
    thr = threading.Thread(target=geri_sayim)
    thr.start()

def bicimleme():
    global zaman,dinlenme_zamani,zaman_etk
    if zaman > dinlenme_zamani:
        zaman_etk["fg"] = "red"
    else:
        zaman_etk["fg"] = "blue"

def geri_sayim():
    global zaman,calisma_zamani,dinlenme_zamani,dnln_spbx,clsm_spbx,tkr_spbx,zaman_etk,baslat_btn,tekrar,tkrsys_etk,toplam_tekrar
    tekrar_sayisi = 1
    baslat_btn["state"] = tk.DISABLED
    dnln_spbx["state"] = tk.DISABLED
    clsm_spbx["state"] = tk.DISABLED
    tkr_spbx["state"] = tk.DISABLED
    tekrar = int(tkr_spbx.get())
    while tekrar > 0:
        calisma_zamani = int(clsm_spbx.get())
        dinlenme_zamani = int(dnln_spbx.get())
        zaman = calisma_zamani + dinlenme_zamani
        zaman_etk["text"] = str(zaman) + "s."
        while zaman > 0:
            bicimleme()
            time.sleep(1)
            zaman -= 1
            zaman_etk["text"] = str(zaman) + "s."
        tekrar -= 1
        toplam_tekrar += 1
        BIP.play()
        tkrsys_etk["text"] = str(toplam_tekrar) + ". tekrar"
    baslat_btn["state"] = tk.ACTIVE
    dnln_spbx["state"] = tk.ACTIVE
    clsm_spbx["state"] = tk.ACTIVE
    tkr_spbx["state"] = tk.ACTIVE
    ALARM.play()

def sifirlama():
    global baslat_btn,zaman,zaman_etk,tekrar,tkrsys_etk,tekrar_sayisi
    zaman = 0
    tekrar = 0
    tekrar_sayisi = 1
    tkrsys_etk["text"] = str(tekrar_sayisi) + ". tekrar"
    baslat_btn["state"] = tk.ACTIVE
    zaman_etk["text"] = zaman

pencere = tk.Tk()
ikon = ImageTk.PhotoImage(Image.open("kosu.png"))
pencere.wm_iconphoto(True,ikon)
pencere.geometry(("500x350"))
pencere.title("İnterval Antrenman")
pencere.resizable(False,False)
zaman_etk = tk.Label(text=zaman,font=("Ariel",100))
zaman_etk.pack()
tkrsys_etk = tk.Label(text="{}. tekrar".format(toplam_tekrar),font=("Ariel",15))
tkrsys_etk.place(x=210,y=170)
clsm_etk = tk.Label(text="Antrenman süresi",fg="red")
clsm_etk.place(x=10,y=230)
tkr_etk = tk.Label(text="Tekrar")
tkr_etk.place(x=228,y=230)
tkr_spbx = Spinbox(from_=1,to=10,width=5,wrap=True)
tkr_spbx.place(x=220,y=255)
clsm_spbx = Spinbox(from_=40,to=80,width=5,wrap=True)
clsm_spbx.place(x=35,y=255)
dnln_etk = tk.Label(text="Dinlenme süresi",fg="blue")
dnln_etk.place(x=382,y=230)
dnln_spbx = Spinbox(from_=20,to=60,width=5,wrap=True)
dnln_spbx.place(x=405,y=255)
baslat_btn = tk.Button(text="Başlat",command=yeni_thread)
baslat_btn.place(x=160,y=300)
sifirla_btn = tk.Button(text="Sıfırla",command=sifirlama)
sifirla_btn.place(x=270,y=300)

pencere.mainloop()
