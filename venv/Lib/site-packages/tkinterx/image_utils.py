from pathlib import Path
from PIL import Image

from .param import ParamDict


class ImageDict(dict):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def __set__(self, instance, value):
        #print('===> set', instance, value)
        self[instance] = value

    def __get__(self, instance, owner):
        m = len(instance)
        if -m <= self[instance] < m:
            return self[instance]
        elif self[instance] < -m:
            return 0
        else:
            return -m


class ImageLoader:
    root = ParamDict()
    current_id = ImageDict()

    def __init__(self, root, current_id=0):
        self.root = Path(root)
        self.current_id = current_id
        #self.name_dict = {name: k for k, name in enumerate(self.names)}

    def get_names(self, re_pattern):
        return set([name.parts[-1] for name in self.root.glob(re_pattern)])

    @property
    def names(self):
        png_names = self.get_names('*.png')
        jpg_names = self.get_names('*.jpg')
        bmp_names = self.get_names('*.bmp')
        names = png_names | jpg_names | bmp_names
        return sorted(names)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [self.root/name for name in self.names[index]]
        else:
            return self.root/self.names[index]

    @property
    def current_name(self):
        return self.names[self.current_id]

    @property
    def current_path(self):
        return self.root / self.current_name

    def __len__(self):
        return len(self.names)

    def path2image(self, path):
        return Image.open(path)

    @property
    def current_image(self):
        return self.path2image(self.current_path)

