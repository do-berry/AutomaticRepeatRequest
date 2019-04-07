from model import Model


def run():
    model = Model()
    model.fillMessage()                                                                                                 # tworzenie msg
    model.createFrames()                                                                                                # dzielenie msg na ramki + bit parzystosci
    model.fillBadFrames()
    model.printFrames(model.sentFrames)
    model.stopAndWait()
    # model.selectiveRepeat()

if __name__ == '__main__':
    run()