# This function will run a given .py script and make its inner contents the contents of a function
def make_function(path, name, last_line, return_name, args_list): # takes in the path where file is located, student name, and the arguments required for the given function
    with open(path + '/' + name + '.py', 'r') as f:
        f_contents = f.read()  # get whole code as string
    contents = f_contents.split('\n')
    exclude_index = contents.index(last_line) # find where to cut part of code to be put in function
    contents = ['\t' + content for content in contents]
    contents = '\n'.join(contents[exclude_index+1:])
    # defining our function
    executable_string = "def func({}):\n{}\n\t{}".format(', '.join(args_list), contents, 'return '+return_name)
    exec(executable_string, globals())
    return func


if __name__ == '__main__':
    path = 'students_block_code'
    name = 'joao'
    args_list = ['annual_salary', 'portion_saved', 'total_cost', 'down_payment', 'r = 0.04']
    function = make_function(path, name, 'r = 0.04', 'n_months', args_list)
    print(function(80000, 0.15, 500000, 125000))