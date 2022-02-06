#import and install the required modules for this project

from cProfile import label
from cgitb import text
from tkinter import font
from turtle import width
from pytube import YouTube
from tkinter import *

#instantiate the tkinter class by creating an object 
draw = Tk()
draw.geometry('500x300')
draw.resizable(0,0)
draw.title("welcome, please enter the link to download")
label(draw, text="Download_me", font = 'Roboto 15 Bold').pack()

#a varibale to store the link
link = StringVar()
#label to show paste here 
Label(draw, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
#the text field to input the link for downloads 
link_box = Entry(draw, width=100, textplace_holder = link).place(x = 35, y = 90)
#function to download

def Download_me():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(draw, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
    Button(draw,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Download_me).place(x=180 ,y = 150)
    draw.mainloop()