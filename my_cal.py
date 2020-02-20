import justpy as jp

def num_changes(self, msg):
    msg.page.data['result'] = float(msg.page.in1.value) * float(msg.page.in2.value)


async def square_input(request):
    wp = jp.WebPage(data={'result': 'Result will show up here'})
    result_div = jp.Div(classes='text-xl border m-2 p-2 w-1/3', model=[wp,'result'], a=wp)
    wp.in1 = jp.Input(type='number', a=wp, placeholder='First number', input=num_changes, value=0, classes=jp.Styles.input_classes)
    wp.in2 = jp.Input(type='number', a=wp, placeholder='Second number', input=num_changes, value=0, classes=jp.Styles.input_classes)
    return wp

jp.justpy(square_input)
