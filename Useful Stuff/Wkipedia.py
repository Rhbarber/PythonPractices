import tkinter as tk

import wikipedia


def search():
    content = search_box.get()
    result = wikipedia.summary(content, sentences=2)
    T.delete(1.0, tk.END)
    T.insert(tk.END, result)


window = tk.Tk()
window.geometry("300x300")
search_box = tk.Entry(window)
search_box.place(x=0, y=0)
search_box.bind("<Return>", search)
T = tk.Text(window)
search_box.pack()
T.pack()
T.insert(tk.END, "Test")
