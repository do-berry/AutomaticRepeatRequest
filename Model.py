import random
import time


class Model:
    message = []                                                                                                        # ciag ktory bedziemy przesylac
    bits = 100                                                                                                          # ile bitow w wiadomosci
    sentFrames = []                                                                                                     # lista ramek ktora wysylamy
    receivedFrames = []                                                                                                 # odbierana lista ramek
    badFrames = []                                                                                                      # nry zlych ramek
    howManyFrames = 20                                                                                                  # ilosc utworzonych ramek
    frameLength = 5                                                                                                     # dlugosc 1 ramki
    prob = 90                                                                                                           # prawdopodobienstwo zepsucia
    incorrectlySent = 0                                                                                                 # stat: niepoprawne (suma)
    correctlySent = 0                                                                                                   # stat: poprawne (suma)

    def fillBadFrames(self):
        self.badFrames = list(range(self.howManyFrames))

    def fillMessage(self):
        for i in range(self.bits):
            self.message.append(random.randint(0, 1))                                                                   # uzupelnia message 0 lub 1

    def printFrames(self, frame):                                                                                       # wypisuje ciag bitow
        for i in range(self.howManyFrames):
            print(frame[i], end="")
            print('\n')

    def parityBit(self, frame):                                                                                         # wyznaczanie bitu parzystosci
        sum = 0
        for j in range(self.frameLength):
            sum += frame[j]
        return (sum % 2)

    def createFrames(self):                                                                                             # dzielenie na ramki
        for i in range(self.howManyFrames):
            self.sentFrames.append([])
            for j in range(self.frameLength):
                self.sentFrames[i].append(self.message[i * self.frameLength + j])
            self.sentFrames[i].append(self.parityBit(self.sentFrames[i]))

    def stopAndWait(self):                                                                                              # tworzenie bledow i wpisywanie
        counter = 0                                                                                                     # ich do receivedFrames
        while counter < self.howManyFrames:
            self.receivedFrames.append([])                                                                              # prawdopodobienstwo do ktorego bd porownywac
            for i in range(self.frameLength + 1):
                a = random.randint(0,100)
                if a < self.prob:                                                                                       # jesli a mniejsze
                    self.receivedFrames[counter].append(self.sentFrames[counter][i])                                    # wpisz co jest
                else:                                                                                                   # jak nie
                    if self.sentFrames[counter][i] == 1:                                                                # to podmien
                        self.receivedFrames[counter].append(0)
                    else:
                        self.receivedFrames[counter].append(1)
            pb = self.parityBit(self.receivedFrames[counter])                                                           # jaki wyjdzie bit parzystosci
            if pb == self.receivedFrames[counter][self.frameLength]:                                                    # jesli jest k
                counter += 1
                self.correctlySent += 1
                time.sleep(1)
                print("The parity bit for ", counter - 1, " frame is correct!")                                       # wczesniej jest inkrementowana zmienna jbc
            else:                                                                                                       # jesli !k
                self.receivedFrames.remove(self.receivedFrames[counter])
                self.incorrectlySent += 1
                time.sleep(1)
                print("The parity bit is incorrect, ", counter, " frame is sent once again.")
        print("Frames were correctly sent ", self.correctlySent, " times.")
        print("Frames were incorrectly sent ", self.incorrectlySent, " times.")

    def selectiveRepeat(self):
        for counter in range(len(self.sentFrames)):
            if self.badFrames.__contains__(counter):                                                                    # jesli w liscie badFrames jest numer ramki to wysylamy
                self.receivedFrames.append([])
                for i in range(self.frameLength + 1):
                    a = random.randint(0, 100)
                    if a < self.prob:
                        self.receivedFrames[counter].append(self.sentFrames[counter][i])
                    else:
                        if self.sentFrames[counter][i] == 1:
                            self.receivedFrames[counter].append(0)
                        else:
                            self.receivedFrames[counter].append(1)
                pb = self.parityBit(self.receivedFrames[counter])
                if pb == self.receivedFrames[counter][self.frameLength]:
                    self.correctlySent += 1
                    self.badFrames.remove(counter)
                    time.sleep(1)
                    print("The parity bit for ", counter, " frame is correct! removed")
                else:
                    self.receivedFrames[counter] = []                                                                   # jak zle wyslana to czyszczenie ramki sposobem NASA
                    self.incorrectlySent += 1
                    time.sleep(1)
                    print("The parity bit is incorrect, ", counter, " frame not removed.")
        if len(self.badFrames) != 0:
            print("Created retransmit list: ", self.badFrames)
            print("Retransmition ", self.correctlySent, "/", self.incorrectlySent)
            self.selectiveRepeat()
        else:
            print("Sending completed! Result: ", self.correctlySent, " correctly sent frames, ", self.incorrectlySent,
                  " incorrectly sent frames.\n")