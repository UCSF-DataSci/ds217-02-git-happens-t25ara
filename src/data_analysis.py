#!/usr/bin/env python3
#Read the CSV file line by line using open() and readlines()
#Split each line by commas to extract fields
#Calculate basic statistics (total students, average grade)
#Count students by subject
#Write results to output/analysis_report.txt
#Use f-strings with .1f formatting for decimal numbers

with open("/Users/tara/Documents/UCSF/DATASCI_217/ds217-02-git-happens-t25ara/data/students.csv") as f:
 text = f.readlines()
 

column_names = text[1:] #skip the header

students = [] #store info in list of dictionaries 

for line in column_names:
 name, age, grade, subject = line.strip().split(",'")
 parts = line.strip().split(",")
 students.append({
  "name":name, 
  "age": int(age),
  "grade": float(grade),
  "subject": subject
 })

#calculate stats 
total = 0
for s in students:
    total += s['grade']

average_grade = total / len(students)
