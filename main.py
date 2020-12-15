import subprocess
import os
import pandas as pd

# Script with which teacher will interact with to generate feedback/carry out assessments
# Has added functionality of adding it to the appropriate directory

# names = ['joao', 'hatice', 'nihir']
names = pd.read_csv('names.csv').iloc[:, 0]
BASEDIR = '/Users/joaobinenbojm/Desktop/Automated-Assesment'

# Removing any old reports in the reports directory
subprocess.call(['rm', '-rf', BASEDIR + '/reports'])
subprocess.Popen("mkdir reports", shell=True)

# Adds current student's name to the file to be read by unit test
for name in names:
    with open('current_student.txt', 'w') as f:
        f.write(name)
    subprocess.run(['pytest'])
    subprocess.run(['pytest', '--html={}.html'.format(name), '--self-contained-html'])
    # Moving to appropriate directory
    os.rename(BASEDIR + '/' + name + '.html', BASEDIR + '/' + 'reports' '/'+ name + '.html', )