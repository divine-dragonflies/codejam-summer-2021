import blessed

term = blessed.Terminal()

def left_of():
    print("Left was passed")

def right_of():
    print("Right was passed")

def above():
    print("Above was passed")

def below():
    print("Below was passed")


def key_mapping(key):
    functions = {
        'a': left_of,
        'd': right_of,
        'w': above,
        's': below,
    }
    func = functions[key]
    func()

def main_loop():
    with term.cbreak():
        val = term.inkey()
        #It will be working until ESCAPE pressed
        while val.code != term.KEY_ESCAPE: 
            val = term.inkey()
            if val and str(val) in 'wasd':
                key_mapping(str(val))
            else:
                pass


main_loop()