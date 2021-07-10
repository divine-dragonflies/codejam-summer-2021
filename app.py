from blessed import Terminal


if __name__ == '__main__':
    term = Terminal()

    print(term.home + term.clear + term.move_y(term.height // 2))
    print(term.black_on_darkkhaki(term.center('Hello World')))
