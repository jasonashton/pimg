import argparse
import tkinter as tk
from PIL import ImageTk, Image

class Application(tk.Frame):
    def __init__(self, master=None, imgPath=""):
        super().__init__(master)
        self.imgPath = tk.StringVar()
        self.imgPath.set(imgPath)
        self.pack()
        self.create_widgets()




    def create_widgets(self):
        self.img = ImageTk.PhotoImage(Image.open(self.imgPath.get()))
        self.imgPanel = tk.Label(image = self.img)
        self.imgPanel.pack(side="top")


        self.test = tk.Label(self)
        self.test["textvariable"] = self.imgPath
        self.test.pack(side="top")

        self.prev = tk.Button(self)
        self.prev["text"] = "<"
        self.prev["command"] = lambda: self.update_img("images/barn.jpg")
        self.prev.pack(side="left")

        self.next = tk.Button(self)
        self.next["text"] = ">"
        self.next["command"] = lambda: self.update_img("images/mountain.jpg")
        self.next.pack(side="right")


    def update_img(self,img):
        print("Loading Image: {}".format(img))
        self.imgPath.set(img)
        self.img = ImageTk.PhotoImage(Image.open(self.imgPath.get()))
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
