

class HTMLDocument:
    """HTML Document class."""

    def __init__(self):

        self.style = ''
        self.head = ''
        self.body = ''
        self.title = self.__class__.__name__

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
            '<div class="container">'
            f'{self.body}'
            '</div>'
            '</body>\n'
            '</html>\n'
        )

    def add_mathjax(self):

        self.body += """<script>
                  MathJax = {
                    tex: {
                      inlineMath: [['$', '$'], ['\\(', '\\)']],
                      displayMath: [['$$','$$'], ['\\[', '\\]']],
                      processEscapes: true,
                      processEnvironments: true
                    },
                    options: {
                      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
                    }
                  };

                  window.addEventListener('load', (event) => {
                      document.querySelectorAll("mjx-container").forEach(function(x){
                        x.parentElement.classList += 'has-jax'})
                    });

                </script>"""

    def add_scripts(self):
        self.body += """<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
                        <script type="text/javascript" id="MathJax-script" async
                        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
                        <script type="text/javascript" src="assets/main.js"></script>"""



    def add_header(self, header, level='h2', align='left'):

        self.body += (
            f'{header}'
        )

    def add_content(self, content):
        self.body += content

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
        with open(filepath, 'w') as f:
            f.write(str(self))
