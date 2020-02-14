import justpy as jp

def hello_world():
        wp = jp.WebPage()
        p = jp.P(text='Hello World!', a=wp)
        return wp

jp.justpy(hello_world)
