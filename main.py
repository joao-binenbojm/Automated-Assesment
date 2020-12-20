import subprocess
import os
import pandas as pd
from utils import convert_html_to_pdf as conv

# Script with which teacher will interact with to generate feedback/carry out assessments
# Has added functionality of adding it to the appropriate directory

# names = ['joao', 'hatice', 'nihir']
names = pd.read_csv('names.csv').iloc[:, 0]
# BASEDIR = '/Users/joaobinenbojm/Desktop/Automated-Assesment'
# 20.12.2020 - HTC - change directory
BASEDIR = 'C:/Users/ahmet/Desktop/AI-Core-Testing/Joao-Version-4/Automated-Assesment'
# 20.12.2020 - HTC - pdf library configuration file
conf_path = '{}/config_files/wkhtmltopdf/bin/wkhtmltopdf.exe'.format(BASEDIR)

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
    os.rename(BASEDIR + '/' + name + '.html', BASEDIR + '/' + 'reports' '/' + name + '.html', )
    # 20.12.2020 - HTC - convert html reports to pdf
    conv.convert_html_to_pdf(conf_path, '{}/reports/{}.html'.format(BASEDIR, name),
                             '{}/reports/{}.pdf'.format(BASEDIR, name))
