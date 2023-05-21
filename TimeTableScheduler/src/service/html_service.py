from datetime import date


class HTMLPage:
    """ A generic html page """

    header = '<!DOCTYPE html>' \
             '<html lang="en">' \
             '<head>' \
             '<style>' \
             'table, th, td {border: 1px solid black;border-collapse: collapse;} ' \
             'th, td {padding: 4px;}' \
             '</style>' \
             '<meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">' \
             '<meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title>' \
             '</head><body>'
    closing_header = '</body></html>'

    def __init__(self):
        self.elements = []

    def add(self, html_element):
        assert isinstance(html_element, str)

        self.elements.append(html_element)

    def generate_html(self):
        html = f'{self.header}'

        for element in self.elements:
            html += element

        html += self.closing_header

        assert isinstance(html, str)

        return html


class TimetablePage:
    """ A helper class to generate a generic timetable page """

    def __init__(self, title, headers: [], data: [], path):
        assert isinstance(title, str) and isinstance(headers, list) and isinstance(data, list) and isinstance(path, str)

        self.title = title
        self.date = date.today()
        self.headers = headers
        self.data = data
        self.cols = len(headers)
        self.path = path

    def generate_html(self):
        html_page = HTMLPage()

        full_table_data = [self.headers] + self.data

        html_page.add(f'<h1>{self.title}</h1>')
        html_page.add(f'<div><strong>Generated: {self.date.isoformat()}</strong></div><hr>')

        html_table = '<table>'
        for i in range(len(full_table_data)):
            row = full_table_data[i]
            html_table += '<tr>'

            row_cols = len(row)
            for col in row:
                span = 1 if row_cols == self.cols else self.cols

                if type(col) is list:
                    col = ', '.join(col)

                if i == 0:
                    html_table += f'<th colspan="{span}">{col}</th>'
                else:
                    html_table += f'<td colspan="{span}">{col}</td>'

            html_table += '</tr>'
        html_table += '</table>'

        html_page.add(html_table)

        html = html_page.generate_html()

        file = open(self.path, 'wt')
        file.write(html)
        file.close()

        return html
