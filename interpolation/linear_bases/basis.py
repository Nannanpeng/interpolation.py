class LinearBasis:

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        return self.eval(*args, **kwargs)

    def eval(self, x, orders=None):
        pass

    def filter(self,x):
        pass
