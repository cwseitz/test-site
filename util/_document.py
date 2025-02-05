class HTMLDocument:

    """HTML Document class."""

    def __init__(self):

        self.style = ''
        self.head = ''
        self.body = ''
        self.title = ''


    def __str__(self):
        return (
            '<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '<meta charset="UTF-8">\n'
            f'<title>{self.title}</title>\n'
            f'<link rel="stylesheet" href="{self.style}">\n'
            f'{self.head}'
            '</head>\n'
            '<body>\n'
            f'{self.body}'
            '</body>\n'
            '</html>\n'
        )

    def add_script(self, path):
    	self.body += f"""<script type="text/javascript" src={path}></script>"""

    def add_content(self, content):
        self.body += content

    def add_header(self, header):

        self.body += f'<header class="header">{header}</header>'

    def add_text(self,
        text,
        size='16px',
        indent='0',
        align='left',
    ):
        """Add text paragraph."""
        self.body += (
            f'<p style="font-size:{size}; text-indent: {indent}; text-align: {align}">'
            f'{text}'
            '</p>\n'
        )

    def add_line_break(self) -> None:
        self.body += '<br>\n'

    def add_page_break(self) -> None:
        """Add page break."""
        self.body += '<p style="page-break-after: always;">&nbsp;</p>\n'

    def set_style(self, style):
        self.style = style

    def set_title(self, title):
        self.title = title

    def write(self, filepath):
        f = open(filepath, 'w+')
        f.write(str(self))
        f.close()
