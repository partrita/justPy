import justpy as jp

input_classes = "m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 py-2 px-4 text-gray-700 focus:outline-none focus:bg-white focus:border-purple-500"
p_classes = 'm-2 p-2 h-32 text-xl border-2'

async def my_input(self, msg):
    self.div.text = self.value

async def input_demo(request):
    wp = jp.WebPage()
    wp.title='input demo'
    wp.favicon='./favicon.ico'
    wp.debug=True
    in2 = jp.Input(a=wp, classes=input_classes, placeholder='Please type here')
    in2.div = jp.Div(text='What you type will show, 입력하는 것이 보여집니다.', classes=p_classes, a=wp)
    in2.on('input', my_input)
    return wp

jp.justpy(input_demo)
