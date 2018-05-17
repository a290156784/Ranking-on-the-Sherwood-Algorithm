class Student:
    name = 'defaule'
    id = 0
    chineseGrade = 0
    englishGrade = 0
    mathGrade = 0
    average = 0
    def __init__(self, inputName, inputID, inputChiGrade, inputEngGrade, inputMathGrade):
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