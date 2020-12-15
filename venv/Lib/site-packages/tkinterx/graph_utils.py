from PIL import Image, ImageTk
from functools import lru_cache

from .image_utils import ImageLoader
from .param import ParamDict

from .graph.drawing import GraphCanvas
from .graph.canvas_design import SelectorFrame
from .tools.helper import StatusTool


class ImageCanvas(GraphCanvas):
    image_root = ParamDict()

    def __init__(self, master=None,  graph_type='rectangle', color='blue',
                 min_size=10, image_root='',
                 is_fullscreen=False, cnf={}, **kw):
        '''
        '''
        super().__init__(master,  graph_type, color, min_size, cnf, **kw)
        self.is_fullscreen = is_fullscreen
        self.image_root = image_root
        self.loader = ImageLoader(self.image_root)
        self.image = None

    def set_photo(self, image=None, size=None, **kw):
        '''设置背景图'''
        # 使用实例变量引用避免 PhotoImage 被销毁
        self.photo = ImageTk.PhotoImage(image, size, **kw)

    @property
    def current_id(self):
        return self.loader.current_id

    def update_current_root(self, image_root):
        self.image_root = image_root
        self.loader.root = self.image_root

    def update_photo(self, image):
        self.delete('background')
        self.set_photo(image=image)
        self.create_image(0, 0, image=self.photo,
                          anchor='nw', tags='background')
        self.lower('background')

    def update_background(self):
        self.update_photo(self.loader.current_image)

    def resize(self, event):
        size = event.width, event.height
        GraphCanvas.resize(self, event)
        if self.image_root:
            self.image = self.loader.current_image
            if self.is_fullscreen:
                self.image = self.image.resize(size)
            self.update_background()

    @property
    def num_loader(self):
        return len(self.loader)

    def prev_image(self, *event):
        if self.num_loader:
            self.loader.current_id -= 1
            self.update_background()

    def next_image(self, *event):
        if self.num_loader:
            self.loader.current_id += 1
            self.update_background()


class GraphFrame(SelectorFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.canvas = ImageCanvas(master, bg='pink', graph_type=None, highlightthickness=0)
        
    def update_color(self, new_color):
        self.selector.color = new_color
        self.set_info()
        self.canvas.color = new_color

    def update_shape(self, new_shape):
        '''Update graph_type information.'''
        self.selector.shape = new_shape
        self.set_info()
        self.canvas.graph_type = new_shape
        self.canvas.bind_drawing(self.master)

    def layout(self):
        self.canvas.layout()
        self.grid(row=3, column=0, sticky='nw')
        self.selector.grid(row=0, column=0, sticky='we')
        self.info_label.grid(row=1, column=0, sticky='we')
