import tkinter as tk
import pandas as pd
import os
import datetime

# Reschedule event in 30 seconds
TIME_DELAY = 1000*10

def root_dir():
    return os.path.dirname(os.path.abspath(__file__))




class GUI():
    """
    Learing Kanada app 
    """
    def __init__(self):
        self.data = pd.read_csv(os.path.join(root_dir(),"kanada.yml"), delimiter=":", header=None)
        self.sample_data  = self.data #.sample(25)
        self.root = tk.Tk()
        self.init()

    def init(self):
        eng, kan = self._get_text()
        self.label = tk.Label(self.root, text=eng)
        self.label2 = tk.Label(self.root, text=kan)
        self.label.pack(padx=30, pady=10)
        self.label2.pack(padx=30, pady=10)

        self.root.title("Learn K")
        self.root.geometry("%dx%d-%d-%d" % (300, 100, 0, 750))
        self.root.resizable(0, 0)

    def _increment_counter(self):
        eng, kan = self._get_text()
        self.label["text"] = eng
        self.label2["text"] = kan
        self.root.after(TIME_DELAY, self._increment_counter)

    def _get_text(self):
        d = self.sample_data.sample(1)
        return d[0].values.tolist()[0], d[1].values.tolist()[0]


    def run(self):
        self.root.after(TIME_DELAY, self._increment_counter)
        self.root.mainloop()

def main():
    gui=GUI()
    gui.run()

if __name__ =="__main__":
    main()