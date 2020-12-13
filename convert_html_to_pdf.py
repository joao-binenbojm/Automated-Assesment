import pdfkit


def convert_html_to_pdf(path, html_file, pdf_file):
    # path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
    path_wkhtmltopdf = path
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # pdfkit.from_file('hatice.html', 'hatice-converted.pdf', configuration=config)
    pdfkit.from_file(html_file, pdf_file, configuration=config)


# convert_html_to_pdf('C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe', 'hatice.html', 'hatice-converted.pdf')