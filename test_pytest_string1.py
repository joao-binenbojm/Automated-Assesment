import make_function as mf

path_code = 'students_block_code_string'  # change directory for every notebook
args_list = ['string1', 'string2']
# name = 'nihir'
name = 'hatice'
# name = 'joao'

func = mf.make_function(path_code, name, "string2 = 'xyz'", 'result', args_list)


def test_string_question_1():
    assert func('abc', 'xyz') == 'xyc abz'


def test_string_question_2():
    assert func('FUNNY', 'GAMES') == 'GANNY FUMES'
