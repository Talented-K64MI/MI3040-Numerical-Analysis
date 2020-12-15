from pathlib import Path
import json
from tkinter import ttk, StringVar


def save_bunch(bunch, path):
    with open(path, 'w') as fp:
        json.dump(bunch, fp)


def load_bunch(path):
    with open(path) as fp:
        bunch = json.load(fp)
    return bunch


def mkdir(root_dir):
    '''依据给定名称创建目录'''
    path = Path(root_dir)
    if not path.exists():
        path.mkdir()


class FileFrame(ttk.LabelFrame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.save_button = ttk.Button(self, text='Save')
        self.load_button = ttk.Button(self, text='Load')
        self.layout(row=0)

    def layout(self, row=0):
        self.load_button.grid(row=row, column=0)
        self.save_button.grid(row=row, column=1)


class GridLayout:
    def __init__(self, master=None, **kw):
        NotImplemented

    def layout_row(self, row=0, *row_widget):
        '''
        row > 0
        '''
        for column, widget in enumerate(row_widget):
            widget.grid(row=row, column=column)

    def layout(self, row_widgets, start=0):
        for row, row_widget in enumerate(row_widgets):
            self.layout_row(row+start, *row_widget)


class FileNotebook(ttk.Notebook, GridLayout):
    def __init__(self, master=None, **kw):
        '''
        Example
        =============
        root = Tk()
        self = FileNotebook(root, width=200, height=100, padding=(5, 5, 5, 5))
        self.add_frame([['Load', 'Save'], ['Prev', 'Next']], 'Image', start=0)
        self.add_frame([['Load', 'Save']], 'Annotation', start=0)
        self.grid()
        root.mainloop()
        '''
        super().__init__(master, **kw)

    def add_row_button(self, frame, *names):
        return [ttk.Button(frame, text=name)for name in names]

    def add_frame(self, names, tab_name, start=0):
        frame = ttk.Frame(self)
        widgets = [self.add_row_button(frame, *name) for name in names]
        self.add(frame, text=tab_name)
        self.layout(widgets, start)
        return frame, widgets
        