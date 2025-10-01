#!/bin/bash

echo "making directory src"
mkdir -p src
echo "making directory data"
mkdir -p data
echo "making directory output"
mkdir -p output

cat > src/data_analysis.py<< 'EOF'
#TODO Read CSV 

#TODO Split Each Line by Commas to Extract Fields

#TODO Calculate Basic Statistics 

#TODO Write Results to Output

EOF

cat > src/data_analysis_functions.py<< 'EOF'
#TODO Separate Data Loading, Processing, and Saving into Different Function 

#TODO CSV Data using the same technique as the basic 

#TODO Calculate highest and lowest grades

#TODO Generate A More Comprehensive Report 

#Demonstrate Function Resuability and Modular Design 
EOF

cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,85,Math
Bob,19,92,Science
Charlie,21,78,English
Diana,20,88,Math
Eve,22,95,Science
Frank,19,82,History
Grace,21,91,Math
Henry,20,76,Science
EOF

echo "print student data"
cat data/students.csv 
 
cat > .gitignore << 'EOF'
EOF

echo "made .gitignore file"


chmod +x setup_project.sh
