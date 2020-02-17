import justpy as jp

def hint_test():
    wp = jp.QuasarPage()
    d = jp.Div(classes="q-pa-md q-gutter-lg", style="max-width: 300px", a=wp)
    input1 = jp.QInput(a=d, label='My Field', hint="This is my hint.")
    s1 = jp.QSelect(label='Select Company', a=d, color='orange', clearable=True, standout=True, bottom_slots=True, counter=True,
                 hint='My hint', options=['Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'])
    return wp

jp.justpy(hint_test)
