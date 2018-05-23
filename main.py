import bigfile
import csv


topList = [['第一名', 'name', 'id', '一等奖学金'], ['第二名', 'name', 'id', '一等奖学金'],
           ['第三名', 'name', 'id', '一等奖学金'], ['第四名', 'name', 'id', '一等奖学金'],
           ['第五名', 'name', 'id', '二等奖学金'], ['第六名', 'name', 'id', '二等奖学金'],
           ['第七名', 'name', 'id', '二等奖学金'], ['第八名', 'name', 'id', '二等奖学金'],
           ['第九名', 'name', 'id', '二等奖学金'], ['第十名', 'name', 'id', '二等奖学金']]


def showTop10Student():
    print('名次'.ljust(10), '姓名'.ljust(10), '学号'.ljust(10), '奖学金'.ljust(10))

    with open('SortedFile.csv', 'r') as file:
        reader = csv.reader(file)

        for i in range(10):
            try:
                currentReadLine = next(reader)
            except StopIteration:
                break

            topList[i][1] = currentReadLine[0]
            topList[i][2] = currentReadLine[1]
            print(topList[i][0].ljust(10), topList[i][1].ljust(10), topList[i][2].ljust(10), topList[i][3].ljust(10))


if __name__ == '__main__':
    print('欢迎使用学生期末成绩综合评比系统')
    print('----------------------------')

    filePath = input('请输入完整原文件路径：')
    print('\n\n处理中，请稍候...\n\n')

    try:
        bigfile.sortBigFile(filePath)
    except BaseException:
        print('排序过程出现异常。如重新尝试后依然出现错误，请与我们取得联系。\n')
    else:
        showTop10Student()
        print('\n\n完整排序文件已保存至 \'SortedFile.csv\'')