from tkinter import * 
from translate import Translator
from gtts import gTTS
from playsound import playsound
from time import sleep
import os
import pyglet
class language:
    def __init__(self,root):
        self.root=root      
        self.root.title("Language Translator And Speech")
        self.root.geometry("500x420+300+50")
        self.root.resizable(False,False)
        self.root.config(bg='white')

        title=Label(self.root,text='Language Translator And Speech',font=("algerian",10),bg="#262626",fg='white').pack(side=TOP,fill=X)

        self.var_content=StringVar()
        self.var_lang=StringVar()
        self.var_lan=StringVar()

        lbl_content=Label(self.root,text='Enter Text:',font=("times new roman",15),bg='white').place(x=10,y=40)
        txt_content=Entry(self.root,textvariable=self.var_content,font=("times new roman",13),bg="#d9fcff").place(x=120,y=40,width=340,height=50)

        lbl_lang=Label(self.root,text='Enter Language To Which We Want To Translate',font=("times new roman",15),bg='white').place(x=10,y=100)
        txt_lang=Entry(self.root,textvariable=self.var_lang,font=("times new roman",13),bg="#d9fcff").place(x=120,y=140,width=340,height=50)

        btn_translate=Button(self.root,text='Translate',command=self.check,font=('times new roman',13),bg='red',fg='white').place(x=60,y=200,width=80,height=50)
        btn_clear=Button(self.root,text='Clear',command=self.clear,font=('times new roman',13),bg='violet',fg='white').place(x=330,y=200,width=80,height=50)

        lbl_translate=Label(self.root,text='Translated Text:',font=("times new roman",15),bg='white').place(x=10,y=260)

        frame_=Frame(self.root,bd=2,relief=RIDGE,bg='#d9fcff')
        frame_.place(x=10,y=300,width=470,height=100)

        self.lbl_trans=Label(frame_,text='',font=("times new roman",18),bg="#d9fcff")
        self.lbl_trans.place(x=0,y=0)

    def check(self):
         if self.var_lang.get()=='english':
             self.var_lan='en'
             translator=Translator(to_lang=self.var_lang.get())
             translation=translator.translate(self.var_content.get())
             sp=gTTS(text=translation,lang=self.var_lan,slow=False)
             filename = 'speech.mp3'
             sp.save(filename)

             music = pyglet.media.load(filename, streaming=False)
             music.play()
               
             self.lbl_trans.config(text=translation)
             sleep(music.duration)
             os.remove(filename) 
         elif self.var_lang.get()=='hindi':
             self.var_lan='hi'
             audio='speech.mp3'
             translator=Translator(to_lang=self.var_lang.get())
             translation=translator.translate(self.var_content.get())
             sp=gTTS(text=translation,lang=self.var_lan,slow=False)
             filename = 'speech.mp3'
             sp.save(filename)

             music = pyglet.media.load(filename, streaming=False)
             music.play()

             self.lbl_trans.config(text=translation)
             sleep(music.duration)
             os.remove(filename) 
         elif self.var_lang.get()=='telugu':
             self.var_lan='te'
             audio='speech.mp3'
             translator=Translator(to_lang=self.var_lang.get())
             translation=translator.translate(self.var_content.get())
             sp=gTTS(text=translation,lang=self.var_lan,slow=False)
             filename = 'speech.mp3'
             sp.save(filename)

             music = pyglet.media.load(filename, streaming=False)
             music.play()
             
             self.lbl_trans.config(text=translation)
             sleep(music.duration)
             os.remove(filename) 
         elif self.var_lang.get()=='malayalam':
             self.var_lan='ml'
             audio='speech.mp3'
             translator=Translator(to_lang=self.var_lang.get())
             translation=translator.translate(self.var_content.get())
             sp=gTTS(text=translation,lang=self.var_lan,slow=False)
             filename = 'speech.mp3'
             sp.save(filename)

             music = pyglet.media.load(filename, streaming=False)
             music.play()

             self.lbl_trans.config(text=translation)
             sleep(music.duration)
             os.remove(filename) 
         elif self.var_lang.get()=='kannada':
             self.var_lan='kn'
             audio='speech.mp3'
             translator=Translator(to_lang=self.var_lang.get())
             translation=translator.translate(self.var_content.get())
             sp=gTTS(text=translation,lang=self.var_lan,slow=False)
             filename = 'speech.mp3'
             sp.save(filename)

             music = pyglet.media.load(filename, streaming=False)
             music.play()

             self.lbl_trans.config(text=translation)
             sleep(music.duration)
             os.remove(filename) 
         elif self.var_lang.get()=='japanese':
             self.var_lan='ja'
             audio='speech.mp3'
             translator=Translator(to_lang=self.var_lang.get())
             translation=translator.translate(self.var_content.get())
             sp=gTTS(text=translation,lang=self.var_lan,slow=False)
             filename = 'speech.mp3'
             sp.save(filename)

             music = pyglet.media.load(filename, streaming=False)
             music.play()

             self.lbl_trans.config(text=translation)
             sleep(music.duration)
             os.remove(filename) 

    def clear(self):
        self.var_lang.set('')
        self.var_content.set('')




root=Tk()
obj=language(root)
root.mainloop()