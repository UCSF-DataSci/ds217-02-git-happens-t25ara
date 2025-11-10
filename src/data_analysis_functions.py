#TODO Separate Data Loading, Processing, and Saving into Different Function 
#TODO CSV Data using the same technique as the basic 
#TODO Calculate highest and lowest grades
#TODO Generate A More Comprehensive Report 
#Demonstrate Function Resuability and Modular Design 
path= 'data/students.csv'
import os
import datetime
# DATA LOADING FUNCTIONS

def load_students(file_path=path):
    """Load student data from CSV file."""
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return []

    # Read the file
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]
    if not lines:
        return []

    students = []
    # Skip the first line (header)
    for line in lines[1:]:
        parts = line.split(",")
        if len(parts) < 4:
            continue
        
        name = parts[0].strip()
        age_text = parts[1].strip()
        grade_text = parts[2].strip()
        subject = parts[3].strip()

        # Convert age to number
        try:
            age = int(age_text)
        except:
            age = 0
        
        # Convert grade to number
        try:
            grade = float(grade_text)
        except:
            grade = 0.0
        
        student = {
            "name": name,
            "age": age,
            "grade": grade,
            "subject": subject
        }
        students.append(student)
    
    return students


# PROCESSING FUNCTIONS

def calculate_average_grade(students):
    """Calculate average grade."""
    if not students:
        return 0.0
    
    total = 0.0
    count = 0
    for student in students:
        grade = student.get("grade")
        if grade and grade > 0:
            total += grade
            count += 1
    
    if count == 0:
        return 0.0
    return total / count


def calculate_average_age(students):
    """Calculate average age."""
    if not students:
        return 0.0
    
    total = 0
    count = 0
    for student in students:
        age = student.get("age")
        if age and age > 0:
            total += age
            count += 1
    
    if count == 0:
        return 0.0
    return total / count


def find_highest_grade(students):
    """Find the highest grade."""
    if not students:
        return 0.0
    
    highest = 0.0
    for student in students:
        grade = student.get("grade")
        if grade and grade > highest:
            highest = grade
    
    return highest


def find_lowest_grade(students):
    """Find the lowest grade."""
    if not students:
        return 0.0
    
    lowest = 100.0
    for student in students:
        grade = student.get("grade")
        if grade and grade > 0 and grade < lowest:
            lowest = grade
    
    return lowest


def count_math_students(students):
    """Count how many students are in Math."""
    count = 0
    for student in students:
        subject = student.get("subject", "").lower()
        if subject == "math":
            count += 1
    return count


def analyze_grade_distribution(students):
    """Count students in each grade range."""
    distribution = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0,
        'F (0-59)': 0
    }

    for student in students:
        grade = student.get("grade", 0)
        if grade >= 90:
            distribution['A (90-100)'] += 1
        elif grade >= 80:
            distribution['B (80-89)'] += 1
        elif grade >= 70:
            distribution['C (70-79)'] += 1
        elif grade >= 60:
            distribution['D (60-69)'] += 1
        else:
            distribution['F (0-59)'] += 1

    return distribution


def find_top_performers(students, min_grade=90):
    """Find students with grades above the minimum."""
    top_students = []
    for student in students:
        grade = student.get('grade', 0)
        if grade >= min_grade:
            top_students.append(student)
    return top_students


def count_students_by_subject(students):
    """Count how many students are in each subject."""
    subject_counts = {}
    for student in students:
        subject = student.get("subject", "Unknown")
        if subject in subject_counts:
            subject_counts[subject] += 1
        else:
            subject_counts[subject] = 1
    return subject_counts


# REPORT GENERATION FUNCTIONS

def generate_basic_report(students):
    """Generate a basic report."""
    total = len(students)
    avg_grade = calculate_average_grade(students)
    avg_age = calculate_average_age(students)
    math_count = count_math_students(students)
    highest = find_highest_grade(students)
    lowest = find_lowest_grade(students)

    # Find top students
    top_names = []
    for student in students:
        if student.get("grade") == highest:
            top_names.append(student["name"])

    # Count by subject
    subject_counts = count_students_by_subject(students)

    report = ""
    report += "Student Analysis Report\n"
    report += "=" * 30 + "\n"
    report += f"Total students: {total}\n"
    report += f"Average grade: {avg_grade:.1f}\n"
    report += f"Average age: {avg_age:.1f}\n"
    report += f"Highest grade: {highest:.1f}\n"
    report += f"Lowest grade: {lowest:.1f}\n"
    report += f"Grade range: {(highest - lowest):.1f}\n"
    
    if top_names:
        report += f"Top performers: {', '.join(top_names)}\n"
    else:
        report += "Top performers: N/A\n"
    
    report += f"Math students: {math_count}\n"
    report += "\n"
    report += "Students by subject:\n"
    
    subjects = sorted(subject_counts.keys())
    for subject in subjects:
        report += f"  {subject}: {subject_counts[subject]}\n"
    
    return report


def generate_comprehensive_report(students):
    """Generate a detailed comprehensive report."""
    if not students:
        return "No data to analyze"

    avg_grade = calculate_average_grade(students)
    highest = find_highest_grade(students)
    lowest = find_lowest_grade(students)
    distribution = analyze_grade_distribution(students)
    top_performers = find_top_performers(students, 90)
    subject_counts = count_students_by_subject(students)

    report = ""
    report += "COMPREHENSIVE STUDENT ANALYSIS REPORT\n"
    report += "=" * 50 + "\n"
    report += f"\nReport generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    # Basic Statistics
    report += "BASIC STATISTICS\n"
    report += "-" * 20 + "\n"
    report += f"Total students: {len(students)}\n"
    report += f"Average grade: {avg_grade:.1f}\n"
    report += f"Highest grade: {highest:.1f}\n"
    report += f"Lowest grade: {lowest:.1f}\n"
    report += f"Grade range: {(highest - lowest):.1f}\n\n"
    
    # Grade Distribution
    report += "GRADE DISTRIBUTION\n"
    report += "-" * 20 + "\n"
    for grade_range in distribution:
        count = distribution[grade_range]
        percent = (count / len(students)) * 100
        report += f"{grade_range}: {count} students ({percent:.1f}%)\n"
    
    # Subject Distribution
    report += "\nSTUDENTS BY SUBJECT\n"
    report += "-" * 20 + "\n"
    subjects = sorted(subject_counts.keys())
    for subject in subjects:
        report += f"{subject}: {subject_counts[subject]} students\n"
    
    # Top Performers
    report += "\nTOP PERFORMERS (90+)\n"
    report += "-" * 20 + "\n"
    if top_performers:
        for student in top_performers:
            report += f"{student['name']}: {student['grade']:.1f} ({student['subject']})\n"
    else:
        report += "No students scored 90 or above\n"
    
    # Individual Records
    report += "\nINDIVIDUAL STUDENT RECORDS\n"
    report += "-" * 30 + "\n"
    for student in students:
        report += f"Name: {student['name']}\n"
        report += f"  Age: {student['age']}\n"
        report += f"  Grade: {student['grade']:.1f}\n"
        report += f"  Subject: {student['subject']}\n\n"

    return report


# DATA SAVING FUNCTIONS

def save_report(report_text, filename):
    """Save report to a file."""
    # Create output folder if it doesn't exist
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    
    # Write report to file
    with open(filename, 'w') as f:
        f.write(report_text)
    
    print(f"Report saved to {filename}")




def main():
    """Main function to run the analysis."""
    print("=" * 50)
    print("STUDENT DATA ANALYSIS SYSTEM")
    print("=" * 50)
    
    # Load data
    print("\nLoading data...")
    students = load_students('data/students.csv')
    if not students:
        print("No data loaded. Check data/students.csv")
        return
    print(f"Loaded {len(students)} students")
    
    # Process data
    print("\nProcessing data...")
    avg_grade = calculate_average_grade(students)
    highest = find_highest_grade(students)
    lowest = find_lowest_grade(students)
    print(f"Average grade: {avg_grade:.1f}")
    print(f"Highest grade: {highest:.1f}")
    print(f"Lowest grade: {lowest:.1f}")
    
    # Generate reports
    print("\nGenerating reports...")
    
    basic_report = generate_basic_report(students)
    save_report(basic_report, 'output/basic_report.txt')
    
    comprehensive_report = generate_comprehensive_report(students)
    save_report(comprehensive_report, 'output/comprehensive_report.txt')
    
    
    print("\n" + "=" * 50)
    print("ANALYSIS COMPLETE!")
    print("=" * 50)
    print(f"Total students analyzed: {len(students)}")
    print(f"Reports generated: 2")
    print("Check the 'output' folder for reports.")



def load_data(path='data/students.csv'):
    """Load data from file."""
    return load_students(path)


def analyze_data(students):
    """Analyze student data and return results."""
    results = {
        'average_grade': calculate_average_grade(students),
        'average_age': calculate_average_age(students),
        'highest_grade': find_highest_grade(students),
        'lowest_grade': find_lowest_grade(students),
        'math_count': count_math_students(students),
    }
    return results


def save_results(results, output_file='output/analysis_report.txt'):
    """Save results to file."""
    report = "Analysis Results\n"
    report += "=" * 20 + "\n\n"
    for key in results:
        report += f"{key}: {results[key]}\n"
    
    save_report(report, output_file)
    return output_file

if __name__ == "__main__":
    main()