from tkinter import Tk, ttk, StringVar, Toplevel


class Table(ttk.Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.bunch = {}
        
    def add_radio(self, key, text, value):
        var = StringVar(name=key)
        kw = {
            'text': text,
            'variable': var,
            'value': value
        }
        self.bunch[key] = var
        return ttk.Radiobutton(self, **kw)
    
    def create_widgets(self, data_bunch):
        widgets = []
        for key, value in data_bunch.items():
            label = ttk.Label(self, text=key, foreground='green')
            widgets.append([label]+[self.add_radio(key, k, v) for k, v in value.items()])
        return widgets
            
    def layout(self, widgets):
        for row, row_widgets in enumerate(widgets):
            for column, widget in enumerate(row_widgets):
                widget.grid(row=row, column=column)
                
    def todict(self):
        return {key:value.get() for key, value in self.bunch.items()}

    
class AskValueWindow(Toplevel):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.table = Table(self)
        self.ok_button = ttk.Button(self, text='OK', command=self.run)
        self.bunch = {
            'name': {'car': '汽车', 'bus': '公交车', 'truck': '卡车'},
            'color': {'red': '红色', 'blue': '蓝色', 'green': '绿色'}
        }
        self.layout()
        self.output = {}
        
    def layout(self):
        widgets = self.table.create_widgets(self.bunch)
        self.table.grid(row=0, column=0, sticky='we')
        self.table.layout(widgets)
        self.ok_button.grid(row=1, column=0, sticky='we')

    def run(self):
        self.output.update(self.table.todict())

        
def ask_window(tk_root, window_type):
    '''Pass information through a window
    :param tk_root: An instance of a Tk or an instance of its subclass
    :param window_type: WindowMeta or its subclasses
    '''
    window = window_type(tk_root)
    window.transient(tk_root)
    tk_root.wait_window(window)
    return window.table


class App(Tk):
    def __init__(self):
        super().__init__()
        style = ttk.Style()
        style.configure("C.TButton",
                        foreground="green",
                        background="white",
                        relief='raise',
                        justify='center',
                        font=('YaHei', '15', 'bold'))
        self.create_button = ttk.Button(self,
                                      text='生成 标签',
                                      command=self.ask_value,
                                      style="C.TButton")

    def ask_value(self):
        window = AskValueWindow(self)
        window.title('标签 工具')
        window.transient(self)
        self.wait_window(window)
        print(window.output)

    def layout(self):
        self.create_button.place(x=50, y=50)

        
if __name__ == "__main__":
    root = App()
    root.layout()
    root.mainloop()