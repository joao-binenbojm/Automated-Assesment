import utils.make_function as mf

# path_code = '/Users/joaobinenbojm/Desktop/Automated-Assesment/submissions/block'
# 20.12.2020 - HTC - change directory
path_code = 'C:/Users/ahmet/Desktop/AI-Core-Testing/Joao-Version-4/Automated-Assesment/submissions/block'

args_list = ['string1', 'string2']

with open('current_student.txt', 'r') as f:
    name = f.read()

func = mf.make_function(path_code, name, "string2 = 'xyz'", 'result', args_list)

def test_string_question_1():
    assert func('abc', 'xyz') == 'xyc abz'


def test_string_question_2():
    assert func('FUNNY', 'GAMES') == 'GANNY FUMES'
