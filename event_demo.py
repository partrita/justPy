import justpy as jp

def my_click(self, msg):
    self.text = 'I was clicked'
    self.set_class('bg-blue-500')
    print(msg.event_type)
    print(msg['event_type'])
    print(msg)

def my_mouseenter(self, msg):
    self.text = 'Mouse entered'
    self.set_class('bg-red-500')

def my_mouseleave(self, msg):
    self.text = 'Mouse left'
    self.set_class('bg-teal-500')

def event_demo():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet',
               a=wp, classes='rounded-full bg-blue-500 text-white h-32 w-32 flex items-center justify-center',
               click = my_click, mouseenter=my_mouseenter, mouseleave= my_mouseleave)
    d.on('click', my_click)
    return wp

jp.justpy(event_demo)
