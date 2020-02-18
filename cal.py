from justpy import Div, Input, Button, WebPage, justpy

input_classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
p_classes = 'm-2 p-2 h-32 text-xl border-2'

async def my_input(self, msg):
    self.div.text = self.value

async def input_demo(request):
    wp = jp.WebPage()
    in1 = jp.Input(type='number', a=wp, classes=input_classes, placeholder='Please type here')
    in2 = jp.Input(type='number', a=wp, classes=input_classes, placeholder='Please type here')
    in1.div = jp.Div(text='What you type will show up here', classes=p_classes, a=wp)
    in1.on('input', my_input)
    return wp

class Calculator(Div):

    btn_classes = 'w-1/4 text-xl font-bold p-2 m-1 border bg-gray-200 hover:bg-gray-700 shadow'
    layout_text = ['value_1','value_2']

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.value = 0
        self.tape = Input(classes='block p-2 m-2  border text-right text-sm bg-gray-200', a=self, readonly=True, value=' ', style='width: 90%')
        self.result = Input(classes='block p-2 m-2 border text-2xl text-right', a=self, readonly=True, value='0', style='width: 90%')
        for line in self.__class__.layout_text:
            d = Input(classes='flex w-auto m-2', a=self)
            for b in line:
                b1 = Button(text=b, a=d, classes=self.__class__.btn_classes, click=self.calculator_click)
                b1.calc = self


jp.justpy(input_demo)