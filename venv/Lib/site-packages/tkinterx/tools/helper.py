from tkinter import ttk, StringVar


class StatusTool(ttk.Frame):
    def __init__(self, master, text, **kw):
        super().__init__(master, **kw)
        self.head_label = ttk.Label(self, text=text)
        self.var = StringVar()
        self.label = ttk.Label(self, textvariable=self.var,
                               relief='sunken', anchor='w')
        self.layout()

    def layout(self):
        self.head_label.grid(row=0, column=0)
        self.label.grid(row=0, column=1)
