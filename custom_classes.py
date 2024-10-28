## Description: You are tasked with creating a Rectangle class

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

a = Rectangle(2, 4)

for item in a:
    print(item)
