from pytube import YouTube
import urllib.request
import customtkinter
from PIL import Image, ImageDraw
import os


# Modes: system (default), light, dark
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk(fg_color="#ecedff")
app.geometry("480x100")
app.title("YT Video Downloader")
app.iconbitmap("yt_icon.ico")
app.maxsize(480, 100)
app.minsize(480, 100)
app.bind_all("<Button-1>", lambda event: event.widget.focus_set())

gobutt_img = customtkinter.CTkImage(
    light_image=Image.open("youtube.png"),
    dark_image=Image.open("youtube.png"),
    size=(32, 32),
)
retry = customtkinter.CTkImage(
    light_image=Image.open("reloading.png"),
    dark_image=Image.open("reloading.png"),
    size=(32, 32),
)
downloadd = customtkinter.CTkImage(
    light_image=Image.open("download.png"),
    dark_image=Image.open("download.png"),
    size=(32, 32),
)
gobutt_imgey = customtkinter.CTkImage(
    light_image=Image.open("youtube (2).png"),
    dark_image=Image.open("youtube (2).png"),
    size=(32, 32),
)


def add_corners(im, rad):
    circle = Image.new("L", (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new("L", im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


def download_window():
    # storing url before forgetting
    urll = str(url.get())
    print(urll)

    def check_if_avail(itagg):

        aud = yt.streams.get_by_itag(itagg)
        return aud

    try:
        if urll != "":
            # storing thumbnail for future use
            yt = YouTube(urll)
            thumb_url = yt.thumbnail_url

            vid_title = yt.title
            if len(vid_title) > 50:
                vid_title = vid_title[0:51] + "..."

            urllib.request.urlretrieve(thumb_url, "thumb.png")
            thumbnail = Image.open("thumb.png")
            thumbnail = add_corners(thumbnail, 30)

            thumbnail_final = customtkinter.CTkImage(
                light_image=thumbnail, dark_image=thumbnail, size=(320, 180)
            )

            def open_strt():
                app.deiconify()
                dnld.destroy()
                url.delete(0, customtkinter.END)

            dnld = customtkinter.CTkToplevel(fg_color="#ecedff")
            dnld.geometry("600x600")
            dnld.title("YT Video Downloader")
            dnld.after(250, lambda: dnld.iconbitmap("yt_icon.ico"))
            dnld.maxsize(600, 600)
            dnld.minsize(600, 600)

            bg = customtkinter.CTkFrame(
                master=dnld,
                width=500,
                height=540,
                corner_radius=10,
                border_color="white",
                border_width=2,
                fg_color="#f8f9fe",
                bg_color="#ecedff",
            )
            bg.place(relx=0.085, rely=0.05)

            img = customtkinter.CTkLabel(
                master=bg,
                width=320,
                height=180,
                text="",
                image=thumbnail_final,
                bg_color="#f8f9fe",
            )
            img.place(relx=0.185, rely=0.04)

            title = customtkinter.CTkButton(
                master=bg,
                width=450,
                height=30,
                bg_color="#f8f9fe",
                fg_color="#f8f9fe",
                hover=False,
                text=vid_title,
                text_color="black",
                font=("Poppins Black", 15),
            )
            title.place(relx=0.044, rely=0.39)

            dnlds = customtkinter.CTkScrollableFrame(
                master=bg,
                width=425,
                height=10,
                corner_radius=10,
                border_color="white",
                border_width=2,
                bg_color="#f8f9fe",
                fg_color="#ecedff",
                scrollbar_button_color="#f8f9fe",
                scrollbar_fg_color="#ecedff",
                scrollbar_button_hover_color="white",
            )
            dnlds.place(relx=0.044, rely=0.463)

            # 144p
            onefourfourp = customtkinter.CTkFrame(
                master=dnlds,
                width=425,
                height=50,
                corner_radius=10,
                border_color="white",
                border_width=2,
                bg_color="#ecedff",
                fg_color="#f8f9fe",
            )
            onefourfourpquality = customtkinter.CTkLabel(
                master=onefourfourp,
                height=50,
                width=50,
                text="144p",
                bg_color="#f8f9fe",
                fg_color="#f8f9fe",
                text_color="black",
                font=("Poppins Black", 15),
            )
            onefourfourptype = customtkinter.CTkLabel(
                master=onefourfourp,
                height=50,
                width=50,
                text="mp4",
                bg_color="#f8f9fe",
                fg_color="#f8f9fe",
                text_color="black",
                font=("Poppins Black", 15),
            )
            onefourfourpdownld = customtkinter.CTkButton(
                master=onefourfourp,
                width=35,
                height=45,
                corner_radius=10,
                border_color="white",
                border_width=2,
                fg_color="#ecedff",
                bg_color="#f8f9fe",
                hover_color="#f8f9fe",
                text="",
                image=downloadd,
            )

            diff_itags = [160, 133, 18, 135, 22, 337, 336, 335, 140, 251]
            results = []

            # filling results
            for itagg in diff_itags:
                check = check_if_avail(itagg)
                if check == None:
                    results.append(False)
                else:
                    results.append(True)
            print(results)

            if results[0] == True:
                onefourfourp.pack(pady=0)
                onefourfourpquality.place(relx=0.01)
                onefourfourptype.place(relx=0.43)
                onefourfourpdownld.place(relx=0.86, rely=0.05)

            tryagain = customtkinter.CTkButton(
                master=dnld,
                width=120,
                command=open_strt,
                height=40,
                corner_radius=10,
                border_color="white",
                border_width=2,
                fg_color="#ecedff",
                bg_color="#f8f9fe",
                hover_color="#f8f9fe",
                text="Another One?",
                image=retry,
                font=("Poppins Black", 14),
                text_color="red",
            )
            tryagain.place(relx=0.357, rely=0.863)

            app.withdraw()

        else:
            url.delete(0, customtkinter.END)
            url.configure(placeholder_text="    Please Enter A Valid Youtube URL")

    except Exception as e:

        url.delete(0, customtkinter.END)
        url.configure(placeholder_text="    Please Enter A Valid Youtube URL")
        print(f"An Error Occured --> {e}")


fg = customtkinter.CTkLabel(
    master=app,
    width=460,
    height=75,
    corner_radius=0,
    fg_color="#ecedff",
    text="",
    bg_color="#ecedff",
)
fg.place(relx=0.0225, rely=0.1)


url = customtkinter.CTkEntry(
    master=fg,
    width=385,
    height=60,
    corner_radius=7.5,
    bg_color="#ecedff",
    border_width=2,
    border_color="#ffffff",
    text_color="#ff0000",
    fg_color="#f8f9fe",
    placeholder_text="    Enter Video URL",
    placeholder_text_color="#ff0000",
    font=("Poppins Black", 15),
)
url.place(relx=0.014, rely=0.125)


gobutt = customtkinter.CTkButton(
    master=fg,
    text="",
    command=download_window,
    fg_color="#f8f9fe",
    border_color="white",
    hover_color="#ecedff",
    border_width=2,
    bg_color="#ecedff",
    width=60,
    height=60,
    corner_radius=7.5,
    image=gobutt_img,
)
gobutt.place(relx=0.86, rely=0.125)


app.mainloop()
