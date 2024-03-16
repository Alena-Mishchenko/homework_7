from datetime import datetime


from sqlalchemy import and_, or_,func, desc
from sqlalchemy.orm import joinedload, subqueryload

from db import session
from model import Teacher, Student, Subject, Group, Grade


def get_average_grade_1():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result
 

def max_average_grade_2():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subject_id==1).group_by(Student.id).order_by(desc('average_grade')).limit(1).all()
    return result

 

def average_grade_group_3():
    result = session.query(Subject.subject_name, Group.group_name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).join(Subject).filter(Subject.id==1).group_by(Subject.subject_name, Group.group_name).\
            order_by(desc('average_grade')).all()
    return result



def get_all_average_grade_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('all_average_grade')).all()
    return result


def get_subject_teacher_5():
    result = session.query(Teacher.fullname, Subject.subject_name)\
        .select_from(Teacher).join(Subject).filter(Teacher.id==1).group_by(Teacher.fullname, Subject.subject_name).all()
    return result


# def get_list_students_group_6():
#     result = session.query(Student.id, Student.fullname, Group.group_name) \
#         .select_from(Student).join(Group).filter(Group.id==1).all()
#     return result

def get_list_students_group_6():
    students = session.query(Student).join(Student.group).filter(Group.id==1).all()
    for s in students:
        columns = ["id", "fullname", "group_name"]
        r = [dict(
            zip(columns, (s.id, s.fullname, s.group.group_name)))]
        print(r)


def get_grade_students_group_7():
    result = session.query(Student.id, Student.fullname, Grade.grade) \
        .select_from(Student).join(Grade).join(Subject).join(Group) \
        .filter(and_(Group.id==3, Subject.id ==2)).group_by(Student.id,Student.fullname,Grade.grade).all()
    return result
   

def get_verage_grade_teachers_subject_8():
    result = session.query(Teacher.id, Teacher.fullname, Subject.subject_name, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Teacher).join(Subject).filter(Teacher.id==1).group_by(Subject.subject_name,Teacher.id, Teacher.fullname,).all()
    return result


def get_courses_student_9():
    result = session.query(Student.id, Student.fullname,Subject.subject_name)\
        .select_from(Grade).join(Subject).filter(Student.id==1).\
            group_by(Student.id, Subject.subject_name).all()
    return result


def get_subjects_student_by_teacher_10():
    result = session.query(Subject.subject_name, Teacher.fullname)\
        .select_from(Grade).join(Subject).join(Teacher).filter(Student.id==1).group_by(Subject.subject_name, Teacher.fullname,).all()
    return result

def get_average_grade_11():
    result = session.query(Student.fullname,func.round(func.avg(Grade.grade), 2).label('average_grade'),Teacher.fullname,)\
            .select_from(Grade).join(Subject).join(Teacher).filter(and_(Student.id==1,Teacher.id ==1))\
                .group_by(Student.id,Teacher.fullname).all()
    return result


def get_grade_students_subject_last_lesson_12():
    result = session.query(Grade.grade, Student.fullname,Grade.date_received,Group.group_name,Subject.subject_name)\
        .select_from(Grade).join(Student).join(Subject).join(Group).filter(and_(Student.id==33,Subject.id ==7)).\
            order_by(desc(Grade.date_received)).limit(1).all()
    return result




if __name__ == '__main__':
    print(get_average_grade_1())
    print(max_average_grade_2())
    print(average_grade_group_3())
    print(get_all_average_grade_4())
    print(get_subject_teacher_5())
    print(get_list_students_group_6())
    print(get_grade_students_group_7())
    print(get_verage_grade_teachers_subject_8())
    print(get_courses_student_9())
    print(get_subjects_student_by_teacher_10())
    print(get_average_grade_11())
    print(get_grade_students_subject_last_lesson_12())