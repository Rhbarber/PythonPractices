from tkinter import *
from tkinter import messagebox as MessageBox

from pytube import YouTube


def fetch():
    link = videos.get()
    video = YouTube(link)
    download = video.streams.get_highest_resolution()
    download.download()


def popup():
    MessageBox.showinfo("Inspired by", "https://github.com/Maalfer/Youtube_Downloader")


root = Tk()
root.config(bd=15)
root.title("YouTube Downloader")

image = PhotoImage(file="Data/icon.png")
photo = Label(root, image=image, bd=0)
photo.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="More Info", menu=helpmenu)
helpmenu.add_command(label="Author's Info", command=popup)

menubar.add_command(label="Exit", command=root.destroy)

instructions = Label(root, text="Paste YouTube link on here!")
instructions.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

button = Button(root, text="Download :)", command=fetch)
button.grid(row=2, column=1)

root.mainloop()
