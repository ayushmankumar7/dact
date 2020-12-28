class Html_Templates():
    def __init__(self):
        self.index_html = '''
         {%load static%}
        <html lang="en">
            <body>
                <div id="root"></div>
            </body>
            <script src = "{% static '/dist/app.bundle.js' %}"></script>
        </html>
        '''.strip()
        self.dact_svg = '''
        '''