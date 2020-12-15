import sys
sys.path.append("../pygui")


def test_Meta():
    from tkinter import Tk
    from tkinterx.graph.canvas import CanvasMeta
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    self = CanvasMeta(root)
    kw = {
        'color': 'purple',
        'dash': 2,
        'width': 3,
    }
    self.create_graph('line', [20, 20, 100, 200], **kw)
    self.create_graph('oval', [50, 80, 100, 200], fill='red', **kw)
    self.create_graph('rectangle', [170, 80, 220, 200], fill='yellow', **kw)
    self.create_graph('arc', [180, 100, 250, 260],
                      tags='test',
                      fill='lightblue', style='chord', **kw)
    self.create_graph('polygon', [(70, 80), (20, 70),
                                  (30, 90)], fill='purple', **kw)
    self.grid(row=0, column=0)
    print(self.gettags(1))
    print(self.find_withtag('test'))
    root.mainloop()


def test_CanvasMeta():
    from tkinter import Tk
    from tkinterx.graph.canvas import CanvasMeta
    root = Tk()
    root.geometry('350x350')
    self = CanvasMeta(root, background='pink', width=300, height=300)
    self.create_square_point((10, 10), color='blue', width=5)  # 设置点的大小为 7
    self.create_circle_point((20, 20), color='red', width=5)  # 设置点的大小为 7
    self.create_circle((80, 80), radius=40, color='yellow', width=2)
    self.create_circle((180, 180), radius=40,
                       color='yellow', width=2, fill='red')
    self.create_square((80, 100), radius=40, color='red', width=2)
    self.create_square((180, 100), radius=40, color='red',
                       width=2, fill='yellow')
    self.grid(row=0, column=0)
    self.layout(row=1, column=0)
    root.mainloop()


def test_GraphMeta():
    from tkinter import Tk
    from tkinterx.graph.drawing import GraphMeta
    root = Tk()
    root.geometry('750x650')
    self = GraphMeta(root, background='pink', width=600, height=600)
    self.grid(row=0, column=0)
    self.layout(row=1, column=0)
    root.mainloop()


def test_graph():
    from tkinterx.graph.drawing import Drawing
    from tkinter import Tk
    root = Tk()
    self = Drawing(root, width=800, height=600, background='lightgray')
    self.grid(row=0, column=0)
    self.selector_frame.layout(0, 1)
    self.layout(1, 0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()


if __name__ == "__main__":
    #test_Meta()
    #test_CanvasMeta()
    test_GraphMeta()
