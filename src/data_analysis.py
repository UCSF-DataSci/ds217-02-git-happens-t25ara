#!/usr/bin/env python3

def load_students(filename):
  students = []
  #open file 
  with open(filename) as f:
    lines = f.readlines()[1:]
    for line in lines:
        name, age, grade, subject = line.strip().split(",")
        students.append({
            "name": name, 
            "age": int(age),
            "grade": float(grade),
            "subject":subject
        })
  return students


def count_average_grade(grades):
    if not grades:
        return 0 
    return sum(grades)/len(grades)

def count_math_students(students):
    n_math_students = 0 
    for student in students:
        if student['subject'].strip().lower() == "math":
            n_math_students = n_math_students + 1 
    return(n_math_students)

def generate_report(students, grades, average, math_students):
    print("____REPORT_____")
    print("Student Data \n", students)
    print("Grades\n", grades)
    print(f"Average Grade:\n {average:.1f}")
    print("Number of Math Students\n", math_students)
    report = (f"____REPORT_____\nAverage Grade:{average:.1f}\nNumber of Math Students:\n{math_students}")
    return(report)


def save_report(report, filename):
    with open(filename, 'w') as file:
        file.write(str(report))  # write the string directly
    print(f"report saved")
    

def main(myfile):
    students = load_students(myfile)
    grades = [student['grade'] for student in students]
    average = count_average_grade(grades)
    math_students = count_math_students(students)
    filename = "student_analysis.txt"
    report = generate_report(students, grades, average, math_students)
    save_report(report, "output/analysis_report.txt")
    print("analysis complete results saved to analysis_report.txt")

myfile = "/Users/tara/Documents/UCSF/DATASCI_217/ds217-02-git-happens-t25ara-1/data/students.csv"
main(myfile)
