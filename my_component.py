import justpy as jp

class InputWithDiv(jp.Div):
    @staticmethod
    def input_handler(self, msg):
        self.div.text = self.value

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.in1 = jp.Input(a=self, placeholder='type me',
                input = self.input_handler)
        self.in2 = jp.Input(a=self, placeholder='type me2',
                input = self.input_handler)
        self.in2.div = jp.Div(text='What do you type?', a=self)


def input_demo(request):
    wp = jp.WebPage()
    InputWithDiv(a=wp)
    return wp

jp.justpy(input_demo)
