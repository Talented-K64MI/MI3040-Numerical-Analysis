from tkinter import Tk, ttk, filedialog, StringVar
from pathlib import Path
from PIL import ImageTk
from pathlib import Path
from functools import lru_cache

from .tools.helper import StatusTool
from .graph_utils import GraphFrame
from .meta import ask_window, askokcancel, showwarning
from .meta import Table, PopupLabel
from .utils import FileNotebook, mkdir, save_bunch, load_bunch
from .image_utils import ImageLoader


class GraphLoader(GraphFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.bunch = {}
        self.default_path = 'data/annotations.json'
        self.notebook = FileNotebook(self, width=200, height=90, padding=2)
        self.create_image_loader()
        master.bind('<Control-s>', self.save_graph)
        master.bind('<Control-l>', self.load_graph)

    def layout(self):
        GraphFrame.layout(self)
        self.notebook.grid(row=0, column=1, sticky='nw', padx=5)

    def create_image_loader(self):
        self.image_frame = ttk.Frame(self.notebook)
        self.load_image_button = ttk.Button(
            self.image_frame, text='New', width=5, command=self.new_create)
        self.table = Table(self.image_frame)
        self.table.add_row('image_id', 'image_id:', width=7)
        self.prev_image_button = ttk.Button(
            self.image_frame, text='Prev', width=5, command=self.prev_image)
        self.next_image_button = ttk.Button(
            self.image_frame, text='Next', width=5, command=self.next_image)
        self.notebook.add(self.image_frame, text='Image')
        self.table['image_id'].entry['validate'] = "focusout"
        self.table['image_id'].entry['validatecommand'] = self.change_image
        self.table.layout(row=0, sticky='w')
        self.load_image_button.grid(row=3, column=0, sticky='w')
        self.prev_image_button.grid(row=3, column=1, sticky='w')
        self.next_image_button.grid(row=3, column=2, sticky='w')

    def load_bunch(self):
        path = Path(self.default_path)
        if path.exists():
            bunch = load_bunch(path)
        else:
            bunch = {}
        return bunch

    def new_create(self, *event):
        DIR = Path(filedialog.askdirectory())
        self.canvas.update_current_root(DIR)
        if self.canvas.num_loader:
            self.canvas.update_background()
            self.table['image_id'].var.set(0)

    def cat2params(self, cats):
        params = []
        for cats in cats.values():
            tags = cats['tags']
            _, color, shape, *_ = tags
            graph_type = shape.split('_')[0]
            bbox = cats['bbox']
            params.append({'tags': tags, 'color': color,
                           'graph_type': graph_type, 'direction': bbox})
        return params

    def load_graph(self, *args):
        self.bunch = self.load_bunch()
        if self.bunch.get('root'):
            self.canvas.update_current_root(Path(self.bunch['root']))
            num = len(self.canvas.loader)
            if num:
                self.canvas.update_background()
                self.table['image_id'].var.set(0)
                self.draw_current_graph()
        else:
            cats = self.bunch.get('default')
            if cats:
                self._draw_graph(cats)

    def save_graph(self, *event):
        mkdir('data')
        self.bunch = self.load_bunch()
        self.canvas.update_bunch(event)
        bunch = self.canvas.bunch
        if self.canvas.num_loader:
            current_name = self.canvas.loader.current_name
            root = self.canvas.loader.root.as_posix()
            cats = {current_name: bunch}
            self.bunch.update({"root": root, **cats})
        else:
            self.bunch.update({'default': bunch})
        save_bunch(self.bunch, self.default_path)

    def _draw_graph(self, cats):
        params = self.cat2params(cats)
        for param in params:
            self.canvas.create_graph(activedash=10, **param)

    def draw_graph(self, name):
        cats = self.bunch.get(name)
        if cats:
            params = self.cat2params(cats)
            for param in params:
                self.canvas.create_graph(activedash=10, **param)

    def draw_current_graph(self):
        name = self.canvas.loader.current_name
        self.draw_graph(name)

    def change_image(self, *event):
        self.save_graph(event)
        self.canvas.clear_graph(event)
        current_image_id = self.table['image_id'].var.get()
        num = self.canvas.num_loader
        if num:
            if current_image_id in [str(k) for k in range(-num, num)]:
                self.canvas.loader.current_id = int(current_image_id)
            self.canvas.update_background()
            self.draw_current_graph()
            return True
        else:
            return False

    def prev_image(self, *event):
        self.save_graph(event)
        self.canvas.clear_graph(event)
        self.bunch = self.load_bunch()
        if self.canvas.num_loader:
            self.canvas.prev_image(event)
            self.table['image_id'].var.set(self.canvas.current_id)
            self.draw_current_graph()

    def next_image(self, *event):
        self.save_graph(event)
        self.canvas.clear_graph(event)
        self.bunch = self.load_bunch()
        if self.canvas.num_loader:
            self.canvas.next_image(event)
            self.table['image_id'].var.set(self.canvas.current_id)
            self.draw_current_graph()


class GraphWindow(Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.graph = GraphLoader(self)
        self.graph.canvas.bind_drawing(self)
        self.graph.layout()
