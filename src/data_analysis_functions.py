#!/usr/bin/env python3
"""
Student Data Analysis
"""
import os

path = "data/students.csv"

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


# DATA PROCESSING FUNCTIONS

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


def analyze_grade_distribution(grades):
    """Count grades by letter grade ranges."""
    distribution = {
        'A (90-100)': 0,
        'B (80-89)': 0,
        'C (70-79)': 0,
        'D (60-69)': 0,
        'F (0-59)': 0
    }

    for grade in grades:
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


def analyze_data(students):
    """Return dictionary with multiple stats: highest, lowest, grade distribution."""
    if not students:
        return {}
    
    # Get all grades from students
    grades = []
    for student in students:
        grade = student.get("grade", 0)
        if grade > 0:
            grades.append(grade)
    
    # Calculate statistics
    highest = find_highest_grade(students)
    lowest = find_lowest_grade(students)
    distribution = analyze_grade_distribution(grades)
    
    # Calculate average
    total = 0.0
    for grade in grades:
        total += grade
    average = total / len(grades) if grades else 0.0
    
    results = {
        'highest_grade': highest,
        'lowest_grade': lowest,
        'average_grade': average,
        'grade_distribution': distribution,
        'total_students': len(students)
    }
    
    return results


# REPORT GENERATION FUNCTIONS (REMOVED - NOT NEEDED)


# DATA SAVING FUNCTIONS

def save_results(results, filename):
    """Write and save results to a file."""
    # Create output folder if it doesn't exist
    folder = os.path.dirname(filename)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    
    # Write results to file
    with open(filename, 'w') as f:
        f.write("Analysis Results\n")
        f.write("=" * 30 + "\n\n")
        
        # Write each result
        for key in results:
            if key == 'grade_distribution':
                f.write("Grade Distribution:\n")
                distribution = results[key]
                for grade_range in distribution:
                    f.write(f"  {grade_range}: {distribution[grade_range]}\n")
            else:
                f.write(f"{key}: {results[key]}\n")
    
    print(f"Results saved to {filename}")


# MAIN PROGRAM

def main():
    """Main function to run the analysis."""
    print("=" * 50)
    print("STUDENT DATA ANALYSIS")
    print("=" * 50)
    
    # Step 1: Load the data
    print("\n[Step 1] Loading data from CSV...")
    students = load_students('data/students.csv')
    
    if not students:
        print("Error: No data loaded. Check data/students.csv")
        return
    
    print(f"Success! Loaded {len(students)} students")
    
    # Step 2: Analyze the data
    print("\n[Step 2] Analyzing student data...")
    results = analyze_data(students)
    
    print(f"Highest grade: {results['highest_grade']:.1f}")
    print(f"Lowest grade: {results['lowest_grade']:.1f}")
    print(f"Average grade: {results['average_grade']:.1f}")
    
    print("\nGrade Distribution:")
    for grade_range in results['grade_distribution']:
        count = results['grade_distribution'][grade_range]
        print(f"  {grade_range}: {count} students")
    
    # Step 3: Save the results
    print("\n[Step 3] Saving results to file...")
    save_results(results, 'output/analysis_results.txt')
    
    print("\n" + "=" * 50)
    print("ANALYSIS COMPLETE!")
    print("=" * 50)


# Helper functions for testing

def load_data(path='data/students.csv'):
    """Load data from file."""
    return load_students(path)


if __name__ == "__main__":
    main()