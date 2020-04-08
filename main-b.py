from tokens import Tokens
from anytree import Node, RenderTree

def I(tokens):

    tok = tokens.next_token()

    if tok is 'a':
        tokens.advance()
        t = Node('a', children=[A(tokens)])
        return t


def A(tokens):

    tok = tokens.next_token()
    t = Node(tok)


    while tok is 'a' or tok is 'n':
        tokens.advance()

        if tokens.next_token():
            t = Node(tok, children = [A(tokens)])
        else:
            t = Node(tok)

        tok = tokens.next_token()

    return t

def main():

    f = open("tests/b.txt")

    for l in f:
        l = l.split('\n')[0]
        l = l + '$'

        token = Tokens(l)
        root = A(token)

        print(l[:-1])
        for pre, fill, node in RenderTree(root):
            print("%s%s" % (pre, node.name))
        print()

main()






