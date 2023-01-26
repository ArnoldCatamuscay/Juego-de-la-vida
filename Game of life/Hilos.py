from threading import Thread

class Hilo(Thread):
    def __init__(self, args):
        Thread.__init__(self)
        self.args = args

    # def run(self):
    #     main(self.args)

