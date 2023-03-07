import pygame
import tkinter as tk
from PIL import Image, ImageTk
from threading import Thread
class Window:
    def __init__(self, height, width, title="Test", icon=None):
        self.title = title
        self.height = height
        self.width = width
        self.icon = icon

        self.window = None
        self.elements = None

        self.visible = False

    def createWindow(self):
        window = tk.Tk()
        window.title(self.title)

        if self.icon != None:
            try:
                window.wm_iconphoto(False, ImageTk.PhotoImage(Image.open(self.icon)))
            except:
                self.icon = None

        if self.width != -1:
            window.geometry(str(self.width)+"x"+str(self.height))
        else:
            window.attributes('-fullscreen', True)

        self.window = window

    def __run(self, window):
        while self.visible == True:
            print(self.visible)
            self.window.update()

    def showWindow(self):
        if self.window != None and self.visible == False:
            self.visible = True

            t = Thread(target=self.__run, args=(self.window,))
            t.daemon = True
            t.start()

    def hiddeWindow(self):
        if self.visible == True:
            self.window.destroy()
            self.visible = False