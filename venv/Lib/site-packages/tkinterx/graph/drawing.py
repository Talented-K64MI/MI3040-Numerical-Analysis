from tkinter import ttk, Toplevel

from .canvas import GraphMeta
from .shape import Rectangle
from ..param import ParamDict
from .generate_label import AskValueWindow


class _GraphCanvas(GraphMeta):
    graph_type = ParamDict()
    color = ParamDict()

    def __init__(self, master=None,  graph_type='rectangle', color='blue',  min_size=7, cnf={}, **kw):
        '''
        '''
        super().__init__(master, cnf, **kw)
        self.min_rect = Rectangle([0, 0, min_size, min_size])
        self.move_bbox = ['none']*4
        self.graph_type, self.color = graph_type, color
        self.bind_tune(master)
        self.bunch = {}  # 记录 canvas 对象
        master.bind('<p>', self.print_bunch)
        master.bind('<1>', self.select_graph)
        self.tag_bind('helper', '<1>', self.start_move_selected)
        self.tag_bind('selected', '<3>', self.ask_selected_value)
        self.tag_bind('center', '<ButtonRelease-1>', self.all_move_selected)
        self.tag_bind('left_top_corner', '<ButtonRelease-1>',
                      lambda e: self.scale_selected(e, [1, 1, 0, 0]))
        self.tag_bind('right_bottom_corner', '<ButtonRelease-1>',
                      lambda e: self.scale_selected(e, [0, 0, 1, 1]))
        self.tag_bind('left_bottom_corner', '<ButtonRelease-1>',
                      lambda e: self.scale_selected(e, [1, 0, 0, 1]))
        self.tag_bind('right_top_corner', '<ButtonRelease-1>',
                      lambda e: self.scale_selected(e, [0, 1, 1, 0]))
        self.tag_bind('top_middle', '<ButtonRelease-1>',
                      lambda e: self.scale_selected(e, [0, 1, 0, 0]))
        self.tag_bind('bottom_middle', '<ButtonRelease-1>',
                      lambda e: self.scale_selected(e, [0, 0, 0, 1]))
        self.tag_bind('left_middle', '<ButtonRelease-1>',
                      lambda e: self.scale_selected(e, [1, 0, 0, 0]))
        self.tag_bind('right_middle', '<ButtonRelease-1>',
                      lambda e: self.scale_selected(e, [0, 0, 1, 0]))

    def ask_selected_value(self, event=None):
        try:
            if self.label_window.state() == 'normal':
                self.label_window.focus()
        except:
            self.label_window = AskValueWindow(self)
        self.label_window.title('标签 工具')
        self.label_window.transient(self)
        self.wait_window(self.label_window)
        print(self.bunch)
        bunch = self.label_window.output
        for graph_id in self.find_withtag('selected'):
            value = self.bunch.get(graph_id)
            if value:
                self.bunch[graph_id].update({'label': bunch})

    @property
    def record_bbox(self):
        _record_bbox = self._record_bbox
        if 'none' in _record_bbox:
            return
        else:
            return Rectangle(_record_bbox)

    def scale_selected(self, event, scale_bbox):
        self.move_bbox[2:] = self._record_bbox[2:]
        move_bbox = self.move_bbox
        if 'none' not in move_bbox:
            selected_ids = self.find_withtag('selected')
            rect = Rectangle(move_bbox)
            if selected_ids and rect:
                for selected_id in selected_ids:
                    bbox = list(self.bbox(selected_id))
                    bbox[0] += rect.grad_x * scale_bbox[0]
                    bbox[1] += rect.grad_y * scale_bbox[1]
                    bbox[2] += rect.grad_x * scale_bbox[2]
                    bbox[3] += rect.grad_y * scale_bbox[3]
                    self.move('helper', rect.grad_x, rect.grad_y)
                    self.coords('selected', bbox)
            self.dtag('selected')
            self.delete('helper')
        self.reset()
        self.update_bunch(event)

    def start_move_selected(self, event):
        self.move_bbox[:2] = self._record_bbox[2:]
        self.unbind_drawing(self.master)

    def all_move_selected(self, event):
        self.move_bbox[2:] = self._record_bbox[2:]
        move_bbox = self.move_bbox
        if 'none' not in move_bbox:
            rect = Rectangle(move_bbox)
            if rect:
                self.move('helper', rect.grad_x, rect.grad_y)
                self.move('selected', rect.grad_x, rect.grad_y)
            self.dtag('selected')
            self.delete('helper')
        self.reset()
        self.update_bunch(event)

    def create_helper(self, rect):
        r = 5
        color = 'khaki'
        self.delete('helper')
        for name, point in rect.bunch.items():
            self.create_circle(point, r, tags=f'helper {name}', fill=color)
        self.create_circle(rect.center, r, tags=f'helper center', fill=color)

    @property
    def selected_current_graph(self):
        tags = self.gettags('current')
        graph_ids = set(self.find_withtag('current'))
        if 'background' in tags:
            bbox = self.bbox('background')
            graph_ids = set(self.find_enclosed(*bbox)) - graph_ids
        return tuple(graph_ids)

    def select_graph(self, event):
        x, y = self._record_bbox[2:]
        graph_id = self.find_closest(x, y) if 'none' not in [x, y] else ()
        tags = self.gettags(graph_id)
        bbox = self.bbox(graph_id) if 'graph' in tags else ''
        #print(tags, bbox)
        if bbox:
            rect = Rectangle(bbox)
            width, height = rect.width, rect.height
            if (x, y) in rect:
                self.create_helper(rect)
                self.addtag_withtag('selected', graph_id)

    def print_bunch(self, *event):
        self.update_bunch(event)
        print(self.bunch)

    def bind_tune(self, master):
        master.bind('<F1>', self.clear_graph)
        master.bind('<Delete>', self.delete_graph)
        master.bind('<Up>', lambda event: self.move_graph(event, 0, -1))
        master.bind('<Down>', lambda event: self.move_graph(event, 0, 1))
        master.bind('<Left>', lambda event: self.move_graph(event, -1, 0))
        master.bind('<Right>', lambda event: self.move_graph(event, 1, 0))
        master.bind('<Control-Up>',
                    lambda event: self.tune_graph(event, [0, -1, 0, 0]))
        master.bind('<Control-Down>',
                    lambda event: self.tune_graph(event, [0, 1, 0, 0]))
        master.bind('<Control-Left>',
                    lambda event: self.tune_graph(event, [-1, 0, 0, 0]))
        master.bind('<Control-Right>',
                    lambda event: self.tune_graph(event, [1, 0, 0, 0]))
        master.bind('<Control-Shift-Up>',
                    lambda event: self.tune_graph(event, [0, 0, 0, -1]))
        master.bind('<Control-Shift-Down>',
                    lambda event: self.tune_graph(event, [0, 0, 0, 1]))
        master.bind('<Control-Shift-Left>',
                    lambda event: self.tune_graph(event, [0, 0, -1, 0]))
        master.bind('<Control-Shift-Right>',
                    lambda event: self.tune_graph(event, [0, 0, 1, 0]))

    def mouse_draw_graph(self, width=1, tags=None, **kw):
        if self.graph_type == 'point':
            return self.create_square_point(self._record_bbox[2:], self.color, width, tags, **kw)
        else:
            return self.create_graph(self.graph_type, self._record_bbox, self.color, width, tags, **kw)

    def drawing(self, width=1, tags=None, **kw):
        if self.record_bbox:
            self.delete('temp')
            if self.graph_type in ['line', 'point'] or not self.record_bbox < self.min_rect:
                return self.mouse_draw_graph(width, tags, activedash=10, **kw)

    def refresh_graph(self, event, **kw):
        if self.graph_type:
            self.after(5, lambda: self.drawing(
                width=2, tags='temp', dash=10, **kw))

    def finish_drawing(self, *event,  **kw):
        if self.graph_type:
            if self.record_bbox:
                self.drawing(width=1, tags=None, **kw)
        self.reset(event)

    def reset(self, *event):
        self._record_bbox[:2] = ['none']*2

    def bind_drawing(self, master):
        master.bind('<B1-Motion>', self.refresh_graph)
        master.bind('<ButtonRelease-1>', self.finish_drawing)

    def unbind_drawing(self, master):
        master.unbind('<B1-Motion>')
        master.unbind('<ButtonRelease-1>')

    def get_graph(self, graph_id):
        return {'bbox': self.bbox(graph_id), 'tags': self.gettags(graph_id)}

    def update_bunch(self, *event):
        graph_ids = self.find_withtag('graph')
        params = {k: self.get_graph(graph_id)
                  for k, graph_id in enumerate(graph_ids)}
        self.bunch = params

    def clear_graph(self, event):
        self.delete('graph')
        self.bunch = {}

    def delete_graph(self, event):
        self.delete(self.selected_current_graph)
        self.update_bunch(event)

    def tune_graph(self, event, strides):
        bbox = self.bbox('current')
        width = 1  # 图形的宽度
        if bbox:
            x0, y0, x1, y1 = bbox
            x0 += strides[0] + width
            y0 += strides[1] + width
            x1 += strides[2] - width
            y1 += strides[3] - width
            self.coords(self.selected_current_graph, *[x0, y0, x1, y1])
            self.update_bunch(event)

    def move_graph(self, event, x, y):
        self.move(self.selected_current_graph, x, y)
        self.update_bunch(event)


class GraphCanvas(_GraphCanvas):
    def __init__(self, master=None,  graph_type='rectangle', color='blue', min_size=10, cnf={}, **kw):
        '''
        '''
        super().__init__(master,  graph_type, color, min_size, cnf, **kw)
        self.scroll_x = ttk.Scrollbar(master, orient='horizontal')
        self.scroll_y = ttk.Scrollbar(master, orient='vertical')
        self.scroll_x['command'] = self.xview
        self.scroll_y['command'] = self.yview
        self.configure(xscrollcommand=self.scroll_x.set,
                       yscrollcommand=self.scroll_y.set)
        self.update_idletasks()
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        region = self.bbox('all')
        self.configure(scrollregion=region)

    def layout(self):
        self.grid(row=0, column=0, sticky='nesw')
        self.scroll_y.grid(row=0, column=1, sticky='ns')
        self.scroll_x.grid(row=1, column=0, sticky='we')
