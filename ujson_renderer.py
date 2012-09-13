###
# ujson_renderer.py
#
# Sets up ujson as a renderer. Can be used instead of the # simplejson 'json'
# which is provided by pyramid by default, or can be used as an alternative as
# needed.
#
# Note that this is not a real python package.  It's intended to be dropped
# into a common pyramid aplication package.
#
# Requires ujson (a la 'easy_install ujson')
#
# To use (replaces the default 'json' renderer):
#   # Where config is an instance of Configurator:
#   config.add_render('json', 'mystuff.ujson_renderer.Factory')
#
#
# Or (as a new renderer):
#   config.add_render('ujson', 'mystuff.ujson_renderer.Factory')
#
#
# Or (for dict/list not caught by a renderer and not proper Response objects):
#   config.add_response_adapter(mystuff.ujson_renderer.adapter, dict, list)
#
#
# Or you can just uncomment the line indicated below to enable recognition by a
# config.scan()
#

from pyramid.response import Response, response_adapter
import ujson

#
# Uncomment this if you're using configurator_instance.scan() and want a
# response adapter instead of a renderer
#@response_adapter(dict, list)
def adapter(json_thing):
    response = Response(content_type="application/json")
    # We'll write to the response body "file" in hopes that it's faster than a
    # huge standard string.  Absolutely 100% untested and uninvestigated.
    ujson.dump(json_thing, response.body_file)
    return response

class Factory:
    def __init__(self, info):
        pass

    def __call__(self, value, system):
        system['request'].response.content_type = "application/json"
        return ujson.dumps(value)

