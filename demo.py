import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo,showwarning
from tkinter.filedialog import askdirectory


add=" "
def file_path():
    global add
    add=askdirectory()
   
def save_file():
    global add
    try:
        time=int(sec.get())
        addr=add+"/"+"demo.wav"
        showinfo(title="Start",message="Rec Start")
        rece= sounddevice.rec(time*44100,samplerate=44100,channels=2)
        sounddevice.wait()
        write(addr,44100,rece)
        showinfo(title="End",message="Rec Stop")

    except:
        showwarning(title="Time",message="Wrong Format of Time")
def main_window():
    global sec
    win=Tk()
    win.geometry("500x700")
    win.resizable(False,False)
    win.title("Bhavish Makkar")
    win.config(bg="black")
    
    
    img1=PhotoImage(file="wa.png")
    l1=Label(win,image=img1)
    l1.place(x=50, y=20, width=400, height=150)
    
    sec=Entry(win,font=(20))
    sec.place(x=100, y=180, width=300, height=50)
    l2=Label(win,text="Time In Sec.",font=("Time New Roman",20),bg="blue")
    l2.place(x=100, y=240, width=300, height=50)  
    
    b=Button(win,text="Path",font=("Time New Roman",20),command=file_path)
    b.place(x=150,y=300,height=30,width=200)
    
    img2=PhotoImage(file="project.png")
    
    
    
    start= Button(win,image=img2,height=150,width=200,command=save_file)
    start.place(x=150,y=340)
    win.mainloop()
main_window()
# def savefile(sec):
#     print("start")
#     rece= sounddevice.rec(sec*44100,samplerate=44100,channels=2)
#     sounddevice.wait()
#     write("demo.wave",44100,rece)
#     print("end")
    
# savefile(10)