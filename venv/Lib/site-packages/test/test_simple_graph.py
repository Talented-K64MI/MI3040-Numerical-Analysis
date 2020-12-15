import sys
sys.path.append(r"D:\study\pygui")

from tkinterx.graph.canvas_design import SimpleGraph
from tkinter import Tk


if __name__ == "__main__":
    root = Tk()
    self = SimpleGraph(root, 'rectangle', 'red')
    self.add_row([15, 15, 40, 40], 10)
    self.add_column([15, 45, 40, 80], 5)
    self.create_square((200, 120), 50)
    self.create_circle((150, 120), 50)
    self.create_square_point((150, 130), width=10)
    self.grid()
    root.mainloop()
