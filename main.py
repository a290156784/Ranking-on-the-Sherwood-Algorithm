import bigfile

if __name__ == '__main__':
    print('欢迎使用学生期末成绩综合评比系统')
    print('----------------------------')

    filePath = input('请输入完整原文件路径：')
    bigfile.sortBigFile(filePath)