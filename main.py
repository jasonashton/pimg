import argparse
import os, sys
import tkinter as tk
from PIL import ImageTk, Image

class Application(tk.Frame):
    def __init__(self, master=None, imgPath=""):
        super().__init__(master)

        self.imgPath = imgPath

        self.multiple = os.path.isdir(imgPath)
        self.pos = 0

        if self.multiple:
            self.imgList = os.listdir(imgPath)
        else:
            self.imgList = [imgPath]

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        if self.multiple:
            self.img = ImageTk.PhotoImage(Image.open("{}{}".format(self.imgPath, self.imgList[0])))
        else:
            self.img = ImageTk.PhotoImage(Image.open("{}".format(self.imgPath)))
        self.imgPanel = tk.Label(image = self.img)
        self.imgPanel.pack(side="top")

        self.name = tk.Label(self)
        self.name["textvariable"] = str(self.imgList[0])
        self.name.pack(side="top")

        if self.multiple:
            self.prev = tk.Button(self)
            self.prev["text"] = "<"
            self.prev["command"] = lambda: self.update_img(-1)
            self.prev.pack(side="left")

            self.next = tk.Button(self)
            self.next["text"] = ">"
            self.next["command"] = lambda: self.update_img(1)
            self.next.pack(side="right")



    def update_img(self, dir):
        self.pos = (self.pos + (1 * dir)) % len(self.imgList)
        img = self.imgList[self.pos]

        print("Loading Image: {}".format(str(img)))
        self.img = ImageTk.PhotoImage(Image.open("{}{}".format(self.imgPath, img)))
        self.imgPanel.configure(image = self.img)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="file location of img")
    args = parser.parse_args()

    root = tk.Tk()
    root.title("Pimg - Python IMG viewer")
    root.geometry("600x400")
    app = Application(master=root, imgPath=args.path)
    app.mainloop()
