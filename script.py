from individu import Inidividual
import difflib

nbOfIndividual = 500
percentageOfSelection = 0.1
hardTarget = "le superbawl c cool"


def generateRandom():
    individus = []
    for i in range(0, nbOfIndividual):
        individus.append(Inidividual(hardTarget))
        print("Random individual : " + individus[i].matchPhrase)


def main():
    generateRandom()


main()
