import random
from random import randint, choice
from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from db import session
from model import Teacher, Student, Subject, Group, Grade


fake = Faker()

def insert_student_groups():
    for _ in range(3):
        group = Group(
            group_name=fake.word(),
            description=fake.sentence(), 
        )
        session.add(group)
       

def insert_students(groups):
    for _ in range(50):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth= fake.date_of_birth(minimum_age=18, maximum_age=30),
            gender = fake.random_element(elements=('Male', 'Female')), 
            group=random.choice(groups)
        )
        session.add(student)


def insert_teachers():
    for _ in range(5):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),  
        )
        session.add(teacher)


def insert_subject(teachers):
    for _ in range(8):
        subject = Subject(
            subject_name=fake.job(),
            subject_description=fake.sentence(),
            teacher=random.choice(teachers)
        )
        session.add(subject)

def insert_grade():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for _ in range(20):
        grade = Grade(
            grade=fake.random_int(min=1, max=10),
            date_received=fake.date_between(start_date='-1y', end_date='today'),
            student=random.choice(students),
            subject=random.choice(subjects)
        )
        session.add(grade)



if __name__ == '__main__':
    try:
        insert_student_groups()
        groups = session.query(Group).all()
        insert_students(groups)
        insert_teachers()
        teachers = session.query(Teacher).all()
        insert_subject(teachers)
        insert_grade()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()

