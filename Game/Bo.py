class Bo:
    def __init__(self, name=None):
        if name is None:
            print("Default")
        else:
            self.name = name
            print(name)