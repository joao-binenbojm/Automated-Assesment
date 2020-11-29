import make_function as mf
import loop_over_files as loop
import write_feeback as fb

path_code = 'students_block_code'
path_fb = 'students_feedback/'
args_list = ['annual_salary', 'portion_saved', 'total_cost', 'down_payment', 'r = 0.04']
files_list = loop.return_filenames(path_code)

for names in files_list:
    func = mf.make_function(path_code, names, 'r = 0.04', 'n_months', args_list)

    print(f'Test results for {names} is shown below:')

    # TEST CASE 1
    test_1 = func(80000, 0.15, 500000, 125000)
    if test_1 == 105:
        print(f'{names} passed test_1')
        output = f'{names} passed test_1'
    else:
        print(f'{names} failed test_1')
        output = f'{names} failed test_1'

    # write test 1 feedback
    fb.writeout(output, 'Branching-Test 1', path_fb, names)

    # TEST CASE 2
    test_2 = func(120000, 0.10, 1000000, 1000000*0.25)
    if test_2 == 183:
        print(f'{names} passed test_2')
        output = f'{names} passed test_2'
    else:
        print(f'{names} failed test_2')
        output = f'{names} failed test_2'

    # write test 2 feedback
    fb.writeout(output, 'Branching-Test 2', path_fb, names)
