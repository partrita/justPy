import justpy as jp

@jp.SetRoute('/')
def html_comps():
    wp = jp.WebPage()
    jp.Div(text='Text in italic', a=wp, classes='italic')
    jp.Div(text='Text in bold', a=wp, classes='font-bold')
    jp.Div(text='한글 입력',a=wp, classes='font-bold')
    return wp

@jp.SetRoute('/bye')
def bye_function():
    wp = jp.WebPage()
    wp.add(jp.P(text='Goodbye!', classes='text-5xl m-2'))
    return wp

def hello_function():
    wp = jp.WebPage()
    wp.add(jp.P(text='Hello there!', classes='text-5xl m-2'))
    return wp

jp.Route('/hello', hello_function)

jp.justpy()

