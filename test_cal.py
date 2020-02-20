import justpy as jp

class Calculator(jp.Div):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.value = 0
        self.tape = jp.Input(classes='block p-2 m-2  border text-right text-sm bg-gray-200',
                             a=self, readonly=True, value=' ', style='width: 90%')
        self.result = jp.Input(classes='block p-2 m-2 border text-2xl text-right',
                               a=self, readonly=True, value='0',
                               style='width: 90%')
        d = jp.Div(classes='flex w-auto m-2', a=self)    
        b = jp.Input(text='type', a=d)
        b1 = jp.Button(text='cal!', a=d,
                    click=self.cal_click)
        b1.calc = self

    @staticmethod
    def cal_click(self, msg):
        calc = self.calc
        calc.tape.value += self.text
        calc.result.value = str(eval(calc.tape.value)*2)
        
    


def calculator_test():
    wp = jp.WebPage()
    c = Calculator(a=wp, classes='m-1 border inline-block', style='width: 250px')
    return wp

jp.justpy(calculator_test)
