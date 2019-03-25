from Model import Model


class Receiver:
    gotFramesCounter = 0                                                                   # licznik ile ramek zostalo odebranych
    model = Model()                                                                        # pusty model

    def getFrame(self, gotFrame, counter):                                                 # do frame ramka ktora przychodzi: dekoder
        self.model.frames.append([])
        ++counter
        for i in range(len(gotFrame) - 1):
            self.model.frames[counter].append(gotFrame[i])                                 # odbieramy ramke
        pb = self.model.frames[counter].parityBit()                                        # wyznaczamy bit parzystosci
        #if pb !=
