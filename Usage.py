# -*- coding: utf-8 -*-

from tkinter import *
from psutil import net_io_counters
####################################ARKAPLAN RENGININ ALGILANMASI ICIN OLAN KISIM
from PIL import ImageGrab
def bgcoloravg():
    toplam=0
    px=ImageGrab.grab().load()
    for y in range(0,20):       ##BELİRLENECEK ALAN 20 PİXEL YÜKSEKLİKTE
        for x in range(460,560):## VE 100 PİXEL GENİŞLİKTE
            rgb=px[x,y]
            toplam+=rgb[0]+rgb[1]+rgb[2]

    bgcolor=round(toplam/6000) #0 ile 255 arasında bir sayı verir parlaklık ölçümü yapar bi nevi.
    return bgcolor
####################################ARKAPLAN RENGININ ALGILANMASI ICIN OLAN KISIM
limit=50
fade=0
sayac=0
        
def updatelabelfont():
    yazi.configure(font=("Helvetica",16,"bold"))
    pencere.geometry('1000x16+0+1')
    madeby.destroy()
    
def acilis():
    yazi.configure(text="Furkan\nBakal",font=("Monotype Corsiva",54,"bold"))
    s=20
    for i in range(0,100):
        pencere.after(s+i*20,fadebelirle)
        
def fadebelirle():
    global fade
    fade= fade+0.01
    pencere.attributes("-alpha",fade)
    

pencere = Tk()
pencere.geometry('450x326+400+600')
#pencere.geometry('1000x16+0+1')          #PENCERENIN BAŞLATILACAĞI KONUMU VE PENCERE BOYUTLARINI BELİRLER
pencere.attributes("-alpha",1)           #ŞEFFAFLIĞI AYARLAR 1.00=OPAK
pencere.attributes("-transparentcolor", "purple")   #MOR RENKLERİ ŞEFFAF YAPAR(PENCERE ARKA PLANINI MOR YAPMIŞTIM)
pencere.configure(background="purple") #PENCERE ARKAPLANININ RENGİNİ BELİRLER #RGB
pencere.overrideredirect(1)             #PENCERE ÇERÇEVESİNİ KALDIRIR
pencere.attributes("-topmost",1)        #SÜREKLİ ÜSTTE KALMAYI SAĞLAR
pencere.title("Kullanım")               #PENCERE BAŞLIĞI
 
topframe = Frame(pencere)
topframe.pack() 

madeby = Label(topframe,text="made by",width=555,bg="purple",fg="black",font=("Monotype Corsiva",25,"bold"))
madeby.pack(side=TOP,fill=Y),
yazi = Label(topframe,width=555,bg="purple",fg="black",font=("Helvetica", 16, "bold"))
yazi.pack(side=LEFT,fill=Y)

acilis()

def downloadbytes():
    try:
        bayt=net_io_counters().bytes_recv/1048576
        return "{:.2f}".format(bayt)+" MB"
    except:
        return "0.00 MB"
    
def updatelabel():
    global limit
    global sayac
    baytlar=downloadbytes()
    yazi.configure(text=baytlar)
    if bgcoloravg()>127:
        yazi.configure(fg="black")
    else:
        yazi.configure(fg="white")

    kullanilan=int(baytlar[:-6])
    sayac+=1
    print(sayac)
    if kullanilan>=limit:
        alarm()
        limit+=50
    yazi.after(50, updatelabel)     #500ms DELAY SAĞLAR. DELAY SONUNDA YAPILACAK İŞLEMİ PARAMETRE OLARAK ALIR
    return

def alarm():
    i=1
    s=-500
    while(i<=3):
      s=s+1000
      pencere.after(s,alarmpos1)
      pencere.after(500+s,alarmpos2)
      i=i+1
        
def alarmpos1():
    yazi.configure(bg="red",fg="white")
    
def alarmpos2():
    yazi.configure(bg="purple",fg="black")

pencere.after(3000,updatelabelfont)
pencere.after(3000,updatelabel)
pencere.mainloop()