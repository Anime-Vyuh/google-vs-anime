import tkinter as tk
from gtts import gTTS
import pygame,os
from PIL import Image,ImageTk
import playsound
from tkinter import messagebox

def speak(dialog):
    try:
        google_dia = gTTS(text=dialog, lang='ja', slow=False)
        google_dia.save('{}.mp3'.format(dialog))  ##  save audio
        playsound.playsound('{}.mp3'.format(dialog))
    except:
        pass
def character_dialog(char):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('dialouges/{}.ogg'.format(char))
        pygame.mixer.music.play(loops=1)
    except pygame.error as e:
        messagebox.showerror(e,"Change the folder path")

def sub(dialog):
    pygame.mixer.init()
    m = pygame.mixer.Sound
    pygame.mixer.sound.play()

def googleVA(name):
    speak(name.replace('_',''))

def animeVA(name):
    character_dialog(name)

def main():
    root = tk.Tk()
    pygame.init()
    root.geometry("625x665+325+0")
    root.resizable(False,False)
    root.title("GoogleVA Vs AnimeVA")

    canvas= tk.Canvas(root,bg="#00ffff")
    canvas.place(x=-1,y=-1,width=650,height=330)
    canvas1= tk.Canvas(root,bg="#ff66ff")
    canvas1.place(x=0,y=330,width=650,height=350)

    famous_dialouge = ['Baka','Yowai_mo','Tatakae','Ara_ara','Ganbare_Ganbare','Nani','OKawaii_Koto','Kamona','Yamate_Kudasai','Chotto_matte']
    famous_dialouge.sort()

    for i,dia in enumerate(famous_dialouge,1):
        dialouge_label = tk.Label(text="{}.{}".format(i,dia.replace('_',' ')),font=("arial",14,"bold"),bg="black",fg="white").place(x=30,y=(51+i)*i)
        g = tk.Button(root, text="Google VA{}".format(i),bd=4,command= lambda i = dia:googleVA(i.lower()))
        g.place(x=240,y=(50+i)*i)

        a = tk.Button(root, text="Anime VA{}".format(i),bd=4,command= lambda i = dia:animeVA(i.lower()))
        a.place(x=450,y=(50+i)*i)

    root.mainloop()

if __name__ == '__main__':
    main()