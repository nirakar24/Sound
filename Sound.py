from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pygame

root=Tk()
#functions
pygame.mixer.init()

def open():
    song = filedialog.askopenfilename(initialdir="C:/Music/",title="Select the music file",filetypes=(("mp3 files", "*.mp3"),))
    # print(root.filename)
    song=song.replace("C:/Music/","")
    song=song.replace(".mp3","")
    lbx.insert(END,song)

def add_songs():
    songs = filedialog.askopenfilenames(initialdir="C:/Music/",title="Select the music file",filetypes=(("mp3 files", "*.mp3"),))
    
    for song in songs:
        song=song.replace("C:/Music/","")
        song=song.replace(".mp3","")
        lbx.insert(END,song)

def close():
    ask=messagebox.askyesno("Exit","Are you sure",icon="warning")
    if ask==1:
        root.destroy()
    else:
        return   
    
def delete():
    lbx.delete(ANCHOR)
    pygame.mixer.music.stop()

def clr():
    lbx.delete(0,END)
    pygame.mixer.music.stop()

def play():
    
    pygame.mixer.music.load(f"C:/Music/{lbx.get(ANCHOR)}.mp3")
    # pygame.mixer.music.set_volume(volume.get())
    pygame.mixer.music.play()

global paused
paused = False
def pause(is_paused):
    global paused
    paused=is_paused

    if paused:
        pygame.mixer.music.unpause()
       
        paused=False

    else:
        pygame.mixer.music.pause()
        paused=True
        #lbx.selection_clear(ACTIVE)

def fwd():
    next_song=lbx.curselection()

    next_song=next_song[0]+1
    song=lbx.get(next_song)
    pygame.mixer.music.load(f"C:/Music/{song}.mp3")
    pygame.mixer.music.play()
    lbx.selection_clear(0, END)
    lbx.activate(next_song)
    lbx.selection_set(next_song, last=None)

def bwd():
    next_song=lbx.curselection()

    next_song=next_song[0]-1
    song=lbx.get(next_song)
    pygame.mixer.music.load(f"C:/Music/{song}.mp3")
    pygame.mixer.music.play()
    lbx.selection_clear(0, END)
    lbx.activate(next_song)
    lbx.selection_set(next_song, last=None)

def about():
 #global sound_img
 run=Toplevel()
 run.title("About")
 run.geometry(f"{670}x{screen_height}")
 run.iconbitmap("music.ico")
 run.configure(bg="#9AC51E")
 fm1=Frame(run,bg="#9AC51E")
 fm1.pack()
 fm2=Frame(run,width=f"{screen_width}")
 fm2.pack()
 lb1=Label(fm1,image=sound_img)
 lb1.pack() 
 lb2=Label(fm2,font=("",14) ,bg="#9AC51E",text="'Sound' is a mp3 player application, which supports Windows operating system\nFor feedback\nContact us: jenashubham60@gmail.com")
 lb2.grid(ipady=20)
 run.mainloop()
  
#Define images
play_img=PhotoImage(file="play.png")
pause_img=PhotoImage(file="pause.png")
fwd_img=PhotoImage(file="bwd.png")
bwd_img=PhotoImage(file="fwd.png")
sound_img=PhotoImage(file="sound.png")

#Creating window
screen_width=600
screen_height=330
root.geometry(f"{screen_width}x{screen_height}")
root.maxsize(screen_width,screen_height)
root.minsize(screen_width,screen_height) 
root.title("Sound")
root.iconbitmap("music.ico")
root.configure(bg="#1A1A1A")

lbx=Listbox(root,border=7,width=23,bg="#9AC51E",font=("",10),relief=GROOVE,selectbackground="#1A1A1A",selectforeground="white",foreground="#1A1A1A") 
lbx.pack(side=RIGHT,fill=Y)

f1=Frame(root,bg="#1A1A1A", height=87, width=100)
f1.pack(side=BOTTOM)
f2=Frame(root,bg="#1A1A1A")
f2.pack(side=LEFT)

illut_label=Label(f2, image=sound_img, borderwidth=0,relief=GROOVE)
illut_label.grid(row=0,column=0,padx=20)

#buttons
b1=Button(f1,image=play_img, command=play, borderwidth=0,background="#1A1A1A",activebackground="#1A1A1A",relief=RAISED)
b3=Button(f1,image=fwd_img, command=fwd, borderwidth=0,background="#1A1A1A",activebackground="#1A1A1A",relief=RAISED)
b4=Button(f1,image=bwd_img, command=bwd, borderwidth=0,background="#1A1A1A",activebackground="#1A1A1A",relief=RAISED)
b2=Button(f1,image=pause_img, command=lambda: pause(paused), borderwidth=0,background="#1A1A1A",activebackground="#1A1A1A",relief=RAISED)

b3.grid(row=0,column=3,padx=10)
b1.grid(row=0,column=1,padx=10)
b2.grid(row=0,column=2,padx=10)
b4.grid(row=0,column=0,padx=10)

# volume=Scale(root,from_=100,to=0,borderwidth=0,bg="grey")
# volume.pack(side=LEFT)

#menu
menubar=Menu(root)
file=Menu(menubar,tearoff=0)
New=Menu(menubar,tearoff=0) 
Help=Menu(menubar,tearoff=0) 
menubar.add_cascade(label="File",menu=file)
menubar.add_cascade(label="New",menu=New)
menubar.add_cascade(label="Help",menu=Help)
New.add_command(label="Add Songs",command=add_songs)    
Help.add_command(label="About",command=about)
file.add_command(label="Clear Playlist",command=clr)
file.add_command(label="Delete",command=delete)

file.add_separator()
file.add_command(label="Exit",command=close)

root.config(menu=menubar)

root.mainloop()