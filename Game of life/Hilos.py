from threading import Thread

class testit(Thread):
    def __init__(self, args):
        Thread.__init__(self)
        self.args = args

    # def run(self):
    #     main(self.args)