import argparse
import tkinter as tk
from PIL import ImageTk, Image

class Application(tk.Frame):
    def __init__(self, master=None, imgPath=""):
        super().__init__(master)
        self.imgPath = imgPath
        self.pack()
        self.create_widgets(self.imgPath)


    def create_widgets(self, imgPath):
        self.img = ImageTk.PhotoImage(Image.open(imgPath))
        self.imgPanel = tk.Label(image = self.img)
        self.imgPanel.pack(side="top")

        self.prev = tk.Button(self)
        self.prev["text"] = "<"
        self.prev["command"] = self.prev_img
        self.prev.pack(side="left")

        self.next = tk.Button(self)
        self.next["text"] = ">"
        self.next["command"] = self.next_img
        self.next.pack(side="right")


    def prev_img(self):
        print("Loading Prev Image")


    def next_img(self):
        print("Loading Next Image")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="file location of img")
    args = parser.parse_args()

    root = tk.Tk()
    root.title("Pimg - Python IMG viewer")
    root.geometry("600x400")
    app = Application(master=root, imgPath=args.path)
    app.mainloop()
