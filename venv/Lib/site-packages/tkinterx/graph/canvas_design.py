from tkinter import ttk, colorchooser, StringVar

from ..param import ParamDict
from .canvas import CanvasMeta


class SimpleGraph(CanvasMeta):
    color = ParamDict()
    shape = ParamDict()
    fill = ParamDict()
    width = ParamDict()

    def __init__(self, master, shape, color, width=1, fill=None, cnf={}, **kw):
        '''The base class of all graphics frames.

        :param shape: 'rectangle', 'oval', 'line', 'arc'(That is, segment), 'polygon'.

        Example
        ============
        from tkinter import Tk
        from tkinterx.graph.canvas_design import SimpleGraph
        root = Tk()
        self = SimpleGraph(root, 'rectangle', 'yellow', width=1, fill=None, background='pink')
        self.add_row([25, 25, 40, 40], 10, 20)
        self.fill = 'blue'
        self.add_column([40, 80, 100, 100], 5, 30, tags='TY')
        self.grid(row=0, column=0)
        root.mainloop()
        '''
        super().__init__(master, cnf, **kw)
        self.color = color
        self.shape = shape
        self.width = width
        self.fill = fill

    def draw(self, direction, tags=None, **kw):
        return self.create_graph(self.shape, direction, self.color, self.width, tags, fill=self.fill, **kw)

    @property
    def default_tags(self):
        return f"graph {self.color} {self.shape}"

    def add_row(self, direction, num, stride=10, tags=None, **kw):
        x0, y0, x1, y1 = direction
        for _ in range(num):
            x0 += stride
            x1 += stride
            direction = (x0, y0, x1, y1)
            self.draw(direction, tags, **kw)

    def add_column(self, direction, num, stride=5, tags=None, **kw):
        x0, y0, x1, y1 = direction
        for _ in range(num):
            y0 += stride
            y1 += stride
            direction = (x0, y0, x1, y1)
            self.draw(direction, tags, **kw)


class RegularGraph(SimpleGraph):
    def __init__(self, master, shape, color, width=1, fill=None, cnf={}, **kw):
        '''The base class of all graphics frames.
        :param shape: 'circle', 'square'.

        Example:
        =============
        root = Tk()
        self = RegularGraph(root, 'circle', 'yellow', width=1, fill=None, background='pink')
        self.fill = 'red'
        self.draw([140, 140], 40, tags='DF', activedash=7)
        self.add_row([75, 45], 20, 10)
        self.fill = 'blue'
        self.add_column([40, 80], 20, 5)
        self.grid(row=0, column=0)
        root.mainloop()
        '''
        super().__init__(master, shape, color, width, fill, cnf, **kw)

    def draw(self, center, radius, tags=None, **kw):
        if self.shape == 'circle':
            return self.create_circle(center, radius, self.color, self.width, tags, fill=self.fill, **kw)
        elif self.shape == 'square':
            return self.create_square(center, radius, self.color, self.width, tags, fill=self.fill, **kw)

    def add_row(self, center, radius, num, stride=10, tags=None, **kw):
        x0, y0 = center
        for _ in range(num):
            x0 += stride
            self.draw((x0, y0), radius, tags=tags, **kw)

    def add_column(self, center, radius, num, stride=5, tags=None, **kw):
        x0, y0 = center
        for _ in range(num):
            y0 += stride
            self.draw((x0, y0), radius, tags=tags, **kw)


class SelectorMeta(CanvasMeta):
    colors = 'red', 'blue', 'black', 'purple', 'green', 'orange'  # 'skyblue'
    shapes = 'rectangle', 'oval', 'line', 'point'
    color = ParamDict()
    shape = ParamDict()

    def __init__(self, master, shape='rectangle', color='blue', cnf={}, **kw):
        '''A selection icon that sets the shape and color of the graphic.

        Example:
        ======================
        from tkinter import Tk
        from tkinterx.graph.canvas_design import SelectorMeta
        root = Tk()
        select = SelectorMeta(root, background='pink')
        select.grid()
        root.mainloop()
        '''
        super().__init__(master, cnf, **kw)
        self.shape = shape
        self.color = color
        self.x, self.y = 10, 20
        self.radius = 15
        self.custom_color_button = ttk.Button(self, text='Custom',
                                              width=7,
                                              style="BW.TButton",
                                              command=self.custom_color)
        self.create_colors(self.x, self.y)
        self.create_shapes(self.x, self.y+self.radius*3)
        self.dtag('graph')

    def custom_color(self, *args):
        # Pop-up color selection dialog box
        select_color = colorchooser.askcolor(parent=self.master,
                                             title="Please choose a color", color=self.color)
        if select_color:
            self.color = select_color[1]

    def create_colors(self, x, y):
        self.create_text((x, y), text='color', font='Times 15', anchor='w')
        x0 = self.radius + self.x*3
        stride = self.radius*2 + 5
        for color in self.colors:
            x0 += stride
            self.create_circle((x0, y), self.radius,
                               fill=color, color='yellow', tags=color)
        self.create_window((x0+self.radius+5, y),
                           window=self.custom_color_button, anchor='w')

    def create_shapes(self, x, y):
        self.create_text((x, y), text='shape', font='Times 15', anchor='w')
        x += self.radius * 2
        for shape in self.shapes:
            x += self.radius * 2 + 5
            fill = 'white' if shape in ['rectangle', 'oval'] else 'blue'
            width = 2 if shape in ['rectangle', 'oval'] else 10
            if shape != 'point':
                bbox = [x-self.radius, y-self.radius,
                        x+self.radius, y+self.radius]
                self.create_graph(shape, bbox, fill=fill,
                                  tags=shape, width=width)
            else:
                self.create_square_point([x, y], fill, width, tags=shape)


class SelectorFrame(ttk.LabelFrame):
    def __init__(self, master=None, **kw):
        '''Events that bind colors and shapes
        '''
        super().__init__(master, **kw)
        self.selector = SelectorMeta(
            self, background='skyblue', width=350, height=100)
        self.selector.custom_color_button['command'] = self.custom_color
        self.info_var = StringVar(master, name='info')
        self.info_label = ttk.Label(self, textvariable=self.info_var,
                                    relief='sunken')
        self.set_info()
        self.bind_selector()

    @property
    def shape(self):
        return self.selector.shape

    @property
    def color(self):
        return self.selector.color

    def set_info(self):
        text = f"{self.selector.color},{self.selector.shape}"
        self.info_var.set(text)

    def bind_selector(self):
        [self.color_bind(self.selector, color)
         for color in SelectorMeta.colors]
        [self.shape_bind(self.selector, shape)
         for shape in SelectorMeta.shapes]

    def custom_color(self, *args):
        # Pop-up color selection dialog box
        self.selector.custom_color(*args)
        self.set_info()

    def update_color(self, new_color):
        self.selector.color = new_color
        self.set_info()

    def update_shape(self, new_shape):
        '''Update graph_type information.'''
        self.selector.shape = new_shape
        self.set_info()

    def color_bind(self, canvas, color):
        canvas.tag_bind(color, '<1>', lambda e: self.update_color(color))

    def shape_bind(self, canvas, shape):
        canvas.tag_bind(shape, '<1>', lambda e: self.update_shape(shape))

    def layout(self):
        self.selector.grid(row=0, column=0, sticky='we')
        self.info_label.grid(row=1, column=0, sticky='we')