import sys
import io
import importlib

# This function takes in a base directory, list of student names, and return what each of the corresponding .py files print to console
def get_printed(student_firstname_list, BASEDIR):
    student_output_list = []
    for name in student_firstname_list:
        old_stdout = sys.stdout  #Memorize the default stdout stream
        sys.stdout = buffer = io.StringIO()

        importlib.import_module(BASEDIR + '.' + name, package=None)

        sys.stdout = old_stdout

        student_output_list.append(buffer.getvalue()[:-1]) # returns string containing the entire components of the buffer
    return student_output_list

# Test use case
if __name__ == '__main__':
    student_firstname_list = ['joao', 'hatice', 'nihir']
    BASEDIR = 'students_print'
    outputs = get_printed(student_firstname_list, BASEDIR)
    print(outputs)


