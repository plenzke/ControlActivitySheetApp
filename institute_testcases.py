from datetime import date
from classes import Student, Specialization, Subject, Group, Exam, ExamPoints, Institute
import unittest

class addStudent_testcase(unittest.TestCase):
    def test_adding(self):
        student = Student('Павлов Вячеслав Июльевич', 185774)
        inst = Institute()
        inst.addStudent(student)
        self.assertEqual(len(inst.students), 1)

    def test_adding_2(self):
        student_1 = Student('Павлов Вячеслав Июльевич', 185774)
        student_2 = Student('Иванов Иван Иванович', 185773)
        inst = Institute()
        inst.addStudent(student_1)
        inst.addStudent(student_2)
        self.assertEqual(len(inst.students), 2)

class addSubject_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization('ФИИТ')
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        inst = Institute()
        inst.addSubject(subject)
        self.assertEqual(len(inst.subjects), 1)

    def test_adding_2(self):
        spec = Specialization('ФИИТ')
        subject_1 = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        subject_2 = Subject("Б1.В.01", "Английский язык", 2, 108, spec)
        inst = Institute()
        inst.addSubject(subject_1)
        inst.addSubject(subject_2)
        self.assertEqual(len(inst.subjects), 2)

class addGroup_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, spec)
        inst = Institute()
        inst.addGroup(group)
        self.assertEqual(len(inst.groups), 1)

    def test_adding_2(self):
        spec = Specialization('ФИИТ')
        group_1 = Group("М-ФИИТ-21", 2021, spec)
        group_2 = Group("М-ИВТ-21", 2021, spec)
        inst = Institute()
        inst.addGroup(group_1)
        inst.addGroup(group_2)
        self.assertEqual(len(inst.groups), 2)

class addSpecs_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization("ФИИТ")
        inst = Institute()
        inst.addSpecs(spec)
        self.assertEqual(len(inst.specs), 1)

    def test_adding_2(self):
        spec_1 = Specialization("ФИИТ")
        spec_2 = Specialization("ИВТ")
        inst = Institute()
        inst.addSpecs(spec_1)
        inst.addSpecs(spec_2)
        self.assertEqual(len(inst.specs), 2)

class addExam_testcase(unittest.TestCase):
    def test_adding(self):
        spec = Specialization("ФИИТ")
        subject = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam = Exam(subject, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.addExam(exam)
        self.assertEqual(len(inst.exams), 1)

    def test_adding_2(self):
        spec = Specialization("ФИИТ")
        subject_1 = Subject("Б1.В.02", "Методы тестирования и верификации программных продуктов", 2, 108, spec)
        subject_2 = Subject("Б1.В.01", "Английский язык", 2, 108, spec)
        examDate = date(2022, 1, 1)
        exam_1 = Exam(subject_1, examDate, "2021-2022", "Эверстов Владимир Васильевич")
        exam_2 = Exam(subject_2, examDate, "2021-2022", "Иванова Иванна Ивановна")
        inst = Institute()
        inst.addExam(exam_1)
        inst.addExam(exam_2)
        self.assertEqual(len(inst.exams), 2)

class addExamResult_testcase(unittest.TestCase):
    def test_adding(self):
        student = Student("Павлов Вячеслав Июльевич", 185774)
        examPoints = ExamPoints(student, 60, 30)
        inst = Institute()
        inst.addExamResult(examPoints)
        self.assertEqual(len(inst.exam_results), 1)

    def test_adding_2(self):
        student_1 = Student("Павлов Вячеслав Июльевич", 185774)
        student_2 = Student("Иванов Иван Иванович", 185773)
        examPoints_1 = ExamPoints(student_1, 60, 30)
        examPoints_2 = ExamPoints(student_2, 60, 30)
        inst = Institute()
        inst.addExamResult(examPoints_1)
        inst.addExamResult(examPoints_2)
        self.assertEqual(len(inst.exam_results), 2)

if __name__ == '__main__':
    unittest.main()