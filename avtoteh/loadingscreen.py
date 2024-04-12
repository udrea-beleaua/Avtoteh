from tkinter import *
from PIL import Image
import mainwindow

def loadingscreen():
    def main_window():
        splash.destroy()
        mainwindow.mainwindow()
        


    splash = Tk()
    height = 500
    width = 500
    x = (splash.winfo_screenwidth() // 2) - (width // 2)
    y = (splash.winfo_screenheight() // 2) - (height // 2)
    splash.geometry('{}x{}+{}+{}'.format(width, height, x, y))


    backgroundImage = PhotoImage(file='Project.png')
    bg_image = Label(
        splash,
        image=backgroundImage
    )
    bg_image.pack()

    splash.overrideredirect(True)

    gifImage = 'Loading.gif'
    openImage = Image.open(gifImage)
    frames = openImage.n_frames
    imageObject = [PhotoImage(file=gifImage, format=f'gif -index {i}') for i in range(frames)]

    count = 0
    showAnimation = None


    def animation(count):
        nonlocal showAnimation
        newImage = imageObject[count]

        gif_Label.configure(image=newImage)
        count += 1
        if count == frames:
            count = 0
        showAnimation = splash.after(50, lambda: animation(count))



    gif_Label = Label(splash, image='')
    gif_Label.place(x=150, y=220, width=200, height=200)


    text_label = Label(splash, text="Getting everything ready for ya!", font=("Arial", 12), bg="#16161a", fg="#2cb67d")
    text_label.place(relx=0.5, rely=0.8, anchor="center")

    splash.after(3000, main_window)

    animation(count)
    splash.mainloop()
