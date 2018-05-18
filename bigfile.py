#用来模拟外部排序
import random


def copyTempToSortedFile():
    with open('tempFile.txt', 'r') as tempFile:
        with open('SortedFile.txt', 'w+') as sortedFile:
            for currentReadLine in tempFile:
                sortedFile.write(currentReadLine)


def mergeSonFile(sonFileNum):
    sonFileName = 'sonFile' + str(sonFileNum) + '.txt'

    with open('tempFile.txt', 'w+') as tempFile:
        with open('SortedFile.txt', 'r') as sortedFile:
            with open(sonFileName, 'r') as sonFile:

                    sortedFileLine = sortedFile.readline()
                    sonFileLine = sonFile.readline()

                    while sortedFileLine and sonFileLine:
                        currentSortedNum = int(sortedFileLine.rstrip('\n'), 10)
                        currentSonNum = int(sonFileLine.rstrip('\n'), 10)

                        if currentSortedNum >= currentSonNum:
                            tempFile.write(sortedFileLine)
                            sortedFileLine = sortedFile.readline()

                        else:
                            if sonFileLine.find('\n') == -1:
                                sonFileLine = sonFileLine + '\n'
                            tempFile.write(sonFileLine)
                            sonFileLine = sonFile.readline()

                    while sortedFileLine:
                        tempFile.write(sortedFileLine)
                        sortedFileLine = sortedFile.readline()

                    while sonFileLine:
                        if sonFileLine.find('\n') == -1:
                            sonFileLine = sonFileLine + '\n'
                        tempFile.write(sonFileLine)
                        sonFileLine = sonFile.readline()

    copyTempToSortedFile()


def copyFirstSonFileToSortedFile():
    with open('SortedFile.txt', 'w+') as sortedFile:
        with open('sonFile1.txt', 'r') as sonFile1:

            for currentReadLine in sonFile1:
                if currentReadLine.find('\n') == -1:
                    currentReadLine = currentReadLine + '\n'
                sortedFile.write(currentReadLine)


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
copyFirstSonFileToSortedFile()

for i in range((fileCount-1)):
    mergeSonFile((i+2))