#!/bin/bash

echo "making directory src"
mkdir -p src
echo "making directory data"
mkdir -p data
echo "making directory output"
mkdir -p output

cat > src/data_analysis.py<< 'EOF'
EOF

cat > src/data_analysis_functions.py<< 'EOF'
EOF

cat > data/students.csv << 'EOF'
name, age, grade, subject
Bob, 12, 1, history
Jerry, 15, 9, english
Annie, 13, 5, biology
Tom, 17, 11, history
Jim, 18, 12, spanish
Tara, 15, 8, spanish
Kate, 16, 10, english
Sara, 14, 9, biology
EOF

echo "print student data"
cat data/students.csv 
 
cat > .gitignore << 'EOF'
EOF

echo "made .gitignore file"


chmod +x setup_project.sh
