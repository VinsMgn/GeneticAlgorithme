import random
import string
import difflib


class Inidividual:
    def __init__(self, target):
        self.matchPhrase = self.generateRandomIndividual(target)
        self.sizePhrase = len(target)
        self.generateFitness(target, self.matchPhrase)

    @staticmethod
    def generateRandomIndividual(finalWord):
        letters = string.ascii_lowercase + ' '
        # letters = string.printable
        return ''.join(random.choice(letters) for i in range(len(finalWord)))

    @staticmethod
    def generateFitness(target, compareWord):
        print("Fitness : {}".format(difflib.SequenceMatcher(None, target, compareWord).ratio()))

