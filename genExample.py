import sys
import math
from genDieNumber import*
from viterbi import*

def main():
    outFileName = sys.argv[1]
    n = int(sys.argv[2])
    outFile = open(outFileName,'w')
    
    data = genDieNumber(n)
    prediction = viterbi(data[0])
    for i in range(0,len(prediction)//50):
        outFile.write("Rolls    ")
        for j in range(0,50):
            outFile.write(str(data[0][j]))
        outFile.write("\n")
        outFile.write("Die      ")
        for j in range(0,50):
            outFile.write(str(data[1][j]))
        outFile.write("\n")
        outFile.write("Viterbi  ")
        for j in range(0,50):
            outFile.write(str(prediction[j]))
        outFile.write("\n")
main()
