class HTML:
    def __init__(self):
        self.code = ""

    def get_code(self):
        return self.code

    def body(self):
        self.code += "<body>"
        yield
        self.code += "</body>"

    def div(self):
        self.code += "<div>"
        yield
        self.code += "</div>"

    def p(self, text):
        self.code += f"<p>{text}</p>"


html = HTML()

with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

print(html.get_code())
