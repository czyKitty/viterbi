import sys
import math
from viterbi import*
from genDieNumber import*

def evaluate():
    seqLen = []
    avg_accuracy = []
    avg_MCC = []
    for n in range(1000,10100,100):
        for i in range(0,10):
            accuracy = []
            MCC = []
            data = genDieNumber(n)
            true_result = data[1]
            prediction = viterbi(data[0])
            TP = 0
            TN = 0
            FP = 0
            FN = 0
            for i in range(0,len(data[0])):
                if true_result[i] == "F":
                    if prediction[i] == "F":
                        TP += 1
                    else:
                        FN += 1
                else:
                    if prediction[i] == "F":
                        FP += 1
                    else:
                        TN += 1
            accuracy.append((TP+TN)/(TP+TN+FP+FN))
            if (TP+TN)*(TP+FP)*(TN+FP)*(TN+FN) != 0:
                MCC.append((TP*TN-FP*FN)/math.sqrt((TP+TN)*(TP+FP)*(TN+FP)*(TN+FN)))
            else:
                MCC.append((TP*TN-FP*FN)/0.000001)

        seqLen.append(n)
        avg_accuracy.append(sum(accuracy)/len(accuracy))
        avg_MCC.append(sum(MCC)/len(MCC))
    return [seqLen,avg_accuracy,avg_MCC]

def main():
    outFileName = sys.argv[1]
    outFile = open(outFileName,'w')
    result = evaluate()
    outFile.write("Length: "+"\n")
    for i in range(0,len(result[0])):
        outFile.write(str(result[0][i])+"\n")
    outFile.write("Accuracy: "+"\n")
    for i in range(0,len(result[1])):
        outFile.write(str(result[1][i])+"\n")
    outFile.write("MCC: "+"\n")
    for i in range(0,len(result[2])):
        outFile.write(str(result[2][i])+"\n")
main()