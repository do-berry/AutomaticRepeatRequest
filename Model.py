import random
import time


class Model:
    message = []                                                                                                        # ciag ktory bedziemy przesylac
    bits = 100                                                                                                           # ile bitow w wiadomosci
    frames = []                                                                                                         # lista list == lista z ramkami
    howManyFrames = 20
    frameLength = 5
    framesWithErrors = []

    def fillMessage(self):
        for i in range(self.bits):
            self.message.append(random.randint(0, 1))                                                                   # uzupelnia message 0 lub 1

    def printFrames(self, frame):                                                                                       # wypisuje ciag bitow
        for i in range(self.howManyFrames):
            for j in range(self.frameLength):
                print(frame[i][j], end="")
            print('\n')

    def parityBit(self, frame):                                                                                         # wyznaczanie bitu parzystosci
        sum = 0
        for j in range(self.frameLength):
            sum += frame[j]
        return (sum % 2)

    def createFrames(self):                                                                                             # dzielenie na ramki
        for i in range(self.howManyFrames):
            self.frames.append([])
            for j in range(self.frameLength):
                self.frames[i].append(self.message[i * self.frameLength + j])
            self.frames[i].append(self.parityBit(self.frames[i]))

    def generateErrors(self):                                                                                           # tworzenie bledow i wpisywanie
        counter = 0                                                                                                     # ich do framesWithErrors
        correctlySent = 0
        incorrectlySent = 0
        while counter < self.howManyFrames:
            self.framesWithErrors.append([])
            prob = 90                                                                                                   # prawdopodobienstwo do ktorego bd porownywac
            for i in range(self.frameLength + 1):
                a = random.randint(0,100)
                if a < prob:                                                                                            # jesli a mniejsze
                    self.framesWithErrors[counter].append(self.frames[counter][i])                                      # wpisz co jest
                else:                                                                                                   # jak nie
                    if self.frames[counter][i] == 1:                                                                    # to podmien
                        self.framesWithErrors[counter].append(0)
                    else:
                        self.framesWithErrors[counter].append(1)
            pb = self.parityBit(self.framesWithErrors[counter])                                                         # jaki wyjdzie bit parzystosci
            if pb == self.framesWithErrors[counter][self.frameLength]:                                                  # jesli jest k
                counter += 1
                correctlySent += 1
                time.sleep(2)
                print("The parity bit for ", counter, " frame is correct!\n")
            else:                                                                                                       # jesli !k
                self.framesWithErrors.remove(self.framesWithErrors[counter])
                incorrectlySent += 1
                time.sleep(2)
                print("The parity bit is incorrect, ", counter + 1, " frame is sent once again.\n")
        print("Frames were correctly sent ", correctlySent, " times.")
        print("Frames were incorrectly sent ", incorrectlySent, " times.")