import justpy as jp

def num_changes(self, msg):
    msg.page.result_div.text = float(msg.page.in1.value) * float(msg.page.in2.value)


async def square_input(request):
    wp = jp.WebPage()
    wp.result_div = jp.Div(text='Result will show up here',classes='text-xl border m-2 p-2 w-1/3', a=wp)
    wp.in1 = jp.Input(type='number', a=wp, placeholder='First number', input=num_changes, value=0, classes=jp.Styles.input_classes)
    wp.in2 = jp.Input(type='number', a=wp, placeholder='Second number', input=num_changes, value=0, classes=jp.Styles.input_classes)
    return wp

jp.justpy(square_input)
