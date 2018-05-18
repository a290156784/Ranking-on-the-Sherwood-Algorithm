import random


class Student:                                                     # 学生类
    name = 'default'
    id = 0
    chineseGrade = 0
    englishGrade = 0
    mathGrade = 0
    average = 0

    def __init__(self, inputName, inputID, inputChiGrade, inputEngGrade, inputMathGrade):   # 用于初始化学生类成员变量的值
        self.name = inputName
        self.id = inputID
        self.chineseGrade = inputChiGrade
        self.englishGrade = inputEngGrade
        self.mathGrade = inputMathGrade
        self.average = (inputMathGrade+inputMathGrade+inputEngGrade)/3


studentList = []

student1 = Student('jam', 10001, 98, 100, 99)
student2 = Student('dong', 10002, 99, 99, 97)
student3 = Student('ma', 10003, 100, 100, 100)
student4 = Student('zhou', 10004, 95, 92, 96)
student5 = Student('xu', 10005, 85, 82, 81)
student6 = Student('shun', 10006, 90, 72, 66)
student7 = Student('kun', 10007, 23, 18, 93)
student8 = Student('bo', 10008, 98, 57, 93)
student9 = Student('xiang', 10009, 91, 66, 92)

studentList = studentList + [student1, student2, student3, student4, student5, student6, student7, student8, student9]

listLenth = len(studentList)


def quickSort(left, right):
    if(left < right):
        randomLeft = left                                           # 随机产生一个范围在当前列表内的整数
        randomBase = random.randint(left, right)

        randomTemp = studentList[randomLeft]                        # 将随机选出的元素交换至最左侧设为基准数
        studentList[randomLeft] = studentList[randomBase]
        studentList[randomBase] = randomTemp

        mid = partition(left, right)                                # 进行排序运算，找出当前轮次基准数的位置
        quickSort(left, mid-1)                                      # 分治
        quickSort(mid+1, right)


def partition(l, r):                                                # 快速排序
    i = l
    j = r
    temp = studentList[l].average

    while i!=j:                                                     # 找出比基准数小和大的数，分别排至基准数左右
        while studentList[j].average<=temp and j>i:
            j -= 1
        while studentList[i].average>=temp and i<j:
            i += 1
        temp2 = studentList[i]
        studentList[i] = studentList[j]
        studentList[j] = temp2

    temp3 = studentList[l]                                          # 将位于列表最左侧的基准数交换至其应该在的位置
    studentList[l] = studentList[i]
    studentList[i] =temp3
    return i


quickSort(0, listLenth-1)

for currentOutputStudent in studentList:
    print(currentOutputStudent.name, '   ', currentOutputStudent.id, '   ',\
    currentOutputStudent.chineseGrade, '   ', currentOutputStudent.englishGrade, '   ',\
    currentOutputStudent.mathGrade, '   ', currentOutputStudent.average)
    print('\n')