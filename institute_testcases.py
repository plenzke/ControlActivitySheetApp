from datetime import date
from classes import Student, Specialization, Subject, Group, Exam, ExamPoints, Institute
import unittest

class addStudent_testcase(unittest.TestCase):
    def test_adding(self):
        student = Student('Павлов Вячеслав Июльевич', 185774)
        inst = Institute()
        inst.addStudent(student)
        self.assertEqual(len(inst.students), 1)

class addSubject_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization('ФИИТ')
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        inst = Institute()
        inst.addSubject(subject)
        self.assertEqual(len(inst.subjects), 1)

class addGroup_testcase(unittest.TestCase):
    def test_adding(self):
        spec = "ФИИТ"
        group = Group("М-ФИИТ-21", 2021, spec)
        inst = Institute()
        inst.addGroup(group)
        self.assertEqual(len(inst.groups), 1)

class addSpecs_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization("ФИИТ")
        inst = Institute()
        inst.addSpecs(spec)
        self.assertEqual(len(inst.specs), 1)

class addExam_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam = Exam(subject, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.addExam(exam)
        self.assertEqual(len(inst.exams), 1)

class addExamResult_testcase(unittest.TestCase):
    def test_adding(self):
        student = Student("Павлов Вячеслав Июльевич", 185774)
        examPoints = ExamPoints(student, 60, 30)
        inst = Institute()
        inst.addExamResult(examPoints)
        self.assertEqual(len(inst.exam_results), 1)

if __name__ == '__main__':
    unittest.main()