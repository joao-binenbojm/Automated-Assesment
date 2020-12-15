from utils.object_import import object_import

path_code = 'submissions/defs'  # change directory for every notebook
def_name = 'return_thing'

with open('current_student.txt', 'r') as f:
    name = f.read()

# Get function from the given student's submission
func = object_import(name, [def_name])[0]

with open('current_student.txt', 'r') as f:
    name = f.read()

def test_string_question_1():
    assert isinstance(func(), str)


def test_string_question_2():
    assert func() == 'something'
