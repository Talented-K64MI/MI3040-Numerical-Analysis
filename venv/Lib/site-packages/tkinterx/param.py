class ParamDict(dict):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def __set__(self, instance, value):
        #print('===> set', instance, value)
        self[instance] = value

    def __get__(self, instance, owner):
        return self[instance]
