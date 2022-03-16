from dataclasses import dataclass
from datetime import date

@dataclass
class Student:
    fio: str
    id: int

    def __init__(self, new_fio: str, new_id: int):
        #self.fio = new_fio
        self.id = new_id

@dataclass
class Specialization:
    name: str

    def __init__(self, new_name: str):
        self.name = new_name

@dataclass
class Subject:
    id: str
    name: str
    semester: int
    hours: int
    spec: Specialization

    def __init__(self, new_id: str, new_name: str, new_semester: int, new_hours: int, new_spec: Specialization):
        self.id = new_id
        self.name = new_name
        self.semester = new_semester
        self.hours = new_hours
        self.spec = new_spec

@dataclass
class Group:
    name: str
    year: int
    spec: Specialization

    def __init__(self, new_name: str, new_year: int, new_spec: Specialization):
        self.name = new_name
        self.year = new_year
        self.spec = new_spec

@dataclass
class Exam:
    subject: Subject
    examDate: date
    year: str
    lecturer_fio: str

    def __init__(self, new_subject: Subject, new_examDate: date, new_year: str, new_lectFio: str):
        self.subject = new_subject
        self.examDate = new_examDate
        self.year = new_year
        self.lecturer_fio = new_lectFio

@dataclass
class ExamPoints:
    student: Student
    Points: int
    examPoints: int

    def __init__(self, new_student: Student, new_Points: int, new_examPoints: int):
        self.student = new_student
        self.Points = new_Points
        self.examPoints = new_examPoints