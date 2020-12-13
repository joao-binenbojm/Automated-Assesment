# This function will take in a string or a list and write it out to an existing or non-existing text file

def writeout(output, challenge_name, path, name, write_type='a'):
    # Appending to the existing file. The 'a' allows us to add feedback to multiple challenges at once
    with open(path + name + '.txt', write_type) as f:
        f.write(challenge_name + ':\n')
        f.write(output)
        f.write('\n\n')

# Test use case
if __name__ == '__main__':
    student_name_list = ['joao', 'nihir', 'hatice']
    path = 'students_feedback/'

    # First example challenge and feedback
    challenge_name = 'Hangman Challenge'
    outputs = ['Error: blablablabla', 'Failed the use case blabla', 'All tests passed']
    for output, name in zip(outputs, student_name_list):
        writeout(output, challenge_name, path, name, write_type='w') # use w for first challenge to clear any other text that may be in the file
    # Second example challenge and feedback
    challenge_name = 'Math Challenge'
    outputs = ['Error: blablablabla', 'Failed the use case blabla', 'All tests passed']
    for output, name in zip(outputs, student_name_list):
        writeout(output, challenge_name, path, name)