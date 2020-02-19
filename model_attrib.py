import justpy as jp

async def input_demo(request):
    wp = jp.WebPage(data={'text':'', 'result':''})
    input_classes = "m-2 bg-gray-200 border-2"
    jp.Input(a=wp, classes=input_classes, placeholder='please type',
            model=[wp, 'text'])
    jp.Div(model=[wp, 'text'], a=wp)
    return wp

jp.justpy(input_demo)
    
