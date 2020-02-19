import justpy as jp

def color_change(self, msg):
    self.d.style=f'color:{self.value}'
    self.d.text = f'The color of this text is: {self.value}'

def color_demo(request):
    wp = jp.WebPage()
    in1 = jp.Input(type='color', a=wp, input=color_change, debounce=30)
    in1.d = jp.Div(text='click box above to change color', a=wp)
    return wp

jp.justpy(color_demo)
