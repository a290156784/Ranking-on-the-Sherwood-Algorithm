# 模拟外部排序
import csv
import quicksort


def copyTempToSortedFile():
    with open('tempFile.csv', 'r') as tempFile:
        reader = csv.reader(tempFile)
        with open('SortedFile.csv', mode='w+', newline='') as sortedFile:
            writer = csv.writer(sortedFile)

            for currentReadLine in reader:
                writer.writerow(currentReadLine)


def mergeSonFile(sonFileNum):
    sonFileName = 'sonFile' + str(sonFileNum) + '.csv'

    with open('tempFile.csv', mode='w+', newline='') as tempFile:                # 将已排序的文件和一个新文件进行合并排序，并将结果存入tempFile.csv
        writer = csv.writer(tempFile)
        with open('SortedFile.csv', 'r') as sortedFile:
            sortedReader = csv.reader(sortedFile)
            with open(sonFileName, 'r') as sonFile:
                    sonReader = csv.reader(sonFile)

                    try:
                        sortedFileLine = next(sortedReader)
                        sonFileLine = next(sonReader)
                    finally:
                        print('')


                    while sortedFileLine and sonFileLine:
                        currentSortedNum = float(sortedFileLine[5])
                        currentSonNum = float(sonFileLine[5])

                        if currentSortedNum >= currentSonNum:
                            writer.writerow(sortedFileLine)
                            try:
                                sortedFileLine = next(sortedReader)
                            except StopIteration:
                                flag = 0
                                break

                        else:
                            writer.writerow(sonFileLine)
                            try:
                                sonFileLine = next(sonReader)
                            except StopIteration:
                                flag = 1
                                break

                    while flag != 0:
                        writer.writerow(sortedFileLine)
                        try:
                            sortedFileLine = next(sortedReader)
                        except StopIteration:
                            break

                    while flag != 1:
                        writer.writerow(sonFileLine)
                        try:
                            sonFileLine = next(sonReader)
                        except StopIteration:
                            break


def copyFirstSonFileToSortedFile():
    with open('SortedFile.csv', mode='w+', newline='') as sortedFile:
        writer = csv.writer(sortedFile)
        with open('sonFile1.csv', 'r') as sonFile1:
            reader = csv.reader(sonFile1)
            for currentReadLine in reader:
                writer.writerow(currentReadLine)


def createSonFile(fileCount, tempList, lineCount):
    quicksort.quickSort(0, (lineCount-1), tempList)     #排序

    fileName = 'sonFile' + str(fileCount) + '.csv'

    with open(fileName, mode='w+', newline='') as file:
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
    copyFirstSonFileToSortedFile()

    if fileCount != 1:
        for i in range((fileCount-1)):
            mergeSonFile((i+2))
            copyTempToSortedFile()