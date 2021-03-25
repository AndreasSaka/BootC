# -*- coding: utf-8 -*-
"""
@author: Andreas
"""
import datetime
import time 

course_t = ("C#","Java", "JavaScript", "Python")
duration = ("12 weeks", "24 weeks")
types = ("Full Time","Part Time")
prop = ("Courses", "Trainers", "Students", "Assignments")
courses = {}
trainers = []
students = []
assignments = {}

def courses_in(course_t,duration,types):
    '''
    This function requests user iput for courses.
    This function also perform input validation 
    and returns course_title, course_language, course_ds, course_type
    '''
 
    
    course_title = input("Enter a course title: ")
        
        
    while True:
        print(course_t)
        course_language = input("Enter a course language: ")
        if course_language in course_t:
            print("Valid course!")
            break
        else:
            print('Invalid course, try again!')
    
    while True:
        print(duration)
        course_dur = input("Enter a course duration: ")
        if course_dur == '12 weeks':
            course_ds = course_language + course_dur
            course_type = 'Part Time'
            break
        elif course_dur == '24 weeks':
            course_ds = course_language + course_dur
            course_type = 'Full Time'
            break
        else:
            print('That was an invalid duration!')
        

            
    return course_title, course_language, course_ds, course_type
 

def train_in(course_t):
    '''
    This function requests user iput for the trainers.
    This function also perform input validation 
    and returns tr_fname, tr_lname, tr_sub
    '''
    
    tr_fname = input("Provide the first name of the teacher: ")
    tr_lname = input("Provide the last name of the teacher: ")
        
    while True:
        tr_sub = input("Provide the teacher's subject: ")
        if tr_sub in course_t:
            print(f'The teacher will teach {tr_sub}.')
            break
        else:
            print(f'The teacher will not teach {tr_sub}, try again.')
           
    return tr_fname, tr_lname, tr_sub



def student_in():
    '''
    This function requests user iput for the students.
    This function also perform input validation 
    and returns st_fname, st_lname, st_tfees
    '''
    st_fname = input("Provide the first name of the student: ")
    st_lname = input("Provide the last name of the student: ")
    
    
    while True:
        birthday = time.strftime(input("Please enter birthday in Y-m-d format: "))
        try:
            datetime.datetime.strptime(birthday, '%Y-%m-%d').date()
            print('The birthday {} is valid.'.format(birthday))
            break
        except ValueError:
            print('The birthday {} is invalid'.format(birthday))
    
    st_tfees = int(input('Enter the student\'s tuition fees: '))
    
    return st_fname, st_lname, st_tfees




def assignments_in():
    '''
    This function requests user iput for the assignments.
    This function also perform input validation 
    and returns agm_title, agm_description, date_sub, mark_code, mark_oral
    '''
    agm_title = input("Provide the assignment tittle: ")
    agm_description = input("Provide the assignment description: ")
    
    while True:
        date_sub = time.strftime(input("Please enter submission date in Y-m-d format: "))
        try:
            datetime.datetime.strptime(date_sub, '%Y-%m-%d').date()
            print('The submission date {} is valid.'.format(date_sub))
            break
        except ValueError:
            print('The submission date {} is invalid'.format(date_sub))
            
    mark_code = int(input("Enter the mark for the submitted code: "))
    mark_oral = int(input("Enter the oral mark: "))
    
    return agm_title, agm_description, date_sub, mark_code, mark_oral


def how_many(wt):
    '''
    Parameters
    ----------
    wt : string
        The input is one from the potential choices
        'Courses', 'Trainers', 'Students', 'Assignments'.

    Returns
    -------
    entries : int
        The output is the number of entries that the user will enter.

    '''
    entries = int(input('How many entries do you wish to enter?: '))
    print(f'You are going to enter {entries} {wt}')
    return entries

def what_en(prop):
    '''
    

    Parameters
    ----------
    prop : a tuple
        The tuple with the potential choices
        'Courses', 'Trainers', 'Students', 'Assignments'..

    Returns
    -------
    wt : string
        The input is one from the potential choices
        'Courses', 'Trainers', 'Students', 'Assignments'.

    '''
    print(prop)    
    while True:
        wt = input('What do you wish to enter from the available? ')
        if wt in prop:
            print(f'{wt} is in the choices!')
            break
        else:
            print(f'{wt} is not a valid choice.')
           
    return wt

def check_answ():
    '''
    Function that requires answer to check from the user

    Returns
    -------
    answ : string
        A yes/ no string.

    '''
    answ = input('Do you wish to enter more entries type yes/no: ')
    return answ
        
    
def storage(courses, trainers, students, assignments, entries, wt):
    '''
    Parameters
    ----------
    courses : dictionary
        Empty dictionary .
    trainers : list
        Empty list.
    students : list
        Empty dictionary.
    assignments : dictionary
        Empty dictionary.

    Returns
    -------
    courses : dictionary
        a dictionary with the courses entries .
    trainers : list
        a list with the trainers entries.
    students : list
        a list with the students entries.
    assignments : dictionary
        a dictionary with the assignments entries.

    '''

    
    for i in range(entries):
        if wt == 'Courses':
            course_title, course_language, course_ds, course_type = courses_in(course_t,duration,types)
            temp = [course_language, course_ds, course_type]
            courses[course_title] = temp
        elif wt == 'Trainers':
            tr_fname, tr_lname, tr_sub = train_in(course_t)
            temp2 = [tr_fname, tr_lname, tr_sub]
            trainers.append(temp2)
        elif wt == 'Students':
            st_fname, st_lname, st_tfees = student_in()
            temp3 = [st_fname, st_lname, st_tfees]
            students.append(temp3)
        elif wt == 'Assignments':
            agm_title, agm_description, date_sub, mark_code, mark_oral = assignments_in()
            temp4 = [agm_description, date_sub, mark_code, mark_oral]
            assignments[agm_title] = temp4
    
    return courses, trainers, students, assignments


if __name__ == '__main__':
    
    wt = what_en(prop)
    entries = how_many(wt)
    courses, trainers, students, assignments = storage(courses, trainers, students, assignments, entries, wt)
    answ = check_answ()
    while answ != 'no':
        wt = what_en(prop)
        entries = how_many(wt)
        courses, trainers, students, assignments = storage(courses, trainers, students, assignments, entries, wt)
        answ = check_answ()
    
    print(courses)
    print(trainers)
    print(students)
    print(assignments)

    
    
    

    
        
        