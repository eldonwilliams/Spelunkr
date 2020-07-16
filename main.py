import Input

def main():
    keys = Input.Input()
    Input.Input.genAliveThread()
    @keys.hookKeyEventDecorator('e')
    def func(pressed):
        print('E {}'.format(pressed))
    
    keys.start()

main()