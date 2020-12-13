import os
import convert_html_to_pdf as cnv

student_name = 'hatice'
cmd = 'pytest --html={name}.html'.format(name=student_name)

# run the pytest command and generate report
os.system(cmd)

# convert generated html report to pdf file
file_name = '{name}.html'.format(name=student_name)
pdf_name = '{name}-converted.pdf'.format(name=student_name)
path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'

cnv.convert_html_to_pdf(path, file_name, pdf_name)
