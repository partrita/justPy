import justpy as jp

menu = '''
    <q-toolbar class="bg-grey-3">
      <q-btn flat round dense>
        <q-icon name="menu" />
         <q-menu>
          <q-list style="min-width: 100px">
            <q-item clickable v-close-popup>
              <q-item-section><a href='/about' style="text-decoration: none">about</a>
              </q-item-section>
            </q-item>
            <q-separator />
            <q-item clickable v-close-popup>
              <q-item-section><a href='/tool' style="text-decoration: none">help</a>
              </q-item-section>
            </q-item>
          </q-list>
        </q-menu>
      </q-btn>
      <q-toolbar-title>
        Toolbar
      </q-toolbar-title>
      <q-btn flat round dense>
        <q-icon name="more_vert" />
      </q-btn>
    </q-toolbar>
      '''


@jp.SetRoute('/')
def index():
    wp = jp.QuasarPage()
    c = jp.parse_html(menu, a=wp)
    wp.add(jp.P(text='Index page', classes='text-5xl m-2'))
    return wp

@jp.SetRoute('/about')
def about():
    wp = jp.WebPage()
    wp.add(jp.P(text='Hello there!', classes='text-5xl m-2'))
    return wp

jp.justpy()
