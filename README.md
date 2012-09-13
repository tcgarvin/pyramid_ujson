ujson_renderer.py
=================

In Python [Pyramid](http://www.pylonsproject.org/), helps use [ujson](http://pypi.python.org/pypi/ujson/) to encode responses instead of the default Pyramid json encoder.

Sets up ujson as a renderer. Can be used instead of the # simplejson 'json'
which is provided by pyramid by default, or can be used as an alternative as
needed.

Note that this is not a real Python package.  It's intended to be dropped
into a common Pyramid application package.

Requires ujson (a la `easy_install ujson`)

To use (replaces the default 'json' renderer):

    # Where config is an instance of Configurator:
    config.add_render('json', 'mystuff.ujson_renderer.Factory')


Or (as a new renderer):

    config.add_render('ujson', 'mystuff.ujson_renderer.Factory')

Or (for dict/list not caught by a renderer and not proper Response objects):
  
    config.add_response_adapter(mystuff.ujson_renderer.adapter, dict, list)

Or you can just uncomment the line indicated below to enable recognition by a
config.scan()