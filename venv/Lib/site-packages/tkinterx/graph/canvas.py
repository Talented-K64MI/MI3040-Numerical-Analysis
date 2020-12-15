from tkinter import Canvas, StringVar


class CanvasMeta(Canvas):
    '''Graphic elements are composed of line(segment), rectangle, ellipse, and arc.
    '''

    def __init__(self, master=None, cnf={}, **kw):
        '''The base class of all graphics frames.

        :param master: a widget of tkinter or tkinter.ttk.
        '''
        super().__init__(master, cnf, **kw)

    def create_graph(self, graph_type, direction, color='blue', width=1, tags=None, **kwargs):
        '''Draw basic graphic elements.

        :param direction: Specifies the orientation of the graphic element. 
            Union[int, float] -> (x_0,y_0,x_,y_1), (x_0, y_0) refers to the starting point of 
            the reference brush (i.e., the left mouse button is pressed), and (x_1, y_1) refers to 
            the end position of the reference brush (i.e., release the left mouse button).
            Multipoint sequences are supported for 'line' and 'polygon',
             for example ((x_0, y_0), (x_1, y_1), (x_2, y_2)).
        :param graph_type: Types of graphic elements.
            (str) 'rectangle', 'oval', 'line', 'arc'(That is, segment), 'polygon'.
            Note that 'line' can no longer pass in the parameter 'fill', and 
            the remaining graph_type cannot pass in the parameter 'outline'.
        :param color: The color of the graphic element.
        :param width: The width of the graphic element.(That is, center fill)
        :param tags: The tags of the graphic element. 
            It cannot be a pure number (such as 1 or '1' or '1 2 3'), it can be a list, a tuple, 
            or a string separated by a space(is converted to String tupers separated by a blank space). 
            The collection or dictionary is converted to a string.
            Example:
                ['line', 'graph'], ('test', 'g'), 'line',
                ' line kind '(The blanks at both ends are automatically removed), and so on.
        :param style: Style of the arc in {'arc', 'chord', or 'pieslice'}.

        :return: Unique identifier solely for graphic elements.
        '''
        if tags is None:
            if graph_type in ('rectangle', 'oval', 'line', 'arc'):
                tags = f"graph {color} {graph_type}"
            else:
                tags = f'graph {color}'

        com_kw = {'width': width, 'tags': tags}
        kw = {**com_kw, 'outline': color}
        line_kw = {**com_kw, 'fill': color}
        if graph_type == 'line':
            kwargs.update(line_kw)
        else:
            kwargs.update(kw)
        func = eval(f"self.create_{graph_type}")
        graph_id = func(*direction, **kwargs)
        return graph_id

    def _create_regular_graph(self, graph_type, center, radius, color='blue', width=1, tags=None, **kw):
        '''Used to create a circle or square.
        :param graph_type: 'oval', 'rectangle'
        :param center: (x, y) The center of the regular_graph
        :param radius: Radius of the regular_graph
        '''
        x, y = center
        direction = [x-radius, y - radius, x+radius, y+radius]
        return self.create_graph(graph_type, direction, color, width, tags, **kw)

    def create_circle(self, center, radius, color='blue', width=1, tags=None, **kw):
        '''
        :param center: (x, y) The center of the circle
        :param radius: Radius of the circle
        '''
        return self._create_regular_graph('oval', center, radius, color, width, tags, **kw)

    def create_square(self, center, radius, color='blue', width=1, tags=None, **kw):
        '''
        :param center: (x, y) The center of the square
        :param radius: Radius of the square
        '''
        return self._create_regular_graph('rectangle', center, radius, color, width, tags, **kw)

    def create_circle_point(self, position, color='blue', width=1, tags=None, **kw):
        '''
        :param location: (x, y) The location of the circle_point
        '''
        return self.create_circle(position, 0, color, width, tags, **kw)

    def create_square_point(self, position, color='blue', width=1, tags=None, **kw):
        '''
        :param location: (x, y) The location of the square_point
        '''
        return self.create_square(position, 0, color, width, tags, **kw)


class GraphMeta(CanvasMeta):
    def __init__(self, master=None, cnf={}, **kw):
        '''
        '''
        super().__init__(master, cnf, **kw)
        '''
        属性
        =====
        record_bbox: [x0, y0, x1, y1]，其中 (x0, y0) 为鼠标单击左键时的 canvas 坐标，当释放鼠标时恢复为 ['none']*2
            (x1, y1) 为鼠标在画布移动时的 canavas 坐标
        '''
        super().__init__(master, **kw)
        self._record_bbox = ['none']*4
        self.bind('<Motion>', self.update_xy)
        self.bind('<1>', self.start_record)

    def start_record(self, event):
        '''开始记录点击鼠标时的 canvas 坐标'''
        self._record_bbox[:2] = self.get_canvasxy(event)

    def get_canvasxy(self, event):
        '''返回事件的 canvas 坐标'''
        return self.canvasx(event.x), self.canvasy(event.y)

    def update_xy(self, event):
        '''记录鼠标移动的 canvas 坐标'''
        self._record_bbox[2:] = self.get_canvasxy(event)
