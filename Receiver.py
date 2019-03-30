from Model import Model


class SAWReceiver:
    gotFramesCounter = -1                                                                   # licznik ile ramek zostalo odebranych
    model = Model()                                                                        # pusty model
    isCorrect = True

    def getFrame(self, gotFrame, counter):                                                 # do frame ramka ktora przychodzi: dekoder
        self.revert()
        self.model.frames.append([])
        ++self.gotFramesCounter
        for i in range(len(gotFrame) - 1):
            self.model.frames[counter].append(gotFrame[i])                                 # odbieramy ramke
        pb = self.model.frames[counter].parityBit()                                        # wyznaczamy bit parzystosci
        if pb != gotFrame[len(gotFrame)]:
            self.isCorrect = False                                                         # bp jest niepoprawny
            --self.gotFramesCounter                                                                      # zmniejszenie licznika - zeby sie powtorzylo dla tej samej ramki

    def revert(self):
        if self.isCorrect == False:
            self.isCorrect = True

class SAWSender:
    sentFramesCounter = -1
    model = Model()

    def getModel(self):                                                                    # tworzenie modelu bez zaklocen
        self.model.fillMessage()
        self.model.createFrames()
        for i in range(len(self.model.frameSize[0])):
            self.model.parityBit(self.model.frames[i])

class Canal:
    sender = SAWSender()
    receiver = SAWReceiver()

    def send(self):
        self.sender.model.generateErrors()                                                  # generowanie errorow
        for i in range(self.sender.model.frameSize[0]):                                     # kazda ramke u sendera
            self.receiver.getFrame(self.sender.model.frames[i], self.receiver.gotFramesCounter)     # odebrac u receivera i robic cos tam z licznikiem
            if self.receiver.isCorrect != True:
                self.sender.model.generateErrors()