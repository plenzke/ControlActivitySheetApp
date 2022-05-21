import classes
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
institute = classes.Institute()

#Optional Argument
subparser = parser.add_subparsers(dest='command')

#Добавление нового студента
add_student = subparser.add_parser("add_student", help="Добавить нового студента")
add_student.add_argument("student_name", type=str, help='Student FIO')
add_student.add_argument("student_code", type=int, help='Student Code')

#Добавление новой специализации
add_spec = subparser.add_parser("add_spec", help="Добавить новую специализацию")
add_spec.add_argument("spec_name", type=str, help='Specialization name')

#Добавление нового предмета
add_subject = subparser.add_parser("add_subject", help="Добавить новый предмет")
add_subject.add_argument("id", type=str, help="Subject ID")
add_subject.add_argument("subject_name", type=str, help="Subject name")
add_subject.add_argument("subject_semester", type=int, help="Subject semester")
add_subject.add_argument("subject_hours", type=int, help="Subject hours")
add_subject.add_argument("subject_spec", type=str, help="Subject specialization")

#Добавление новой группы
add_group = subparser.add_parser("add_group", help="Добавить новую группу")
add_group.add_argument("group_name", type=str, help="Group name")
add_group.add_argument("group_year", type=int, help="Group year")
add_group.add_argument("group_spec", type=str, help="Group specialization")

#Добавление нового экзамена
add_exam = subparser.add_parser("add_exam", help="Добавить новый экзамен")
add_exam.add_argument("exam_subject", type=str, help="Exam subject")
add_exam.add_argument("exam_date", type=str, help="Exam date, Format=DD.MM.YYYY (STR)")
add_exam.add_argument("exam_year", type=str, help="Exam year")
add_exam.add_argument("exam_lecturer", type=str, help="Exam lecturer FIO")

#Добавление нового результата экзамена
add_exam_result = subparser.add_parser("add_exam_result", help="Добавить новый результат экзамена")
add_exam_result.add_argument("exam_result_student", type=int, help="Student ID (INT)")
add_exam_result.add_argument("exam_points", type=int, help="Exam points (INT)")
add_exam_result.add_argument("exam_result_points", type=int, help="Exam result points (INT)")

#Получение существующего студента
get_student = subparser.add_parser("get_student", help="Получить существующего студента")
get_student.add_argument("student_id", type=int, help="Student ID (INT)")

#Получение существующей специализации
get_spec = subparser.add_parser("get_spec", help="Получить существующую специализацию")
get_spec.add_argument("spec_name", type=str, help="Specialization name (STR)")

#Получение существующего предмета
get_subject = subparser.add_parser("get_subject", help="Получить существующий предмет")
get_subject.add_argument("subject_id", type=str, help="Subject ID (STR)")

#Получение существующей группы
get_group = subparser.add_parser("get_group", help="Получить существующую группу")
get_group.add_argument("group_name", type=str, help="Group name (STR)")

#получить существующий экзамен
get_exam = subparser.add_parser("get_exam", help="Получить существующий экзамен")
get_exam.add_argument("exam_name", type=str, help="Exam name (STR)")
get_exam.add_argument("exam_date", type=str, help="Exam date, Format=DD.MM.YYYY (STR)")

#Получить существующий результат экзамена
get_exam_result = subparser.add_parser("get_exam_result", help="Получить существующий результат экзамена")
get_exam_result.add_argument("exam_result_id", type=int, help="Student ID (INT)")

args = parser.parse_args()

def add_stud(args):
    student = classes.Student(args.student_name, args.student_code)
    institute.addStudent(student)
    print(student)

def add_spec(args):
    spec = classes.Specialization(args.spec_name)
    institute.addSpecs(spec)
    print(spec)

def add_subj(args):
    spec = classes.Specialization(args.subject_spec)
    subject = classes.Subject(args.id, args.subject_name, args.subject_semester, args.subject_hours, spec)
    institute.addSubject(subject)
    print(subject)

def add_group(args):
    spec = classes.Specialization(args.group_spec)
    group = classes.Group(args.group_name, args.group_year, spec)
    institute.addGroup(group)
    print(group)

def add_exam(args):
    subject = institute.getSubject(args.exam_subject)
    exdate = datetime.strptime(args.exam_date, "%d.%m.%Y").date()
    exam = classes.Exam(subject, exdate, args.exam_year, args.exam_lecturer)
    institute.addExam(exam)
    print(exam)

def add_exam_result(args):
    stud = institute.getStudent(args.exam_result_student)
    exam_result = classes.ExamPoints(stud, args.exam_points, args.exam_result_points)
    institute.addExamResult(exam_result)
    print(exam_result)

def get_student(args):
    print(institute.getStudent(args.student_id))

def get_spec(args):
    print(institute.getSpec(args.spec_name))

def get_subject(args):
    print(institute.getSubject(args.subject_id))

def get_group(args):
    print(institute.getGroup(args.group_name))

def get_exam(args):
    print(institute.getExam(args.exam_name, args.exam_date))

def get_exam_result(args):
    print(institute.getExamPoints(args.exam_result_id))

if args.command == 'add_student':
    print(args.student_name)
    add_stud(args)
elif args.command == 'add_spec':
    add_spec(args)
elif args.command == 'add_subject':
    add_subj(args)
elif args.command == 'add_group':
    add_group(args)
elif args.command == 'add_exam':
    add_exam(args)
elif args.command == 'add_exam_result':
    add_exam_result(args)
elif args.command == 'get_student':
    get_student(args)
elif args.command == 'get_spec':
    get_spec(args)
elif args.command == 'get_subject':
    get_subject(args)
elif args.command == 'get_group':
    get_group(args)
elif args.command == 'get_exam':
    get_exam(args)
elif args.command == 'get_exam_result':
    get_exam_result(args)
