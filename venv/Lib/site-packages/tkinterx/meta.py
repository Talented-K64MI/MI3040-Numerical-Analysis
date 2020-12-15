from tkinter import Toplevel, ttk, Tk
from tkinter import filedialog, StringVar, messagebox, IntVar


def askokcancel(window, title='Do You need to exit?', message=None):
    if messagebox.askokcancel(title, message):
        window.destroy()
    else:
        window.deiconify()


def showwarning(window, title='Warning', message='Please check your input'):
    if messagebox.showwarning(title, message):
        window.deiconify()


def ask_filename(key):
    if 'path' in key:
        name = filedialog.askopenfilename()
    elif 'dir' in key:
        name = filedialog.askdirectory()
    return name


class TextMeta:
    def __init__(self, master, ttk_type, **kw):
        '''
        :param ttk_type: 'ttk.Combobox', 'ttk.Label',  'ttk.Entry',
            'ttk.Menubutton', 'ttk.Spinbox', 'ttk.Button'
        '''
        self.var = StringVar()
        self.entry = ttk_type(master, textvariable=self.var, **kw)

    def __repr__(self):
        return self.var.get()


class Row(TextMeta):
    def __init__(self, master, ttk_type, text, var_type='str', **kw):
        '''
        :param ttk_type: 'ttk.Combobox', 'ttk.Label',  'ttk.Entry',
            'ttk.Menubutton', 'ttk.Spinbox', 'ttk.Button'
        '''
        super().__init__(master, ttk_type, **kw)
        if var_type == 'int':
            self.var = IntVar()
        else:
            self.var = StringVar()
        self.label = ttk.Label(master, text=text)
        self.entry = ttk_type(master, textvariable=self.var, **kw)

    def layout(self, row=0, **kw):
        self.label.grid(row=row, column=0, **kw)
        self.entry.grid(row=row, column=1, **kw)


class Table(dict):
    '''

    Example
    ======================
    from tkinter import Tk
    from tkinterx.meta import Table
    root = Tk()
    table = Table(root)
    table.add_row('name', '姓名')
    table.add_row('age', '年龄')
    table.add_row('path', '保存路径', width=30)
    table.layout()
    root.mainloop()
    '''

    def __init__(self, master, *args, **kw):
        super().__init__(*args, **kw)
        self.master = master

    def bind_filename(self, event, key):
        name = ask_filename(key)
        self[key].var.set(name)

    def add_row(self, key, text, **kw):
        row = Row(self.master, ttk.Entry, text, **kw)
        if 'path' in key or 'dir' in key:
            row.label.bind('<1>', lambda event: self.bind_filename(event, key))
        self[key] = row

    def layout(self, row=0, **kw):
        for n_row, (key, widget) in enumerate(self.items()):
            widget.layout(row+n_row, **kw)

    def todict(self):
        return {key: str(value) for key, value in self.items()}


class WindowMeta(Toplevel):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.table = Table(self)
        self.ok_button = ttk.Button(self, text='OK', command=self.run)
        self.create_widget()
        self.layout()

    def add_row(self, text, key, **kw):
        self.table.add_row(key, text, **kw)

    def layout(self):
        self.table.layout()
        self.ok_button.grid(sticky='we')

    def run(self):
        NotImplemented

    def create_widget(self):
        NotImplemented


def ask_window(tk_root, window_type):
    '''Pass information through a window
    :param tk_root: An instance of a Tk or an instance of its subclass
    :param window_type: WindowMeta or its subclasses
    '''
    window = window_type(tk_root)
    window.transient(tk_root)
    tk_root.wait_window(window)
    return window.table


class PopupLabel(WindowMeta):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

    def create_widget(self):
        self.add_row('Please enter the label: ', 'label')

    def run(self):
        self.withdraw()
        label = self.table['label']
        if '' in [label]:
            showwarning(self)
        else:
            pass
            #askokcancel(self, message='Do you want to confirm the submission?')
