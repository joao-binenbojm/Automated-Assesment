import os


def return_filenames(directory):

    # directory = os.fsencode('students_block_code')

    file_names = []

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".py"):
            # print(os.path.join(directory, filename))
            # print(filename)
            file_names.append(filename[:-3])
        else:
            continue

    return file_names
