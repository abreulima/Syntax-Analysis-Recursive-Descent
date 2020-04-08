class Tokens:

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.list = []

    def next_token(self):
        if self.text[self.pos] == '$':
            return False
        else:
            return self.text[self.pos]

    def advance(self):
        self.pos = self.pos + 1

