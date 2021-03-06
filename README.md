# Automated-Assesment
Repo where we develop methods for automated assessment of code challenges for our courses. HTML reports will soon be easily converted to PDFs and the generated report formats will become more informative, concise, and easy to follow for students.

# Contents:
- How to use
- Structural description


## How to use: basic instructions
- Write a CSV file named 'names.csv' containing the names/unique identifiers of each student in one column, and add that to the Automated-Assessment directory
- Make a directory for each challenge to be assessed per student in the **submissions** directory, and place student's .py submissions in their respective directories (e.g. place joao.py containing the answer to challenge1 in submission/challenge1)
- Ensure that all pytest test files are in the Automated-Assesment directory
- Run the main.py file
- Generated reports are stored in the reports directory

## Structural description

assets: directory automatically generated by pytest-html, used to style the html reports generated

old: directory containing old files and attempts of test automation, don't worry about this one

reports: directory where generated reports for each of the students are stored

submissions: directory where instructors must place all student submissions (.py) files. For this directory, we create a subdirectory for each challenge/submission to be assesed per student

utils: directory where helper functions developed are stord. Don't worry about these for now as they are under development!

current_student.txt: As most of this code works by interacting with the command line, we use this file as an itermediary (main.py adds the student's name to the file, the unit test reads the name from the file to know which student's file to test)

**main.py**: The only .py file that needs to be explicitly run by the instructor!

names.csv: File to be added to the main workspace by instructor, containing the names of all students (ideally unique identifiers). These 'names' should correspond to the .py file submissions and will be used to name the generated reports. (e.g. name='joao' --> searches for joao.py --> generates joao.html)

test_pytest_defs.py: Simple demo unit test for different functions

test.pytest_string.py: Simple demo unit test for a small block of code
