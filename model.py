from sqlalchemy import Column, Integer, String, Date, ForeignKey, CheckConstraint, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()


    
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    subjects = relationship("Subject", back_populates="teacher")
 
    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(50))
    subject_description = Column(String(100))
    teacher_id = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))
    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    date_of_birth = Column(Date)
    gender = Column(String(10), CheckConstraint("gender IN ('Male', 'Female')"))
    group_id = Column(Integer, ForeignKey('student_groups.id',ondelete='CASCADE', onupdate='CASCADE'))
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")
    
    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name

    
class Group(Base):
    __tablename__ = 'student_groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(50))
    description = Column(String)
    students = relationship("Student", back_populates="group")

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Integer, CheckConstraint('grade > 0 AND grade <= 10'))
    date_received = Column(Date)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='SET NULL', onupdate='CASCADE'))
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='SET NULL', onupdate='CASCADE'))
    student = relationship("Student", back_populates="grades")
    subject  = relationship("Subject", back_populates="grades")
    
