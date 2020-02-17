import justpy as jp

class MyToolbar(jp.QToolBar):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        c1 = self
        c1.classes = 'bg-grey-3'
        c2 = jp.QBtn(flat=True, round=True, dense=True, a=c1)
        c3 = jp.QIcon(name='menu', a=c2)
        c4 = jp.QMenu(a=c2)
        c5 = jp.QList(style='min-width: 100px', a=c4)
        c6 = jp.QItem(clickable=True, v_close_popup=True, a=c5)
        c7 = jp.QItemSection(a=c6)
        c8 = jp.A(href='/about', style='text-decoration: none', a=c7, text='about')
        c9 = jp.QSeparator(a=c5)
        c10 = jp.QItem(clickable=True, v_close_popup=True, a=c5)
        c11 = jp.QItemSection(a=c10)
        c12 = jp.A(href='/tool', style='text-decoration: none', a=c11, text='help')
        c13 = jp.QToolBarTitle(a=c1, text='Toolbar')
        c14 = jp.QBtn(flat=True, round=True, dense=True, a=c1)
        c15 = jp.QIcon(name='more_vert', a=c14)


@jp.SetRoute('/')
def index():
    wp = jp.QuasarPage()
    wp.tailwind = True
    wp.add(MyToolbar())
    wp.add(jp.P(text='Index page', classes='text-5xl m-2'))
    return wp

@jp.SetRoute('/about')
def about():
    wp = jp.QuasarPage()
    wp.tailwind = True
    wp.add(MyToolbar())
    wp.add(jp.P(text='Hello there!', classes='text-5xl m-2'))
    return wp

jp.justpy()
