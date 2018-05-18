# 模拟外部排序
import csv
import quicksort


def copyTempToSortedFile():
    with open('tempFile.csv', 'r') as tempFile:
        with open('SortedFile.csv', 'w+', newline='') as sortedFile:
            reader = csv.reader(tempFile)
            writer = csv.writer(sortedFile)
            for currentReadLine in reader:
                writer.writerow(currentReadLine)


def mergeSonFile(sonFileNum):
    sonFileName = 'sonFile' + str(sonFileNum) + '.csv'

    with open('tempFile.csv', 'w+', newline='') as tempFile:                # 将已排序的文件和一个新文件进行合并排序，并将结果存入tempFile.csv
        with open('SortedFile.csv', 'r') as sortedFile:
            with open(sonFileName, 'r') as sonFile:
                    sortedReader = csv.reader(sortedFile)
                    sonReader = csv.reader(sonFile)
                    writer = csv.writer(tempFile)

                    sortedFileLine = next(sortedReader)
                    sonFileLine = next(sonReader)

                    sortedFileLengh = len(sortedFileLine)
                    sonFileLengh = len(sortedFileLine)

                    while sortedFileLine and sonFileLine:
                        currentSortedNum = int(sortedFileLine[sortedFileLengh - 1], 10)
                        currentSonNum = int(sonFileLine[sonFileLengh - 1], 10)

                        if currentSortedNum >= currentSonNum:
                            writer.writerow(sortedFileLine)
                            sortedFileLine = next(sortedReader)

                        else:
                            writer.writerow(sonFileLine)
                            sonFileLine = next(sonReader)

                    while sortedFileLine:
                        writer.writerow(sortedFileLine)
                        sortedFileLine = next(sortedReader)

                    while sonFileLine:
                        writer.writerow(sonFileLine)
                        sonFileLine = next(sonReader)

    copyTempToSortedFile()                                      # 调用函数将tempFile.csv内结果覆盖拷贝至排序结果文件中


def copyFirstSonFileToSortedFile():
    with open('SortedFile.csv', 'w+', newline='') as sortedFile:
        with open('sonFile1.csv', 'r') as sonFile1:
            reader = csv.reader(sonFile1)
            writer = csv.writer(sortedFile)
            for currentReadLine in reader:
                writer.writerow(currentReadLine)


def createSonFile(fileCount, tempList, lineCount):
    quicksort.quickSort(0, (lineCount-1), tempList)     #排序

    fileName = 'sonFile' + str(fileCount) + '.csv'

    with open(fileName, 'w+', newline='') as file:
        writer = csv.writer(file)
        for i in range(lineCount):
            writer.writerow(tempList[i])


def splitBigFile(filePath):
    lineCount = 0
    fileCount = 0
    tempList = [0] * 100

    with open(filePath, 'r') as bigFile:
        bigFileReader = csv.reader(bigFile)
        for currentReadLine in bigFileReader:
            tempList[lineCount] = currentReadLine
            tempList[lineCount].append((int(tempList[lineCount][2], 10) + int(tempList[lineCount][3], 10) + int(tempList[lineCount][4], 10))/3)
            lineCount += 1

            if lineCount == 100:
                fileCount += 1
                createSonFile(fileCount, tempList, lineCount)
                lineCount = 0

        if lineCount != 0:
            fileCount += 1
            createSonFile(fileCount, tempList, lineCount)

    return fileCount


def sortBigFile(filePath):
    fileCount = splitBigFile(filePath)
    copyTempToSortedFile()

    if fileCount != 1:
        for i in range((fileCount-1)):
            mergeSonFile((i+2))