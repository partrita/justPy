import justpy as jp

async def square_input(request):
    wp = jp.WebPage(data={'result':''})
    result_div = jp.Div(text='Result will show up here',
                        classes=p_classes,
                        model=[wp,'result'])
    in1 = jp.Input(type='number', a=wp)
    in2 = jp.Input(type='number', a=wp)
    wp.data['result'] = in1*in2
    wp.add(reuslt_div)
    return wp

jp.justpy(square_input)
