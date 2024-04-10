class MyList(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callbacks = []

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def __setitem__(self, key, value):
        super(MyList, self).__setitem__(key, value)
        for callback in self.callbacks:
            callback(key, value, 'set')

    def __delitem__(self, key):
        super(MyList, self).__delitem__(key)
        for callback in self.callbacks:
            callback(key, 'delete')
