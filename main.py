import subprocess

# Script with which teacher will interact with to generate feedback/carry out assessments

names = ['joao', 'hatice', 'nihir']

# adds current student's name to the file to be read by unit test
for name in names:
    with open('current_student.txt', 'w') as f:
        f.write(name)
    subprocess.run(['pytest'])
    subprocess.run(['pytest', '--html={}.html'.format(name), '--self-contained-html'])