import make_function as mf
import loop_over_files as loop
import write_feeback as fb

path_code = 'students_block_code_string'  # change directory for every notebook
path_fb = 'students_feedback/'
args_list = ['string1', 'string2']
files_list = loop.return_filenames(path_code)

for names in files_list:
    func = mf.make_function(path_code, names, "string2 = 'xyz'", 'result', args_list)

    print(f'Test results for {names} is shown below:')

    # TEST CASE 1
    test_1 = func('abc', 'xyz')
    if test_1 == 'xyc abz':
        print(f'{names} passed test_1')
        output = f'{names} passed test_1'
    else:
        print(f'{names} failed test_1')
        output = f'{names} failed test_1'

    # write test 1 feedback
    fb.writeout(output, 'String Manipulation-Test 1', path_fb, names)

    # TEST CASE 2
    test_2 = func('FUNNY', 'GAMES')
    if test_2 == 'GANNY FUMES':
        print(f'{names} passed test_2')
        output = f'{names} passed test_2'
    else:
        print(f'{names} failed test_2')
        output = f'{names} failed test_2'

    # write test 2 feedback
    fb.writeout(output, 'String Manipulation-Test 2', path_fb, names)
