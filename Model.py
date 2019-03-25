import random

class Model:
    message = []                                                                # ciag ktory bedziemy przesylac
    bits = 20                                                                   # ile bitow w wiadomosci
    frameSize = [2,10]                                                          # lista MxN: ilosc ramek x ilosc bitow [bez uwzglednienia bitu parzystosci!!!]
    frames = []                                                                 # lista list == lista z ramkami

    def __init__(self):
        for i in range(self.bits):
            self.message.append(random.randint(0,1))                            # uzupelnia message 0 lub 1

    def generateErrors(self):
        prob = 75                                                               # parametr: od tej wartosci wylosowana liczba ma byc mniejsza
        for i in range(self.bits):
            if random.randint(1, 100) > prob:
                if self.message[i] == 0:
                    self.message[i] = 1
                else:
                    self.message[i] = 0

    def print(self):                                                            # wypisuje ciag bitow
        for i in range(self.bits):
            print(self.message[i], end="")
        print("\n")
        for i in range(self.frameSize[0]):
            for j in range(self.frameSize[1] + 1):
                print(self.frames[i][j], end="")
            print("\n")

    def parityBit(self, frame):                                                 # wyznaczanie bitu parzystosci
        sum = 0
        for j in range(len(frame)):
            sum += frame[j]
        frame.append(sum % 2)

    def createFrames(self):                                                     # dzielenie na ramki
        for i in range(self.frameSize[0]):
            self.frames.append([])
            for j in range(self.frameSize[1]):
                self.frames[i].append(self.message[i*self.frameSize[1]+j])
            self.parityBit(self.frames[i])

def test():
    m = Model()
    # m.print()
    m.createFrames();
    print("\n")
    m.print()

if __name__ == '__main__':
    test()