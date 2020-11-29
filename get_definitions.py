# This function takes in a base directory, list of student names, the function or class name, and returns a list of functions/classes corresponding to each student
def get_definitions(student_firstname_list, BASEDIR, definition_name):
    student_list = []
    for name in student_firstname_list:
        # Getting string from Python file
        with open(BASEDIR+ '/' + name + '.py') as f:
            f_contents = f.read()
        # Run python contents from this string with the local scope of this file
        exec(f_contents, globals()) # defines the function or class
        exec('function_or_class_obj = ' + definition_name, globals())
        student_list.append(function_or_class_obj)
    return student_list

# Test use case
if __name__ == '__main__':
    student_firstname_list = ['joao', 'hatice', 'nihir']
    BASEDIR = 'students_definitions'
    functions = get_definitions(student_firstname_list, BASEDIR, 'print_thing')
    functions[0]()


