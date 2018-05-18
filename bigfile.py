#用来模拟外部排序
import random



def mergeSonFile(fileCount):

    fileAName = 'sonFile' + str(1) + '.txt'
    fileBName = 'sonFile' + str(2) + '.txt'

    with open(fileAName, 'r') as fileA:
        with open(fileBName, 'r') as fileB:





def createSonFile(fileCount, tempList, lineCount):
    tempList.sort(reverse=True)     #排序

    fileName = 'sonFile' + str(fileCount) + '.txt'

    with open(fileName, 'w+') as file:
        for i in range(lineCount):
            currentStr = str(tempList[i])
            if i != (lineCount-1):
                currentStr = currentStr + '\n'
            file.write(currentStr)


def splitBigFile():
    lineCount = 0
    fileCount = 0
    tempList = [0] * 100

    with open('OriginFile.txt', 'r') as bigFile:
        for currentReadLine in bigFile:
            currentReadLine = currentReadLine.rstrip('\n')
            tempList[lineCount] = int(currentReadLine, 10)
            lineCount += 1

            if lineCount == 100:
                fileCount += 1
                createSonFile(fileCount, tempList, lineCount)
                lineCount = 0

        if lineCount != 0:
            fileCount += 1
            createSonFile(fileCount, tempList, lineCount)

    return fileCount


fileCount = splitBigFile()