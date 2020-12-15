# -{cd ../tests | python test.py}
from .data import *

# default
MEASURE = FONT = None
LINESPACE = OVERRIDE_LINESPACE = 0

def calculate_linespace(font):
    linespace = font.metrics('linespace')
    mwidth = font.measure('M')
    to_set = mwidth*1.52
    if to_set > linespace:
        return [linespace, linespace]
    return [linespace, to_set]

def select_font(font):
    '''use this before doing anything using this module'''
    global MEASURE, FONT, LINESPACE, OVERRIDE_LINESPACE
    MEASURE = font.measure
    font_props = font.actual()
    FONT = (font_props['family'], font_props['size'])
    LINESPACE, OVERRIDE_LINESPACE = calculate_linespace(font)

class Primitive:
    '''text and line'''
    def __init__(self, content, kind='t', **kwargs):
        self.content = content
        self.kind = kind
        self.relsize = 1
        self.x = kwargs['x'] if 'x' in kwargs else 0
        self.y = kwargs['y'] if 'y' in kwargs else 0
        if self.kind == 't':
            self.slant = kwargs['slant'] if 'slant' in kwargs else 'roman'
            self.width, self.height = MEASURE(self.content), OVERRIDE_LINESPACE
        else:  # line
            self.linewidth = OVERRIDE_LINESPACE * 0.03
            if 'linewidth' in kwargs:
                self.linewidth *= kwargs['linewidth']  # must be relative
            if 'width' in kwargs or 'height' in kwargs:
                self.width, self.height = kwargs['width'], kwargs['height']
            else:
                xes, ys = [], []
                for i in range(int(len(self.content)/2)):  # take two at a time
                    i_x = i*2
                    xes.append(self.content[i_x])
                    ys.append(self.content[i_x + 1])
                self.width, self.height = max(xes) - min(xes), max(ys) - min(ys)
                if not self.height: self.height = self.linewidth * 3
            self.smooth = kwargs['smooth'] if 'smooth' in kwargs else False
        self.midline = kwargs['midline'] if 'midline' in kwargs else 0.5
        if 'relsize' in kwargs:
            self.pull_size(kwargs['relsize'])

    def pull_size(self, to):
        relsize = self.relsize
        self.relsize = (self.relsize + to) / 2
        factor = self.relsize / relsize
        self.width *= factor
        self.height *= factor
        self.x *= factor
        self.y *= factor

    def set_size(self, width=None, height=None):
        if height is not None:
            factor = height / self.height
        elif width is not None:
            factor = width / self.width
        else:
            raise ValueError('One of the two params has to be given.')
        self.relsize *= factor
        self.width *= factor
        self.height *= factor
        self.x *= factor
        self.y *= factor

    def render(self, canvas):
        if self.kind == 't':
            y = self.y - (LINESPACE - OVERRIDE_LINESPACE) * self.relsize / 2  # in the middle
            font = (FONT[0], round(FONT[1] * self.relsize), self.slant)
            canvas.create_text((self.x, y), text=self.content, font=font, anchor='nw')
        elif self.kind == 'l':
            points = []
            for i in range(int(len(self.content)/2)):  # take two at a time
                i_x = i * 2
                points.append(self.content[i_x] * self.relsize + self.x)
                points.append(self.content[i_x + 1] * self.relsize + self.y)
            # three times with different colors & thickness to approximate anti-aliasing
            canvas.create_line(points, width=self.linewidth + .9, smooth=self.smooth, joinstyle='miter', fill='#999')
            canvas.create_line(points, width=self.linewidth - .3, smooth=self.smooth, joinstyle='miter', fill='#444')
            canvas.create_line(points, width=self.linewidth - .5, smooth=self.smooth, joinstyle='miter')
            # canvas.create_line(points, width=self.linewidth, smooth=self.smooth, joinstyle='miter')

    def split(self, string):
        if self.kind != 't':
            return
        return [Primitive(part, 't', slant=self.font_props['slant']) for part in self.content.split(string)]

    def __add__(self, other):
        if type(other) not in [Primitive, Entity]:
            raise TypeError(type(other))
        if isinstance(other, Entity):
            if other.arrangement == 'horiz':
                return Entity([self, *other.content])
        return Entity([self, other])

    def join(self, others):
        to_join = []
        for other in others:
            to_join += [other, Primitive(self.content, self.kind)]
        return Entity(to_join[:-1])

    def __repr__(self):
        content = self.content if type(self.content) == str else "line"
        return f'Primitive({content})'


class Entity:
    '''combination of text, line, (primitives) or other entities'''
    def __init__(self, content, arrange='horiz'):
        self.x = self.y = self.width = self.height = 0
        self.content = content
        self.arrangement = arrange
        self.midline = 0.5
        self.relsize = 1
        self.arrange()

    def arrange(self):
        if self.arrangement == 'horiz':
            # calculate the height
            top, bot = [], []
            for part in self.content:
                top.append(part.height * part.midline)
                bot.append(part.height - top[-1])
            h_top = max(top) if top else 0
            self.height = h_top + (max(bot) if bot else 0)
            self.midline = h_top / self.height
            # determine coords
            x = 0
            for part in self.content:
                part.x, part.y = x, h_top - part.midline*part.height
                x += part.width
            self.width = x
        elif self.arrangement == 'vert':
            y = 0
            self.width = max([part.width for part in self.content])
            for part in self.content:
                part.x, part.y = (self.width - part.width) / 2, y
                y += part.height
            self.height = y
        elif callable(self.arrangement):
            self.arrangement(self)
        else:
            raise TypeError('Arrangement should be "horiz", "vert", or a callable')

    def pull_size(self, to):
        for part in self.content:
            part.pull_size(to)
        self.arrange()  # to adjust the positionings and avoid overlapping

    def render(self, canvas):
        for part in self.content:
            part.x, part.y = part.x + self.x, part.y + self.y
            part.render(canvas)

    def __add__(self, other):
        if type(other) not in [Primitive, Entity]:
            raise TypeError()
        if self.arrangement == 'horiz':
            if isinstance(other, Entity) and other.arrangement == 'horiz':
                return Entity([*self.content, *other.content])
            return Entity([*self.content, other])
        return Entity([self, other])

    def __repr__(self):
        return f'Entity({", ".join([str(c) for c in self.content])})'

class syntax:

    # some symbols
    minus = '−'
    times = '×'
    div = '÷'
    cdot = '⋅'
    halfsp = '\u2006'
    neg = '¬'
    gt = '>'
    lt = '<'
    gte = '≥'
    lte = '≤'
    cdots = '⋯'
    vdots = '⋮'
    ddots = '⋱'

    greek_letters = GREEK_LETTERS
    math_accents = MATH_ACCENTS
    primes = PRIMES

    # things that are transformed, used for units and such
    @property
    def transformed(self):
        return {
            'degC': self.sup(self.txt(' '), self.txt('∘')) + self.txt('C'),
            'degF': self.sup(self.txt(' '), self.txt('∘')) + self.txt('F'),
            'deg': self.sup(self.txt(' '), self.txt('∘')),
            'integral': self.txt('\u222B')
        }

    def txt(self, text):
        if text in [self.times, self.div, self.cdot, '+', self.minus, '=']:
            text = f' {text} '
        if text.isalpha():
            slant = 'italic'
        else:
            slant = 'roman'
        return Primitive(text, 't', slant=slant)

    def txt_rom(self, text):
        return Primitive(text, 't', slant='roman')

    def txt_math(self, text):
        return self.txt_rom(text)

    def arrange_sup(self, sup):
        base, s = sup.content
        s.x = base.width + OVERRIDE_LINESPACE / 5  # s.y = 0
        base_top = base.midline * base.height
        if base_top > s.height:
            base.y = 0.5 * s.height
        else:
            base.y = s.height - 0.5*base.height  # base.x = 0
        sup.width = s.x + s.width
        sup.height = base.y + base.height
        sup.midline = (base.y + base_top) / sup.height

    def sup(self, base, s):
        s.pull_size(.5)
        return Entity([base, s], self.arrange_sup)

    def arrange_sub(self, sub):
        base, s = sub.content
        s.x = base.width
        s.y = 0.5 * base.height
        sub.width = s.x + s.width
        sub.height = s.y + s.height
        sub.midline = base.height*base.midline / sub.height

    def sub(self, base, s):
        s.pull_size(.5)
        return Entity([base, s], self.arrange_sub)

    def arrange_rad(self, rad):
        char, line, base = rad.content
        char.set_size(height=base.height)  # make it equal to the base
        line.set_size(width=base.width + OVERRIDE_LINESPACE / 5)
        line.x = base.x = char.width
        base.y = line.height
        rad.width = char.width + base.width
        rad.height = line.height + base.height

    def rad(self, base):
        line = Primitive([0, 0, base.width + OVERRIDE_LINESPACE/4, 0], 'l')
        if base.height < OVERRIDE_LINESPACE*1.4:
            char = Primitive('√')
        else:
            width, height = OVERRIDE_LINESPACE * 0.7, base.height + line.height
            char = Primitive([
                0,
                height/2,
                0.1 * width,
                height*0.45,
                width/2,
                height,
                width,
                0], 'l', linewidth=1.2)
        return Entity([char, line, base], self.arrange_rad)

    def summation(self, base, end):
        start = Entity([self.txt('i'), self.txt('='), self.txt('1')])
        start.pull_size(.5)
        mark = Primitive('∑', relsize=2)
        end = Primitive(str(end), relsize=0.7)
        notation = Entity([end, mark, start], 'vert')
        return Entity([notation, base])

    def func_name(self, name):
        return self.txt_rom(name + ' ')

    def arrange_frac(self, frac):
        num, line, den = frac.content
        line_add = OVERRIDE_LINESPACE / 3
        if num.width > den.width:
            line.set_size(width=num.width + line_add)
        else:
            line.set_size(width=den.width + line_add)
        num.x = (line.width - num.width) / 2
        den.x = (line.width - den.width) / 2
        line.y = num.height
        den.y = num.height + OVERRIDE_LINESPACE / 10
        frac.height = num.height + line.height + den.height
        frac.width = line.width
        frac.midline = (num.height + line.height / 2) / frac.height

    def frac(self, num, den):
        wmax = max([num.width, den.width])
        line = Primitive([0, 0, wmax + OVERRIDE_LINESPACE/3, 0], 'l')
        part = Entity([num, line, den], self.arrange_frac)
        part.midline = num.height / (num.height + den.height)
        return part

    def math_disp(self, math):
        return math

    def math_inln(self, math):
        return math

    def greek(self, name):
        return self.txt(GREEK_LETTERS[name])

    def arrange_accent(self, accent):
        acc, base = accent.content
        acc.x = (base.width*1.5 - acc.width) / 2
        base.y = 0.2*acc.height
        accent.width, accent.height = base.width, base.y + base.height
        accent.midline = (base.y + base.height/2) / accent.height

    def accent(self, acc, base):
        acc = Primitive(MATH_ACCENTS[acc])
        return Entity([acc, base], self.arrange_accent)

    def prime(self, base, prime):
        return self.sup(base, self.txt(PRIMES[prime]))

    def delmtd(self, contained, kind=0):
        if contained.height < OVERRIDE_LINESPACE*1.4:
            brackets = BRACKETS[kind]
            surround = [Primitive(brackets[0]), Primitive(brackets[1])]
            return Entity([surround[0], contained, surround[1]])

        width, height = OVERRIDE_LINESPACE*2/3, contained.height
        smooth = True
        w = width/2  # width of the horizontal tip
        points = [[width, 0, w, 0, w, height, width, height], [0, 0, w, 0, w, height, 0, height]]
        if kind == 1:  # []
            smooth = False
        elif kind == 2:  # {}
            w, mid_point = width*2/5, height/2  # width and height of the chamfers
            x_mid, x_offset = width - w, width - 2*w
            points = [[width, 0, x_mid, 0, x_mid, mid_point, width-2*w, mid_point, x_mid, mid_point, x_mid, height, width, height],
                      [0, 0, w, 0, w, mid_point, w*2, mid_point, w, mid_point, w, height, 0, height]]
        elif kind == 3:  # ⌊⌋
            smooth = False
            points[0], points[1] = points[0][2:], points[1][2:]
        left = Primitive(points[0], 'l', smooth=smooth, linewidth=2, x=width,
                         y=height*25, width=width, height=height*1.05,
                         midline=contained.midline)
        right = Primitive(points[1], 'l', smooth=smooth, linewidth=2,
                          width=width, y=height*0.025, height=height*1.05,
                          midline=contained.midline)
        return Entity([left, contained, right])

    def _arrange_matrix(self, matrix, cols):
        # get the max params
        widths = [[] for _ in range(cols)]
        heights, row_heights = [], []
        row = col = 0
        i_cols = cols - 1  # max col index
        for element in matrix.content:
            element.row, element.col = row, col  # for arrangement
            widths[col].append(element.width)
            row_heights.append(element.height)
            if col == i_cols:
                heights.append(max(row_heights))
                row_heights = []
                row += 1
                col = 0
            else:
                col += 1
        widths = [max(w) for w in widths]
        x = y = 0
        colgap = OVERRIDE_LINESPACE*0.5
        for element in matrix.content:
            element.x = x + (widths[element.col] - element.width) / 2
            element.y = y + (heights[element.row] - element.height) / 2
            if element.col == i_cols:
                x = 0
                y += heights[element.row]
            else:
                x += widths[element.col] + colgap
        matrix.width = sum(widths) + colgap*(len(widths) - 1)
        matrix.height = sum(heights)

    def matrix(self, elmts, full=False):
        if not full:  # just a row
            return elmts

        # top level, full matrix
        if type(elmts[0]) != list:
            return self.delmtd(Entity(elmts, 'vert'), 1)

        # flatten
        elements = []
        for row in elmts:
            for element in row:
                elements.append(element)
        arrange = lambda matrix: self._arrange_matrix(matrix, len(elmts[0]))

        return self.delmtd(Entity(elements, arrange), 1)

    def arrange_eqarray(self, eqarray):
        # get max dims: widths1 = widths2, heights
        widths, h_top, h_bot = ([], [], []), [], []
        # to get the height above/below the midline
        h = lambda x, top=True: x.height*(x.midline if top else 1-x.midline)
        row, h_rtop, h_rbot = 0, [], []
        for part in eqarray.content:
            part.row = row
            if part.col != 1:
                h_rtop.append(h(part))
                h_rbot.append(h(part, False))
            widths[part.col].append(part.width)
            if part.col == 2:
                h_top.append(max(h_rtop))
                h_bot.append(max(h_rbot))
                h_rtop, h_rbot = [], []
                row += 1
        widths = (max(widths[0]), widths[1][0], max(widths[2]))
        heights = tuple((top + bot for top, bot in zip(h_top, h_bot)))
        row = y = 0
        for part in eqarray.content:
            if part.row > row:
                row = part.row
                y += heights[part.row - 1]
            if part.col == 0:
                part.x = widths[0] - part.width
            elif part.col == 1:
                part.x = widths[0]
            else:
                part.x = widths[0] + widths[1]
            part.y = y + h_top[part.row] - part.height * part.midline
        eqarray.width = sum(widths)
        eqarray.height = y + heights[-1]
      
    def eqarray(self, eqns: list):
        parts = []
        for line in eqns:
            for i, part in enumerate(line):
                col = i * 2
                if i:  # put an equal sign in the middle
                    equals = Primitive(' = ')
                    equals.col = col - 1
                    parts.append(equals)
                part.col = col
                parts.append(part)

        return Entity(parts, self.arrange_eqarray)
