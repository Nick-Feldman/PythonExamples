'''
Define a class named American and its subclass NewYorker.
'''

class American:
    def __init__(self):
        self.text = "I am an American."

class NewYorker(American):
    def __init__(self):
        super().__init__()
        self.text += "  I live in New York City."


amer = American()
ny = NewYorker()

print(amer.text)

print(ny.text)
