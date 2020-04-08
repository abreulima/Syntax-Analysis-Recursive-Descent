from tokens import Tokens
from anytree import Node, RenderTree

def expr(tokens):
    t = term(tokens)
    tok = tokens.next_token()

    while tok is '+':
        tokens.advance()
        t = Node('+', children=[t, term(tokens)])
        tok = tokens.next_token()

    return t


def term(tokens):
    t = factor(tokens)
    tok = tokens.next_token()

    while tok is '*':
        tokens.advance()
        t = Node('*', children=[t, term(tokens)])

        tok = tokens.next_token()

    return t

def factor(tokens):

    tok = tokens.next_token()

    if tok is 'a':
        tokens.advance()
        return Node(tok)

    elif tok is '(':
        tokens.advance()
        t = expr(tokens)

        if tokens.next_token() is ')':
            tokens.advance()
            return t

        else:
            print("Error 1")

    else:
        print("Error 2")


def main():

    f = open("tests/a.txt")

    for l in f:
        l = l.split('\n')[0]
        l = l + '$'

        token = Tokens(l)
        root = expr(token)

        print(l[:-1])
        for pre, fill, node in RenderTree(root):
            print("%s%s" % (pre, node.name))
        print()


main()






