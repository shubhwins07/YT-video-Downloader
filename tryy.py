# from pytube import YouTube
# import os

# user = os.getlogin()

# yt = YouTube("https://youtu.be/5DxcrGJrW_g?si=-aKL2V_j0YRgU2M9")

# def check_if_avail(itagg):

#     aud = yt.streams.get_by_itag(itagg)
#     return aud


# print(yt.streams.filter(res="1080p"))
import customtkinter
from PIL import Image
from tkinter import PhotoImage
from pytube import YouTube
import threading
import time

yt = YouTube("https://youtu.be/mIUoRP6oWuA?si=2OcsAqu-SjGUSrt-")

app = customtkinter.CTk(fg_color="white")
app.geometry("600x600")
# Themes: blue (default), dark-blue, green
frame = customtkinter.CTkFrame(master=app, fg_color="black", width=600, height=600)
frame.place(relx=0, rely=0)

gifloader = Image.open("yt.gif")
loadframes = gifloader.n_frames
imgObj = [
    PhotoImage(file="yt.gif", format=f"gif -index {i}") for i in range(loadframes)
]
count = 0
showanimation = None

loader = customtkinter.CTkLabel(
    master=frame,
    text="",
    image="",
    width=300,
    height=300,
    bg_color="black"
)
Loading = customtkinter.CTkLabel(
    master=frame,
    font=("Poppins Black", 27.5),
    text="Sometimes, a buffer is important...",
    text_color="white",
)
lol = customtkinter.CTkLabel(
    master=frame,
    font=("Poppins", 15),
    text="noo, believe me, I am Serious!",
    text_color="#444444",
)


def animation(count):
    global showanimation
    newImage = imgObj[count]
    if count == loadframes - 1:
        count = 0
    loader.configure(image=newImage)
    count += 1

    showanimation = app.after(50, lambda: animation(count))



def animestrt():
    loader.place(relx=0.2375, rely=0.15)
    Loading.place(relx=0.09, rely=0.8)
    lol.place(relx=0.09, rely=0.86)
    animation(count)





def clearwindow():
    for child in app.winfo_children():
        child.destroy()



def check_if_avail(itagg):

    aud = yt.streams.get_by_itag(itagg)
    return aud


diff_itags = [160, 133, 18, 135, 22, 335, 336, 337, 313, 271, 248, 140, 251]
results = []

def func():
    for itagg in diff_itags:
        check = check_if_avail(itagg)
        if check == None:
            results.append(False)
        else:
            results.append(True)
    print(results)
    print("done")
    


process = threading.Thread(name="process",target=func)

process.start()

animestrt()

app.after(5000,clearwindow)
    
app.mainloop()