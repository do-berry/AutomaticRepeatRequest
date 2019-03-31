from model import Model

def run():
    model = Model()
    model.fillMessage()                                                                                                 # tworzenie msg
    model.createFrames()                                                                                                # dzielenie msg na ramki + bit parzystosci
    model.printFrames(model.frames)
    model.generateErrors()                                                                                              # przeslanie ramek
    model.printFrames(model.framesWithErrors)

if __name__ == '__main__':
    run()