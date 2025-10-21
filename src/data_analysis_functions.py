#!/usr/bin/env python3
#Data Loading CSV Function 
def load_data(filename):
    if not filename.endswith(".csv"):
        print("you did not enter a csv")
        raise ValueError("incorrect file extension")

def load_csv(filename):
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
#Data Analyzing Function: highest lowest grade; grade distribution
def analyze_data(students): #return dictionary with with multiple stats ^^
    pass

def analyze_grade_distribution(grades):#count grades by letter grade ranges 
    pass
#Write and Save Function 
def save_results(results, filename):
    pass

def main():
    pass 
