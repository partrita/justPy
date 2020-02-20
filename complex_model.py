import justpy as jp


class MyDiv(jp.Div):

    def model_update(self):
        # [wp, 'text-data'] for example
        if self.model[0].data[self.model[1]]:
            self.text = (int(self.model[0].data[self.model[1]]))*self.repeat
        else:
            self.text = self.initial_text


def model_demo():
    wp = jp.WebPage()
    d = jp.Div(a=wp, data={'text': ''})
    repeat = 2
    output = jp.Div(a=d)
    jp.Div(text=f'output', a=output)
    MyDiv(text=f'typing will go here', a=output, model=[d, 'text'],
          repeat=repeat, initial_text = 'Yada Yada')
    middle_input = jp.Input(text='',
                            placeholder='Type here',
                            model=[d, 'text'], a=d)
    return wp

jp.justpy(model_demo)
