from tkinter import *
import numpy as np
import cv2
from tkinter import filedialog
from PIL import ImageTk, Image
import urllib.request

import os

import bar_graphs, bar_graphs_auto
import pie_charts, pie_charts_auto
import scattered
import doughnut


root = Tk()
root.title("Team CodeBenders")
root.iconbitmap(False,"Images/favicon.ico")
root.geometry("600x600")
root.configure(background="black")

global url_
url_ = "http://192.168.1.2:8080"


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("blur.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



e = Example(root)
e.pack(fill=BOTH, expand=YES)


def open(value):
    global type
    type = value
    if exportOption == 0:
        URL = url_
        cam = cv2.VideoCapture(URL + "/video")
        cam.set(3,1280)
        cam.set(4,720)
        cv2.namedWindow("IP Camera")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "Images/Camera/opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                # print("{} written!".format(img_name))
                img_counter += 1

        cam.release()

        cv2.destroyAllWindows()
        if type == 1:
            bar_graphs.original("Images/Camera/opencv_frame_auto_0.png")
        elif type == 2:
            pie_charts.original("Images/Camera/opencv_frame_auto_0.png")
        elif type == 3:
            donut.original("Images/Camera/opencv_frame_auto_0.png")
        elif type == 4:
            scattered.original("Images/Camera/opencv_frame_auto_0.png")



    # global my_Image
    # my_label = Label(root, text=root.filename).pack()
    # my_Image = ImageTk.PhotoImage(Image.open(root.filename))
    # my_image_label = Label(image=my_Image).pack()

    if exportOption == 1:
        root.filename = filedialog.askopenfilename(initialdir="/Images", title="Select a file",
                                                   filetypes=(
                                                       ("png files", "*.png"), ("all files", "*.*"),
                                                       ("jpg files", "*.jpg")))

        if type == 1:
            bar_graphs.original(file_name=root.filename)
        elif type == 2:
            pie_charts.original(file_name=root.filename)
        elif type == 3:
            doughnut.original(file_name=root.filename)
        elif type == 4:
            scattered.original(file_name=root.filename)

def open_auto(value):
    global type
    type = value
    if exportOption == 0:
        URL = url_
        cam = cv2.VideoCapture(URL + "/video")

        cam.set(3, 1280)
        cam.set(4, 720)
        cv2.namedWindow("IP Camera")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "Images/Camera/opencv_frame_auto_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                # print("{} written!".format(img_name))
                img_counter += 1

        cam.release()

        cv2.destroyAllWindows()
        if(type==5):
            bar_graphs_auto.original("Images/Camera/opencv_frame_auto_0.png")
        elif type==6:
            pie_charts_auto.original("Images/Camera/opencv_frame_auto_0.png")



    # global my_Image
    # my_label = Label(root, text=root.filename).pack()
    # my_Image = ImageTk.PhotoImage(Image.open(root.filename))
    # my_image_label = Label(image=my_Image).pack()

    elif exportOption == 1:
        root.filename = filedialog.askopenfilename(initialdir="/Images", title="Select a file",
                                               filetypes=(
                                                   ("png files", "*.png"), ("all files", "*.*"),
                                                   ("jpg files", "*.jpg")))

        if type == 5:
            bar_graphs_auto.original(file_name=root.filename)
        elif type == 6:
            pie_charts_auto.original(file_name=root.filename)


#
# def clicked(value):
#     global type
#     type = value



def setExportOption(value):
    global exportOption
    exportOption=value

pic = Image.open("head.png")
photo = ImageTk.PhotoImage(pic)

img=Image.open("Images/ca.png")
photoimage_ = img.resize((50,50), Image.ANTIALIAS)
photoimageCam = ImageTk.PhotoImage(photoimage_)

img=Image.open("Images/file.jpg")
photoimage_ = img.resize((50,50), Image.ANTIALIAS)
photoimageFile = ImageTk.PhotoImage(photoimage_)

e = Label(root,image=photo).place(x=50,y=5)
Button(root, text="Export from Camera", width=200, image = photoimageCam, compound=LEFT,command=lambda: setExportOption(0)).place(x=100,y=50+50)
Button(root, text="Export from File Directory", width=200,image = photoimageFile, compound=LEFT, command=lambda: setExportOption(1)).place(x=330,y=50+50)

img=Image.open("Images/stats.png")
photoimage_ = img.resize((50,50), Image.ANTIALIAS)
photoimage1 = ImageTk.PhotoImage(photoimage_)
img=Image.open("Images/pie-chart.png")
photoimage_ = img.resize((50,50), Image.ANTIALIAS)
photoimage2 = ImageTk.PhotoImage(photoimage_)
img=Image.open("Images/scatter-graph.png")
photoimage_ = img.resize((50,50), Image.ANTIALIAS)
photoimage3 = ImageTk.PhotoImage(photoimage_)
img=Image.open("Images/representation.png")
photoimage_ = img.resize((50,50), Image.ANTIALIAS)
photoimage4 = ImageTk.PhotoImage(photoimage_)

# img=PhotoImage(file = r"1.png")
# photoimage2 = img
# img=PhotoImage(file = r"ScatterShort.png")
# photoimage3 = img
# img=PhotoImage(file = r"doughNut.png")
# photoimage4 = img

# Button(root, text="Bar Chart", padx=40, pady=20, image = photoimage, compound = LEFT, command=lambda: open(1)).grid(row=2, column=0)
# Button(root, text="Pie Chart", padx=40, pady=20,image = photoimage, compound = LEFT, command=lambda: open(2)).grid(row=2, column=1)
# Button(root, text="Donut", padx=40, pady=20,image = photoimage, compound = LEFT, command=lambda: open(3)).grid(row=2, column=2)
# Button(root, text="Scatter Plot", padx=40, image = photoimage, compound = LEFT,pady=20, command=lambda: open(4)).grid(row=2, column=3)
# myButton = Button(root, text="OK", command=lambda: clicked(r.get())).pack()
Button(root, text="Bar Chart",width=150,  image = photoimage1, compound = LEFT, command=lambda: open(1)).place(x=130, y=120+50)
Button(root, text="Bar Chart Automatic",width=175,  image = photoimage1, compound = LEFT, command=lambda: open_auto(5)).place(x=330, y=120+50)
Button(root, text="Pie Chart",width=150,  image = photoimage2, compound = LEFT, command=lambda: open(2)).place(x=130, y=220+50)
Button(root, text="Pie Chart Automatic",width=175,  image = photoimage2, compound = LEFT, command=lambda: open_auto(6)).place(x=330, y=220+50)
Button(root, text="DoughNut Chart",width=150, image = photoimage4, compound = LEFT, command=lambda: open(3)).place(x=130, y=320+50)
Button(root, text="Scatter Chart",width=150,  image = photoimage3, compound = LEFT, command=lambda: open(4)).place(x=130, y=420+50)




# print(r.get())


# open_file = Button(root, text="Open Graph Image", command=open).pack()
button_quit = Button(root, text="Export To Excel", command=root.quit)
button_quit.place(x=430, y=420)

root.mainloop()
if type == 1:
    os.system("out_bar.xlsx")
elif type == 2:
    os.system("out_pie.xlsx")
elif type == 3:
    os.system("out_donut.xlsx")
elif type == 4:
    os.system("out_scatter.xlsx")
elif type == 5:
    os.system("out_bar_auto.xlsx")
elif type == 6:
    os.system("out_pie_auto.xlsx")
