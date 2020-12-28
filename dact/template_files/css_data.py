class Css_Templates():
    def __init__(self):
        self.index_css = ''' '''
        self.app_css = '''
.App
{
    text-align: center;
    color:black;
}
.Applogo
{
    max-width: 100%;
    height: 50%;
    width: 90%; 
}
.Apptext
{
    font-family: sans-serif;
    color:#169A9A;
}
        '''.strip()
    def get_initial_css_files(self):
        x = {
            'index.css':self.index_css,
            'App.css':self.app_css,
        }
        return x