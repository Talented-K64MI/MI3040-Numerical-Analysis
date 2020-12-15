#from functools import lru_cache

class Rectangle:
    def __init__(self, bbox):
        self.x0, self.y0, self.x1, self.y1 = bbox
        self.bunch = {
            'left_top_corner': (self.x0, self.y0),
            'top_middle': (self.center[0], self.y0),
            'right_top_corner': (self.x1, self.y0),
            'right_middle': (self.x1, self.center[1]),
            'right_bottom_corner': (self.x1, self.y1),
            'bottom_middle': (self.center[0], self.y1),
            'left_bottom_corner': (self.x0, self.y1),
            'left_middle': (self.x0, self.center[1])
        }

    @property
    def grad_x(self):
        return self.x1 - self.x0

    @property
    def grad_y(self):
        return self.y1 - self.y0

    @property
    def width(self):
        return abs(self.grad_x)

    @property
    def height(self):
        return abs(self.grad_y)

    @property
    def center(self):
        x = (self.x0 + self.x1)/2
        y = (self.y0 + self.y1)/2
        return x, y

    def __contains__(self, point):
        x, y = point
        x_cond = x in range(self.x0, self.x1)
        y_cond = y in range(self.y0, self.y1)
        return x_cond and y_cond

    def __lt__(self, other):
        '''self < other'''
        return self.width < other.width or self.height < other.height

    def __le__(self, other):
        '''self < other'''
        return self.width <= other.width or self.height <= other.height
