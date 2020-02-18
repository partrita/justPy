import justpy as jp

def my_click(self, msg):
    self.text = 'I was clicked'
    print(msg.event_type)
    print(msg['event_type'])
    print(msg)

def event_demo():
    wp = jp.WebPage()
    wp.title='event demo'
    wp.favicon = './favicon.ico'
    d = jp.P(text='Not clicked yet', a=wp, classes='text-xl m-2 p-2 bg-blue-500 text-white')
    d.on('click', my_click)
    return wp

jp.justpy(event_demo)