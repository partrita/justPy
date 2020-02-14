import justpy as jp

def hello_world():
    wp = jp.WebPage()
    for i in range(1,11):
        jp.P(
                text=f'{i}) Hello world!',
                a =wp, style=f'font-size: {10*i}px')
    return wp

jp.justpy(hello_world)
